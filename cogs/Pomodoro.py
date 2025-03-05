from discord.ext import commands
import discord
import asyncio

class Pomodoro(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    """ 輸入 %pomodoro 啟動番茄鐘 """
    @commands.command(name="pomodoro")
    async def setTimer(self, ctx, work_time: int = 30, break_time: int = 5):
        user = ctx.author  # 使用者物件
        channel = user.voice.channel if user.voice else None  # 檢查使用者是否在語音頻道
        work_channel = discord.utils.get(ctx.guild.voice_channels, name="讀書間")
        rest_channel = discord.utils.get(ctx.guild.voice_channels, name="休息室")

        # 若user不在語音頻道，發送提示請user進入語音頻道
        if not channel:
            await ctx.send(f"{user.mention} 請進入{work_channel.mention}頻道")
        while not user.voice:
            await asyncio.sleep(1)

        if user.voice.channel != work_channel:
            await user.move_to(work_channel)
        
        # 開始番茄鐘倒數work_time
        await ctx.send(f"{user.mention} 番茄鐘計時開始! 接下來{work_time}分鐘請認真工作!")

        while user.voice:
            # 等待user自定義的work_time（轉換為秒）
            for i in range(work_time*60): 
                await asyncio.sleep(1)
                if not user.voice:
                    return
        
            # 當work_time結束，發送休息提示，將user移動到休息間頻道    
            if rest_channel and user.voice:
                await ctx.send(f"{user.mention} {work_time}分鐘倒數結束! 接下來請休息{break_time}分鐘!")
                await user.move_to(rest_channel)

            # 等待user自定義的break_time（轉換為秒）
            for i in range(break_time*60): 
                await asyncio.sleep(1)
                if not user.voice:
                    return
        
            # 休息結束，開始新一輪的番茄鐘
            if work_channel and user.voice:
                await ctx.send(f"{user.mention} 休息時間結束，接下來{work_time}分鐘請認真工作!")
                await user.move_to(work_channel)

""" Cog載入Bot中 """
async def setup(bot: commands.Bot):
    await bot.add_cog(Pomodoro(bot))