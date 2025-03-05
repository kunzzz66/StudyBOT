import time
class StudyTracker:
    
    """用dict來紀錄每位使用者的開始讀書時間"""  
    def __init__(self):
        self.studyDict = {}  # 儲存 user_id -> start_time 的映射

    def add_user(self, userID): # 新增使用者的開始讀書時間
        startTime = time.time()
        self.studyDict[userID] = startTime

    def remove_user(self, userID): # 移除使用者的紀錄（代表結束讀書），並回傳開始時間
        if userID in self.studyDict:
            startTime = self.studyDict[userID]
            del self.studyDict[userID]
            return startTime
        else:
            print(f"使用者 {userID} 不在紀錄中")