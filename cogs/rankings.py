from discord.ext import commands
from utils import dbConnect
from utils import studyrank

class rankings(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    '''輸入 %rankings 獲得所有排名'''
    @commands.command( aliases=['排名'])
    async def rankings(self, ctx):
        user = ctx.author
        conn = dbConnect.getDbConnection()
        [rank_list, user_rank] = await studyrank.getRankList(conn, user)
        
        for id, totalTime, rank in rank_list:
            user = await self.bot.fetch_user(int(id))
            totalTime = int(totalTime)
            hours, remainder = divmod(totalTime, 3600) # 轉換為時、分、秒
            minutes, seconds = divmod(remainder, 60)
            await ctx.send(f"#{rank}: {user.global_name} -  {hours} 小時 {minutes} 分鐘 {seconds} 秒")

        await ctx.send(f"{ctx.author.mention} 目前排名為第{user_rank}名")
        conn.close()

# Cog載入Bot 中
async def setup(bot: commands.Bot):
    await bot.add_cog(rankings(bot))