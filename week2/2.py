def conv(feature_map, kernel):

    fm_h, fm_w = len(feature_map), len(feature_map[0])
    k_h, k_w = len(kernel), len(kernel[0])

    output_h = fm_h - k_h + 1
    output_w = fm_w - k_w + 1

    result = [[0] * output_w for _ in range(output_h)]

    for i in range(output_h):
        for j in range(output_w):
            value = 0
            for m in range(k_h):
                for n in range(k_w):
                    value += feature_map[i + m][j + n] * kernel[m][n]
            result[i][j] = value

    return result

feature_map = [
    [1, 3, 4, 0, 1],
    [6, 6, 0, 1, 2],
    [1, 2, 4, 2, 0],
    [3, 4, 3, 0, 1],
    [2, 0, 1, 5, 2]
]

kernel = [
    [2, 5, 0],
    [0, 1, 3],
    [1, 0, 2]
]

result = conv(feature_map, kernel)

print("卷积结果:")
for row in result:
    print(row)