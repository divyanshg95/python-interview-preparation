
from typing  import List

def climbing_stairs(n: int, memo: List[int])-> int:
    if n <= 2:
        memo[n] = n
    
    if memo[n] != -1:
        return memo[n] 
    
    memo[n] = climbing_stairs(n-1, memo) + climbing_stairs(n-2, memo) 

    return memo[n]


def climbing_tabularization(n: int) -> List[int]:
    memo = [0] * (n+1)
    memo[1] = 1
    memo[2] = 2

    for i in range(3, n+1):
        memo[i] = memo[i-1] + memo[i-2]

    return memo

    


if __name__ == "__main__":
    n = 10
    memo = [-1] * (n+1)
    climbing_stairs(n, memo)
    print(memo)
    t_memo = climbing_tabularization(n)
    print(t_memo)

