class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower_str = s.lower()
        fltrd_str = ''.join(filter(str.isalnum,lower_str))
        for i in range(0,len(fltrd_str)):
            print(f"{fltrd_str[i]} - {fltrd_str[len(fltrd_str)- 1 - i]}")
            if (fltrd_str[i] != fltrd_str[len(fltrd_str)- 1 - i] and fltrd_str[i].isalnum  ):
                return False
        
        return True