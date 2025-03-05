from discord.ext import commands

class HelpBOT(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        

    """ 輸入 %helpBOT或%說明 獲得機器人說明 """
    @commands.command(name="helpBOT", aliases=['說明'])
    async def helpCommand(self, ctx):
        await ctx.send(help_message)


""" Cog載入Bot中 """
async def setup(bot):
    await bot.add_cog(HelpBOT(bot))


help_message = """
**📚 Study Bot 說明文件** 📚

**%studytime**
用來顯示你累積的讀書時間（以小時、分鐘、秒為單位）以及目前排名，進入讀書間後會自動計時。

**%rankings**
用來顯示所有人的讀書時間排名。。

**%pomodoro [工作時間] [休息時間]**
使用番茄鐘功能，設定工作時間與休息時間。

**指令說明：**
- `[工作時間]`：設定每次工作時間的分鐘數（例如 30 分鐘）。
- `[休息時間]`：設定每次休息時間的分鐘數（例如 5 分鐘）。

範例：
`%pomodoro 30 5`  
這會設置工作 30 分鐘，休息 5 分鐘的番茄鐘計時。

當你啟動番茄鐘時，工作與休息時間會依照你的設置自動循環。

🔥 **開始你的學習之旅吧！** 🔥
      """