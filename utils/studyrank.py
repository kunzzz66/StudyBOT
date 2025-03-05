
""" 特定user讀書時間的排名 """ 
def getMyRank(conn, user):
    cursor = conn.cursor()
    query = """
    WITH RankedUsers AS (
        SELECT id, totalTime,
               RANK() OVER (ORDER BY totalTime DESC) AS rank
        FROM users
    )
    SELECT rank FROM RankedUsers WHERE id = ?;
    """
    cursor.execute(query, (user.id,))
    rank = cursor.fetchone()

    return rank[0] if rank else None

""" get讀書時間排行榜 """
async def getRankList(conn, user):
    cursor = conn.cursor()
    query = """
    SELECT id, totalTime,
           RANK() OVER (ORDER BY totalTime DESC) AS rank
    FROM users;
    """
    cursor.execute(query)
    rankList = cursor.fetchall()
    userRank = getMyRank(conn, user)
    return [rankList,userRank]