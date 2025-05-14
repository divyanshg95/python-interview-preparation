
from typing import List


# following method compute the fibonnaci 
# with top-down appoach of memorisation. 
# In top-down approach recursively call the 
# sub-problems and every time store the 
# solution of subproblem 
def fibbonaci_memorisation():

    # while designing such solution you should 
    # think about terminal condition for recursion 
    # also think about the storing the solution 
    # before calling the recursive step
    def memo_fabb(n: int, memo:List[int]):
        if n <= 1:
            memo[n] = n
            return n 
        
        if memo[n] != -1:
            return memo[n]

        memo[n] = memo_fabb(n-1, memo) + memo_fabb(n-2, memo)

        return memo[n]
    
    n = 10
    
    memo = [-1 for _ in range(0,n)]
    memo_fabb(n-1, memo)
    print(memo)


        
    




# tabularisation approach, it is bottom-up 
# approach first calculate subproblem and 
# store their results and slowly build bigger 
# solutions using already calculated sub-problems. 
# This approach uses iteration. 
# for this approch you should figure out initialisation 
# step, iteratively filing the result memo table
def fibonacci_tabularisation():
    n = 10
    memo = [0] * 10
    memo[1] = 1

    for i in range (2, n):
        memo[i] = memo[i-1] + memo[i-2]

    print(memo)





if __name__ == "__main__":
    fibbonaci_memorisation()
    fibonacci_tabularisation()
