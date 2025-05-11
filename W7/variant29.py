import sys


def main(x):
    return first_node(x)


def first_node(x):
    if x[4] == 'TCL':
        return second_node(x)
    elif x[4] == 'IOKE':
        return 10
    return -1


def second_node(x):
    if x[0] == 1967:
        return third_node_upper(x)
    elif x[0] == 1977:
        return third_node_lower(x)
    return -1


def third_node_upper(x):
    if x[1] == 'ASP':
        return forth_node_upper(x)
    elif x[1] == 'JFLEX':
        return forth_node_midle(x)
    return -1


def third_node_lower(x):
    if x[1] == 'ASP':
        return 6
    elif x[1] == 'JFLEX':
        return forth_node_lower(x)
    return -1


def forth_node_upper(x):
    if x[3] == 'HLSL':
        return 0
    elif x[3] == 'STAN':
        return 1
    elif x[3] == 'EQ':
        return 2
    return -1


def forth_node_midle(x):
    if x[2] == 'REBOL':
        return 3
    elif x[2] == 'EQ':
        return 4
    elif x[2] == 'FORTH':
        return 5
    return -1


def forth_node_lower(x):
    if x[3] == 'HLSL':
        return 7
    elif x[3] == 'STAN':
        return 8
    elif x[3] == 'EQ':
        return 9
    return -1


if __name__ == "__main__":
    args = sys.argv[1:]
    x_input = [
        int(args[0]) if args[0].isdigit() else args[0],
        args[1],
        args[2],
        args[3],
        args[4]
    ]
    print(main(x_input))
