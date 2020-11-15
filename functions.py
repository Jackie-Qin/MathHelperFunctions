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


def GaussianElimSPP():
    matrix = [
        [0.4096, 0.1234, 0.3678, 0.2943, 0.4043],
        [0.2246, 0.3872, 0.4015, 0.1129, 0.1550],
        [0.3645, 0.1920, 0.3781, 0.0643, 0.4240],
        [0.1784, 0.4002, 0.2786, 0.3927, 0.2557],
    ]
    rowNum = 4
    scaledVector = []
    index = []
    backSub = []

    for i in range(rowNum):
        scaledVector.append(0)
        index.append(i)
        for j in range(rowNum + 1):
            if abs(matrix[i][j]) > scaledVector[i] and j != rowNum:
                scaledVector[i] = abs(matrix[i][j])

    pos = 0
    # elimination
    while 1:
        compare = []
        for i in range(rowNum):
            if i not in backSub:
                compare.append(abs(matrix[i][pos]) / scaledVector[i])

        # updating index, backSub vector
        nextIndex = compare.index(max(compare))
        index[pos], index[index[nextIndex]] = index[index[nextIndex]], index[pos]
        backSub.append(index[pos])

        for i in range(rowNum):
            if i in backSub:
                continue
            divide = matrix[i][pos] / matrix[index[pos]][pos]
            for j in range(pos, rowNum + 1):
                matrix[i][j] -= matrix[index[pos]][j] * divide
                if abs(matrix[i][j]) < 10**(-10):
                    matrix[i][j] = 0

        pos += 1
        if pos == rowNum - 1:
            backSub.append(index[len(index) - 1])
            break

    # back substitution
    backSub.reverse()
    res = [0] * rowNum
    res[backSub[0]] = matrix[backSub[0]][rowNum] / matrix[backSub[0]][rowNum - 1]
    for i in range(1, rowNum):
        temp = matrix[backSub[i]][rowNum]
        for k in range(i):
            temp -= matrix[backSub[i]][rowNum - k - 1] * res[rowNum - k - 1]
        res[rowNum - i - 1] = temp / matrix[backSub[i]][rowNum - i - 1]

    print(res)
