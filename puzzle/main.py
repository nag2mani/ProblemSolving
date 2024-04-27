from collections import Counter

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                for e in range(1, 10):
                    for f in range(1, 10):
                        for g in range(1, 10):
                            for h in range(1, 10):
                                for i in range(1, 10):
                                    check_list = [a, b, c, d, e, f, g, h, i]
                                    lst = list(Counter(check_list).values())
                                    for item in lst:
                                        if isinstance(item, int) and item > 1:
                                            continue
                                        else:
                                            sum1 = a + b + c
                                            sum2 = d + e + f
                                            sum3 = g + h + i
                                            sum4 = a + d + g
                                            sum5 = b + e + h
                                            sum6 = c + f + i
                                            sum7 = a + e + i
                                            sum8 = c + e + g
                                            if sum1 == 15 and sum2 == 15 and sum3 == 15 and \
                                            sum4 == 15 and sum5 == 15 and sum6 == 15 and \
                                            sum7 == 15 and sum8 == 15:
                                                print("Solution found:")
                                                print(a, b, c)
                                                print(d, e, f)
                                                print(g, h, i)
                                                print("--------------------------------")

                                                