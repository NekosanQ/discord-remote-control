# main.py
import discord_bot
import gui
import threading
import asyncio

# メッセージキューからメッセージを取得して送信する関数
def send_from_queue():
    while True:
        channel_id, message = gui.message_queue.get()
        asyncio.run_coroutine_threadsafe(discord_bot.send_message(discord_bot.client, channel_id, message), discord_bot.client.loop)

# ボットを別スレッドで起動
bot_thread = threading.Thread(target=discord_bot.start_bot)
bot_thread.daemon = True
bot_thread.start()

# メッセージキューからメッセージを取得して送信するスレッドを作成
send_thread = threading.Thread(target=send_from_queue)
send_thread.daemon = True
send_thread.start()

# GUIを起動
gui.gui()