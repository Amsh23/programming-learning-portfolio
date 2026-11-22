# VocaVault

A Telegram music downloader bot that organizes audio into three categories:

- **Hatsune Miku** — `/miku`
- **Kasane Teto** — `/teto`
- **Other** — `/other`

The bot accepts one or multiple YouTube links (one per line), downloads audio with yt-dlp, converts it to MP3 with FFmpeg, and sends each audio file back in Telegram.

## Requirements

- Python 3.10+
- FFmpeg installed and available in PATH
- A Telegram bot token from [@BotFather](https://t.me/BotFather)

## Setup

```bash
python -m venv .venv
```

Windows:

```powershell
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file by copying `.env.example`, then add your Telegram bot token:

```env
BOT_TOKEN=your_real_token
```

Run:

```bash
python bot.py
```

## Usage

1. Open your bot in Telegram and send `/start`.
2. Choose a category using `/miku`, `/teto`, or `/other`.
3. Send one or more YouTube URLs, each on a separate line.
4. The bot downloads and sends each audio track as an MP3.

Downloaded files are stored locally under `downloads/` and are excluded from Git.

## Notes

- Private, deleted, age-restricted, or region-restricted videos may fail to download.
- Keep your real `.env` file private. Never commit bot tokens or downloaded media.
- Use this project only for content you have permission to download and use, and follow YouTube's terms and applicable copyright law.
