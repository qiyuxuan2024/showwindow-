import tkinter as tk
import time
from tkinter import ttk as ttk

def showwindow(window_size="300x500",title=None,text=None,buttontext=None,entrytext=None,buttoncheck=None,):
    print('Hello from the showwindow')
    time.sleep(0.5)
    print('v1.03')
    time.sleep(2)
    while True:
        a = input("Please write your e-mail")
        if '@' not in a:
            print('Please enter a valid e-mail')
        else:
            f = open("email.txt", "a")
            f.write(a)
            f.close()
            break

    window = tk.Tk()
    if title is not None:
        window.title(title)
    else:
        print('请定义标题！')
    window.geometry(window_size)
    if text is not None:
        text = tk.Label(window,text=text)
        text.pack()
    if entrytext is not None:
        entry = tk.Entry(window)
        entry.pack()
    if buttontext is not None or buttoncheck is not None:

            try:
                button = tk.Button(window,text=buttontext,command=buttoncheck)
                button.pack()
            except NameError:
                print('请定义按钮按下的事件或函数处理错误')




    window.mainloop()
def button_check():
    from tkinter.messagebox import showinfo
    showinfo('成功！')






