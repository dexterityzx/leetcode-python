# 375
#buttom up
'''
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number I picked is higher or lower.

However, when you guess a particular number x, and you guess wrong, you pay $x. You win the game when you guess the number I picked.

Example:

n = 10, I pick 8.

First round:  You guess 5, I tell you that it's higher. You pay $5.
Second round: You guess 7, I tell you that it's higher. You pay $7.
Third round:  You guess 9, I tell you that it's lower. You pay $9.

Game over. 8 is the number I picked.

You end up paying $5 + $7 + $9 = $21.
Given a particular n ≥ 1, find out how much money you need to have to guarantee a win.

'''
dp = [[0]*(n+1) for _ in range(0,n+1)]
for startNum in range(n, 0, -1):
    for endNum in range(startNum+1,n+1):
    	dp[startNum][endNum]= min(guessNum+max(dp[startNum][guessNum-1],dp[guessNum+1][endNum]) 
                        for guessNum in range(startNum,endNum))
           
print dp;