class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        parts = queryIP.split(".")
        if len(parts) != 4:
            return False
        
        for p in parts:
            if (
                (not p.isdigit()) or            # not numbers    
                (len(p)>0 and p[0] == '0') or   # MSB = 0
                (not (0<=int(p)<=255))          # not within range
            ): return False

        return True