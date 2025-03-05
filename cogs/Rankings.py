from discord.ext import commands
from utils import dbConnect
from utils import studyrank

class Rankings(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    """ 輸入 %rankings或%排名 獲得所有排名 """
    @commands.command(aliases=['排名'])
    async def rankings(self, ctx):
        user = ctx.author
        conn = dbConnect.getDbConnection()
        [rankList, userRank] = await studyrank.getRankList(conn, user)
        
        # print出每個使用者的排名
        for id, totalTime, rank in rankList:
            user = await self.bot.fetch_user(int(id))
            totalTime = int(totalTime)
            
            # 轉換totalTime為時、分、秒
            hours, remainder = divmod(totalTime, 3600) 
            minutes, seconds = divmod(remainder, 60)
            await ctx.send(f"#{rank}: {user.global_name} -  {hours} 小時 {minutes} 分鐘 {seconds} 秒")

        await ctx.send(f"{ctx.author.mention} 目前排名為第{userRank}名")
        conn.close()

""" Cog載入Bot中 """
async def setup(bot: commands.Bot):
    await bot.add_cog(Rankings(bot))