import time
class StudyTracker:
    
    """用dict來紀錄每位使用者的開始讀書時間"""  
    def __init__(self):
        self.study_dict = {}  # 儲存 user_id -> start_time 的映射

    def add_user(self, user_id): # 新增使用者的開始讀書時間
        start_time = time.time()
        self.study_dict[user_id] = start_time

    def remove_user(self, user_id): # 移除使用者的紀錄（代表結束讀書），並回傳開始時間
        if user_id in self.study_dict:
            start_time = self.study_dict[user_id]
            del self.study_dict[user_id]
            return start_time
        else:
            print(f"使用者 {user_id} 不在紀錄中")