import threading

class Logger:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                print("Creating new Logger instance...")
                cls._instance = super().__new__(cls)
            return cls._instance

    def log(self, message):
        print(f"[LOG]: {message}")

# Usage
logger1 = Logger()
logger2 = Logger()

print(logger1 is logger2)  # True, both are same instance
logger1.log("User logged in")
logger2.log("User clicked checkout")