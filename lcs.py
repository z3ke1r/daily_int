def lcs(s, t):
    m = len(s)
    n = len(t)
    matrix = [[0 for x in range(m + 1)] for y in range(n + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i-1] is t[j-1]:
                matrix[i][j] = 1 + matrix[i-1][j-1]
            else:
                matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])

    return matrix[m][n]


s = "kitten"
t = "sitten"

print("the lcs is: ", lcs(s, t))
