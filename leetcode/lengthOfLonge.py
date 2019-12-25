class Solution:
    def lengthOfLongestSubstring(self,s:str) -> int:
        """
        :type s: str
        :rtype: int
        """
        max_number = 0
        number = 0
        test = ''
        for i in s:
            if i not in test:
                test += i
                number += 1
            else:
                if number >= max_number:
                    max_number = number
                index = test.index(i)
                test = test[(index+1):] + i
                number = len(test)
        if number > max_number:
            max_number = number
        return max_number

if __name__ == "__main__":
    #s1 = str('dfafdgfsfgretbvcbghewdfsfdsafdafdsadfehn')
    s1 = 'dfafdgfsfgretbvcbghewdfsfdsafdafdsadfehn'
    so = Solution()
    num = so.lengthOfLongestSubstring(s1)
    print (num)