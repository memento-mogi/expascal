def generate(num):
    prime_l = []
    kosu = 0
    i = 2
    while kosu <= num:
        for j in prime_l:
            if i % j == 0:
                break
        else:
            prime_l.append(i)
            kosu = kosu + 1
        i = i + 1

    return prime_l

if __name__=="__main__":
    print(generate(100))

