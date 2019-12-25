if __name__ == '__main__':
    res = 0
    m = 1
    for n in range(1000):
        m = m * 0.9
        res += 100 * m
    print(res)
