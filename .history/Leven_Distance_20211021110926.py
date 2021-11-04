
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
        for idx in range(len(w2)):
            if idx < len(w1):
                if w1[idx] != w2[idx]:
                    counter += 1
                    
            elif idx >= len(w1):
                counter += 1
        return counter
                
if __name__ == '__main__':
    print(calc_lev("this", "this"))
    print(calc_lev("that", "this"))
    print(calc_lev("this", "then that"))
