import discord
from discord.ext import commands
import json
from StudyBot import StudyBOT
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__)) # 取得當前目錄
CONFIG_PATH = os.path.join(BASE_DIR, "data", "config.json")

with open(CONFIG_PATH, "r") as f:
    print(BASE_DIR)
    config = json.load(f)

if __name__ == "__main__":
    # intents是要求機器人的權限
    intents = discord.Intents.all()
    # command_prefix是前綴符號，可以自由選擇($, #, &...)
    studyBOT = StudyBOT(command_prefix=config["PREFIX"], intents=intents)

    studyBOT.run(config["TOKEN"])