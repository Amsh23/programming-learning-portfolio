# def func(a,*args,**kwargs):
#     print(a)
#     print(args)
#     print(kwargs)
# func(10,20,30,40,50,x=50,y=70)



def send_email(*reciptions,**option):
    print("reciptions:",reciptions)
    print(":  option",option)
    print(" start send email")


send_email("ph.rafie@gmail.com",
           "parham@gmail.com",cc="arash@gmail.com",bcc="maryam@gmail.com",subject="hi",attachments=["file1","file2"])