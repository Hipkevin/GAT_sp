def add(alpha1, alpha2):
    node_num = alpha1.shape[0]

    result = []
    for i in range(node_num):

        temp = 0
        for j in range(node_num):
            if i != j:
                temp += alpha1[i][j] + alpha2[j][i]

        result.append(temp)

    return result


def plus(alpha1, alpha2):
    node_num = alpha1.shape[0]

    result = []
    for i in range(node_num):

        temp = 0
        for j in range(node_num):
            if i != j:
                temp += alpha1[i][j] * alpha2[j][i]

        result.append(temp)

    return result