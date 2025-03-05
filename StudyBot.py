from discord.ext import commands
import os
from utils.updateState import updateState
from utils.StudyTracker import StudyTracker
from utils.dbConnect import getDbConnection


BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # 取得當前StudyBot.py的目錄
COGS_DIR = os.path.join(BASE_DIR, "cogs")

class StudyBOT(commands.Bot):
    def __init__(self, command_prefix, intents):
        super().__init__(command_prefix=command_prefix, intents=intents)
        
        # 紀錄使用者開始讀書的時間
        self.studyTracker = StudyTracker()
        self.event(self.on_ready)
           
        # 連接資料庫
        conn = getDbConnection()
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                user_id TEXT PRIMARY KEY,
                totalTime INTEGER
            )
        ''')
        conn.close()
        
    """ 當機器人完成啟動 """
    async def on_ready(self):
        print(f"目前登入身份 --> {self.user}")
        # 自動載入cogs(指令擴充)
        await self.load_cogs()
        # for command in self.commands:
        #     print(command.name)
    
    """ 進入讀書間開始計時讀書時間 """
    async def on_voice_state_update(self, member, before, after):
        await updateState(member, before, after, self.studyTracker)
    
    """ 自動載入cogs(指令擴充) """
    async def load_cogs(self):
        for filename in os.listdir(COGS_DIR):
            if filename.endswith(".py"):
                await self.load_extension(f"cogs.{filename[:-3]}")  # 去掉.py
