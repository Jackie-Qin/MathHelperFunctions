import numpy


def gaussianElim():
    rowNum = int(input("Please enter the number of rows: "))
    matrix = numpy.zeros((rowNum, rowNum + 1))
    res = numpy.zeros(rowNum)

    print("Please enter the augmented matrix coefficients: ")
    for i in range(rowNum):
        for j in range(rowNum + 1):
            matrix[i][j] = float(input("matrix[" + str(i) + "][" + str(j) + "]="))

    for i in range(rowNum):
        for j in range(i + 1, rowNum):
            divide = matrix[j][i] / matrix[i][i]
            for k in range(rowNum + 1):
                matrix[j][k] = matrix[j][k] - divide * matrix[i][k]

    res[rowNum - 1] = matrix[rowNum - 1][rowNum] / matrix[rowNum - 1][rowNum - 1]
    for i in range(rowNum - 2, -1, -1):
        res[i] = matrix[i][rowNum]
        for j in range(i + 1, rowNum):
            res[i] = res[i] - res[j] * matrix[i][j]

        res[i] /= matrix[i][i]

    print("solution is:")
    for i in range(rowNum):
        print('X%d = %.4f' % (i + 1, res[i]), end = '\t')


