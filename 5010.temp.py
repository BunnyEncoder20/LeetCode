class Temp:
    def __init__(self, name, position):
        self.name = name 
        self.position = position
    
    @staticmethod
    def solution(x, y):
        print(f"Name:{x} | Position:{y}")

Temp.solution("Varun", "NA")
