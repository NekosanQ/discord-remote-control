# discord_bot.py
import discord
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

# ボットを起動する関数
def start_bot():
    client.run(DISCORD_TOKEN)
