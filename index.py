import tkinter as tk
import discord


#関数定義
def get_id_pass():
    id = text_1.get()
    password = text_2.get()
    print('ID:',id)
    print('Pass:',password)

def set_clear():
    text_1.set('')
    text_2.set('')

win = tk.Tk()
win.title("Discord遠隔操作")

#オブジェクトの定義
label_1 = tk.Label(win,text='ユーザ名')
text_1 = tk.StringVar()
entry_1 = tk.Entry(win,textvariable=text_1)

label_2 = tk.Label(win,text='パスワード')
text_2 = tk.StringVar()
entry_2 = tk.Entry(win, show='*',textvariable=text_2)

button_1 = tk.Button(win,text = 'OK',command=lambda:get_id_pass())
button_2 = tk.Button(win,text = 'Clear',command=lambda:set_clear())
button_3 = tk.Button(win,text = 'Quit',command=quit)

#レイアウト
label_1.grid(row=0,column=0)
entry_1.grid(row=0,column=1)
label_2.grid(row=1,column=0)
entry_2.grid(row=1,column=1)
button_1.grid(row=2,column=0)
button_2.grid(row=2,column=1)
button_3.grid(row=2,column=2)

win.mainloop()