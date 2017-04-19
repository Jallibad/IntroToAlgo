def editDistance(x, y):
    m = len(x)
    n = len(y)
    distances = [[0 for _ in range(n+1)] for _ in range(m+1)]
    arrows = [[None for _ in range(n+1)] for _ in range(m+1)]
    for i in range(1,m+1):
        distances[i][0] = i
        arrows[i][0] = (i-1,0)
    for j in range(1,n+1):
        distances[0][j] = j
        arrows[0][j] = (0,j-1)
    for j in range(1,n+1):
        for i in range(1,m+1):
            arrows[i][j] = (i-1,j-1)
            if x[i-1] == y[j-1]:
                distances[i][j] = distances[i-1][j-1]
            else:
                part = min(distances[i-1][j], distances[i][j-1], distances[i-1][j-1])
                distances[i][j] = 1+part
                if part == distances[i][j-1]:
                    arrows[i][j] = (i,j-1)
                if part == distances[i-1][j]:
                    arrows[i][j] = (i-1,j)
                if part == distances[i-1][j-1]:
                    arrows[i][j] = (i-1,j-1)
    topAns = ""
    bottomAns = ""
    i, j = m, n
    while (i,j) != (0,0):
        if arrows[i][j] == (i-1,j):
            topAns = x[i-1]+topAns
            bottomAns = "-"+bottomAns
        elif arrows[i][j] == (i,j-1):
            topAns = "-"+topAns
            bottomAns = y[j-1]+bottomAns
        else:
            topAns = x[i-1]+topAns
            bottomAns = y[j-1]+bottomAns
        i, j = arrows[i][j]
    return distances[m][n], topAns, bottomAns

if __name__ == "__main__":
    x = "exponential"
#   x = "CATAAGCTTCTGACTCTTACCTCCCTCTCTCCTACTCCTGCTCGCATCTGCTATAGTGGAGGCCGGAGCAGGAACAGGTTGAACAG"
    y = "polynomial"
#   y = "CGTAGCTTTTTGGTTAATTCCTCCTTCAGGTTTGATGTTGGTAGCAAGCTATTTTGTTGAGGGTGCTGCTCAGGCTGGATGGA"
    distance, top, bottom = editDistance(x,y)
    print("edit distance = " + str(distance))
    print("alignment:")
    print(top)
    print(bottom)
