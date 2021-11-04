
def calc_lev(w1, w2):
    print(w1, w2)
    
    counter = 0

    # case 1: same word
    if w1 == w2:
        return counter

        # case 2: same length
        if len(w1) == len(w2):
            for idx in range(len(w2)):
                if w1[idx] != w2[idx]:
                    counter += 1
            return counter

    # case 3: not same length
    if len(w1) != len(w2):
        for w1[idx] in range(len(w2)):
            if w1[idx] != w2[idx]:
                counter += 1
        return counter

if __name__ == '__main__':
    print(calc_lev("this", "this"))
    print(calc_lev("that", "that"))
    print(calc_lev("this", "that"))
