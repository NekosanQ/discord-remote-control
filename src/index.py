import tkinter as tk
import discord
import tkinter as tk
import threading
import asyncio
import queue
import os
from dotenv import load_dotenv

load_dotenv(".env")

# TOKEN取得
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print(f"ログインしました: {client.user.name}")
# メッセージ送信関数
async def send_message(bot, channel_id, message):
    target_channel = bot.get_channel(int(channel_id))
    if target_channel is not None:
        await target_channel.send(message)
        print("送信完了")
    else:
        print("Channel not found.")
# メッセージキューの作成
message_queue = queue.Queue()

# ボットを起動する関数
def start_bot():
    client.run(DISCORD_TOKEN)

# ボットを別スレッドで起動
bot_thread = threading.Thread(target=start_bot)
bot_thread.daemon = True
bot_thread.start()

# メッセージキューからメッセージを取得して送信する関数
def send_from_queue():
    while True:
        channel_id, message = message_queue.get()
        asyncio.run_coroutine_threadsafe(send_message(client, channel_id, message), client.loop)

# メッセージキューからメッセージを取得して送信するスレッドを作成
send_thread = threading.Thread(target=send_from_queue)
send_thread.daemon = True
send_thread.start()

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

# GUIを起動
gui()
