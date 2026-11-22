import asyncio
import logging
import os
import re
import shutil
from pathlib import Path
from urllib.parse import urlparse

import yt_dlp
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
BASE_DIR = Path(__file__).resolve().parent
DOWNLOAD_DIR = BASE_DIR / "downloads"
CATEGORIES = {"miku": "Hatsune Miku", "teto": "Kasane Teto", "other": "Other"}
URL_RE = re.compile(r"https?://(?:www\.)?(?:youtube\.com|youtu\.be)/\S+", re.I)

logging.basicConfig(
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger("VocaVault")


def safe_filename(value: str) -> str:
    value = re.sub(r'[<>:"/\\|?*\x00-\x1f]', "_", value)
    return value.strip(" ._")[:150] or "audio"


def download_audio(url: str, category: str) -> Path:
    """Download a YouTube video and extract its audio as MP3."""
    output_dir = DOWNLOAD_DIR / CATEGORIES[category]
    output_dir.mkdir(parents=True, exist_ok=True)

    options = {
        "format": "bestaudio/best",
        "outtmpl": str(output_dir / "%(title).150B [%(id)s].%(ext)s"),
        "noplaylist": True,
        "quiet": True,
        "no_warnings": True,
        "restrictfilenames": True,
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }],
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)
        audio_path = Path(filename).with_suffix(".mp3")

    if not audio_path.exists():
        raise FileNotFoundError("The MP3 output was not created. Check FFmpeg installation.")
    return audio_path


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "🎧 Welcome to VocaVault!\n\n"
        "Send one or more YouTube links after choosing a category:\n"
        "/miku — Hatsune Miku\n"
        "/teto — Kasane Teto\n"
        "/other — Other music\n\n"
        "Then send the YouTube link(s)."
    )


async def choose_category(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    command = update.message.text.split()[0].lstrip("/").split("@")[0].lower()
    context.user_data["category"] = command
    await update.message.reply_text(
        f"Category selected: {CATEGORIES[command]}\n"
        "Now send one or more YouTube links (one per line)."
    )


async def handle_links(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    category = context.user_data.get("category")
    if category not in CATEGORIES:
        await update.message.reply_text("First choose a category with /miku, /teto, or /other.")
        return

    urls = URL_RE.findall(update.message.text or "")
    if not urls:
        await update.message.reply_text("I couldn't find a supported YouTube link.")
        return

    await update.message.reply_text(f"⏬ Starting {len(urls)} download(s) for {CATEGORIES[category]}...")

    for index, url in enumerate(urls, start=1):
        try:
            audio_path = await asyncio.to_thread(download_audio, url, category)
            with audio_path.open("rb") as audio_file:
                await update.message.reply_audio(
                    audio=audio_file,
                    title=audio_path.stem[:64],
                    read_timeout=120,
                    write_timeout=120,
                    connect_timeout=30,
                )
            await update.message.reply_text(f"✅ {index}/{len(urls)} completed.")
        except Exception as exc:
            logger.exception("Download failed for %s", url)
            await update.message.reply_text(
                f"❌ {index}/{len(urls)} failed.\n"
                f"Reason: {str(exc)[:300]}\n"
                "The video may be private, unavailable, or restricted."
            )


def main() -> None:
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN is missing. Copy .env.example to .env and add your bot token.")
    if shutil.which("ffmpeg") is None:
        raise RuntimeError("FFmpeg was not found. Install FFmpeg and add it to PATH.")

    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    for command in CATEGORIES:
        app.add_handler(CommandHandler(command, choose_category))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_links))

    logger.info("VocaVault is running...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
