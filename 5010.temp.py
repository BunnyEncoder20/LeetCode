class Solution:
    # Mappings
    ones_map = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        10: "Ten",
        11: "Eleven",
        12: "Twelve",
        13: "Thirteen",
        14: "Fourteen",
        15: "Fifteen",
        16: "Sixteen",
        17: "Seventeen",
        18: "Eighteen",
        19: "Nineteen"
    }

    tens_map = {
        2: "Twenty",
        3: "Thirty",
        4: "Forty",
        5: "Fifty",
        6: "Sixty",
        7: "Seventy",
        8: "Eighty",
        9: "Ninety",
    }

    def numberToWords(self, num: int) -> str:
        place_suffixes = ["", " Thousand", " Million", " Billion"]

        # trivial case
        if num == 0:
            return "Zero"
        

        resultant = ""
        i = 0

        while num:
            last3digit = num % 1000
            
            # there might be 000 block
            if last3digit:
                p1 = self.tripleDigit_convertor(last3digit)
                p2 = place_suffixes[i]
                resultant = p1 + p2 + resultant
            
            i += 1
            num //= 1000
        
        # strip trailing whitespaces
        return resultant.strip()

        
    
    def tripleDigit_convertor(self, n):
        res = ""
        hundredth_place, tenth_once_place = divmod(n, 100)

        # hundredth place might be a 0
        if hundredth_place:
            res += " " + Solution.ones_map[hundredth_place] + " Hundred"
        
        # check if last 2 places are above or below 20
        # will need diff mapping for each
        if tenth_once_place >= 20:
            tenth_place, ones_place = divmod(tenth_once_place, 10)
            
            # diffinately something in tenth place
            res += " "+Solution.tens_map[tenth_place]
            
            # ones place might be 0
            if ones_place: res += " " + Solution.ones_map[ones_place]
        
        # only non-zero last 2 digits
        elif tenth_once_place:
            res += " " + Solution.ones_map[tenth_once_place]

        return res


Solution().numberToWords(100)