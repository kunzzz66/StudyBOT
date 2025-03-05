import time
import discord
import utils.dbConnect as dbConnect

""" user進入或離開讀書間 """
async def updateState(member, before, after, studyTracker):
    conn = dbConnect.getDbConnection()
    if after.channel is not None and after.channel.name == "讀書間": # user加入讀書間語音頻道
        # await member.send("開始讀書") # Send a DM to the member who joined
        print(member.global_name + " entered")
        if not after.mute :
            try:
                await member.edit(mute=True) # 強制禁音
                print(f"{member.global_name} has been muted in {after.channel.name}.")
            except discord.Forbidden:
                print(f"Could not mute {member.name}, missing permissions.")
        studyTracker.add_user(member.id)

    elif before.channel is not None and after.channel is not None: # user進入休息室
        if before.channel.name == "讀書間" and after.channel.name == "休息室":
            await member.edit(mute=False) #解除強制禁音
            updateTime(conn, member.id, studyTracker) # 更新讀書時間
            print(member.global_name + " left")

    elif after.channel is None and before.channel is not None: # user離開語音頻道
        if before.channel.name == "讀書間" :
            updateTime(conn, member.id, studyTracker) # 更新讀書時間
            print(member.global_name + " left")
    conn.close()

""" 更新database中user的讀書時間 """
def updateTime(conn, user_id, studyTraker):
    cursor = conn.cursor()
    endTime = time.time()
    startTime = studyTraker.remove_user(user_id)
    totalTime =  endTime - startTime

    # 取得user的totalTime
    cursor.execute('SELECT totalTime FROM users WHERE id = ?', (str(user_id),))
    result = cursor.fetchone()
    if result: # 若資料已存在(user非第一次進入讀書頻道)
        totalTime += result[0]

    # 更新user的totalTime
    query = """
    INSERT INTO users (id, totalTime) 
    VALUES (?, ?) 
    ON CONFLICT(id) DO UPDATE SET totalTime = excluded.totalTime
    """
    cursor.execute(query, (str(user_id), totalTime))
    conn.commit()
