class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}

        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0
            res = dfs(i + 1)
            if (i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456"))):
                res += dfs(i+2)
            dp[i] = res
            return res

        return dfs(0)


'''
    {4: 1, 3: 1, 2: 2, 1: 3, 0: 5}
    i = 4

    2

    2 2  
    22   

    2 2 1 
    22 1 
    2 21 

    2 2 1 4
    22 1 4
    2 21 4
    22 14
    2 2 14

    2214
      ^
     
 

  1 2 3 4
  ___

  1 2

  12

  1 2 3 
  12 3 
  1 23
'''
