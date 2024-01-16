# gui.py
import tkinter as tk
import queue

# メッセージキューの作成
message_queue = queue.Queue()

# GUI関数
def gui():
    # 関数定義
    def get_message():
        channel_id = text_1.get()
        message = text_2.get()
        print("チャンネルID: ", channel_id)
        print("送信したメッセージ: ", message)
        message_queue.put((channel_id, message))

    def set_clear():
        text_1.set("")
        text_2.set("")

    win = tk.Tk()
    win.title("Discord遠隔操作")

    # オブジェクトの定義
    label_1 = tk.Label(win,text= "チャンネルID")
    text_1 = tk.StringVar()
    entry_1 = tk.Entry(win,textvariable=text_1)

    label_2 = tk.Label(win,text= "メッセージ")
    text_2 = tk.StringVar()
    entry_2 = tk.Entry(win, textvariable=text_2)

    button_1 = tk.Button(win,text = "送信",command=lambda: get_message())
    button_2 = tk.Button(win,text = "クリア",command=lambda:set_clear())
    button_3 = tk.Button(win,text = "Quit",command=quit)

    # レイアウト
    label_1.grid(row=0,column=0)
    entry_1.grid(row=0,column=1)
    label_2.grid(row=1,column=0)
    entry_2.grid(row=1,column=1)
    button_1.grid(row=2,column=0)
    button_2.grid(row=2,column=1)
    button_3.grid(row=2,column=2)

    win.mainloop()
