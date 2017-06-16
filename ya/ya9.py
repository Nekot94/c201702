def matrix(N=1, M=0, a=0):
    M = N if M == 0 else M
    matrix = [[a for i in range(M)] for j in range(N)]
    # print(matrix)
    # for i in range(N):
    #     for j in range(M):
    #         print(matrix[i][j], end=" ")
    #     print()
    return matrix

# matrix()
# matrix(N=10)
# matrix(N=3, M=5)
# matrix(N=3, M=5, a="$")


