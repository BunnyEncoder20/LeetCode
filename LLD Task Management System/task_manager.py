from datetime import datetime
from task import Task, TaskStatus
from user import User

class TaskManager:
    _instance = None
    
    def __init__(self):
        if TaskManager._instance is None:
            TaskManager._instance = self
            self.tasks = {}
            self.user_tasks = {}
        else:
            raise Exception("⚠️ Manager class is singleton")
    
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls()
        return cls._instance

    