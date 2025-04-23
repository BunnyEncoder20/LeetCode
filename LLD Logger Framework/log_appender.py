from abc import ABC, abstractmethod

class LogAppender(ABD):
    @abstractmethod
    def append(self, log_message):
        pass