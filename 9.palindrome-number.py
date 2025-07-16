class Solution:
    def isPalindrome(self, x: int) -> bool:
        # all negative are auto false
        if x < 0: return False

        # get the starting denominator for getting msb value
        deno = 1
        while x >= 10 * deno:
            deno *= 10

        while x:
            # fetch first and last digit of number
            msb, lsb = x//deno, x%10

            # check palindrome
            if msb != lsb: return False

            # update x and denominator of msb
            x = (x % deno) // 10    # remove first and last digit from num
            deno /= 100             # /100 cause we removed 2 digits

        return True
