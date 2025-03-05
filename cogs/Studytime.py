from discord.ext import commands
from utils import dbConnect
from utils import studyrank

class Studytime(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    """ 輸入 %studytime 呼叫指令，輸出累積讀書時間 """
    @commands.command()
    async def studytime(self, ctx):
        user = ctx.author
        # 連接資料庫
        conn = dbConnect.getDbConnection()
        cursor = conn.cursor()
        cursor.execute('SELECT totalTime FROM users WHERE id = ?', (str(user.id),))
        result = cursor.fetchone()

        if result:
            total_time = int(result[0]) # 取得totalTime
            # 轉換為時、分、秒
            hours, remainder = divmod(total_time, 3600) 
            minutes, seconds = divmod(remainder, 60)
            rank = studyrank.getMyRank(conn, user)
            await ctx.send(f"{user.mention} 你已經讀了 {hours} 小時 {minutes} 分鐘 {seconds} 秒，目前排名為第{rank}名")
        else:
            await ctx.send(f"{user.mention} 還沒有讀書紀錄喔")

""" Cog載入Bot中 """
async def setup(bot: commands.Bot):
    await bot.add_cog(Studytime(bot))