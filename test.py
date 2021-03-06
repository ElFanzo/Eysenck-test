def get_questions():
    with open("questions.txt") as f:
        return f.readlines()


def get_result(answers: list):
    a_q = {6: 1, 12: 0, 18: 0, 24: 1, 30: 0, 36: 0, 42: 0, 48: 0, 54: 0}
    x_q = {
        1: 1,
        3: 1,
        5: 0,
        8: 1,
        10: 1,
        13: 1,
        15: 0,
        17: 1,
        20: 0,
        22: 1,
        25: 1,
        27: 1,
        29: 0,
        32: 0,
        34: 0,
        37: 0,
        39: 1,
        41: 0,
        44: 1,
        46: 1,
        49: 1,
        51: 0,
        53: 1,
        56: 1,
    }
    y_q = [
        2,
        4,
        7,
        9,
        11,
        14,
        16,
        19,
        21,
        23,
        26,
        28,
        31,
        33,
        35,
        38,
        40,
        43,
        45,
        47,
        50,
        52,
        55,
        57,
    ]
    a = x = y = 0

    for i, j in a_q.items():
        a += int(answers[i - 1]) == j

    for i, j in x_q.items():
        x += int(answers[i - 1]) == j

    for i in y_q:
        y += int(answers[i - 1]) == 1

    a_q = [-2.3, -1.8, -1.2, -0.7, -0.1, 0.4, 1, 1.6, 1.9, 2.1, 2.5]
    x_q = [
        -2.5,
        -2.2,
        -2,
        -1.8,
        -1.5,
        -1.3,
        -1.1,
        -0.9,
        -0.6,
        -0.4,
        -0.2,
        0,
        0.3,
        0.5,
        0.7,
        1,
        1.2,
        1.4,
        1.6,
        1.9,
        2.1,
        2.3,
        2.5,
        2.8,
        3,
    ]
    y_q = [
        -1.5,
        -1.3,
        -1.1,
        -0.8,
        -0.6,
        -0.4,
        -0.2,
        0.1,
        0.3,
        0.6,
        0.8,
        1,
        1.2,
        1.4,
        1.7,
        1.9,
        2.1,
        2.3,
        2.6,
        2.8,
        3,
        3.3,
        3.5,
        3.7,
        3.9,
    ]

    return [a_q[a], x_q[x], y_q[y]]
