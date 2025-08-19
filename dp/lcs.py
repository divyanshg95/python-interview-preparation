# longest common subsequence 

# building bottom up solution 
def lcs_tabularisation(s1: str, s2: str) -> int: 
    # lcs(s1,s2) -> if s1[n]==s[m] lcs(s1-1, s2-1) + 1
    # lcs(s1,s2) -> if s1[n]!=s[m] max(lcs(s1-1, s2-1), lcs(s1-1, s2), lcs(s1, s2-1))
    n1 = len(s1)
    n2 = len(s2)
    lcs = [ [-1 for _ in range(0, n1 + 1)] for _ in  range(1, n2 + 1)]

    # initialise the base case
    for i in range(0, n1):
        lcs[0][i]
        
    for i in range(0, n2):
        lcs[i][0]


    for i in range(1, n2):
        for j in range(1, n1):
            if s1[i-1] == s2[j-1]:
                lcs[i][j] = lcs[i-1][i-1] + 1
            else: 
                lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])

    return lcs[n2-1][n1-1]


if __name__ == "__main__":
    s1 = "AGGTAB"
    s2 = "GXTXAYB"
    print(lcs_tabularisation(s1, s2))