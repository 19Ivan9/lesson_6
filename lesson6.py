import random

if __name__ == '__main__':
    print('tack1:')
    m = []
    i = 0
    length = 10
    while i < length:
        rand_numb = int(random.randint(0,10))
        m.append(rand_numb)
        i += 1
        if len(m) == length:
            print(f'list {m} max: {max(m)}')

    print('tack2')
    m1, m2, gen_m = [], [], []
    i = 0
    length = 10
    while i < length:
        rand_numb, rand_numb1 = int(random.randint(0, 10)), int(random.randint(0, 10))
        m1.append(rand_numb)
        m2.append(rand_numb1)
        i += 1
    print(m1)
    print(m2)
    i = 0
    while i < len(m2):
        j = 0
        while j < len(m2):
            if m1[i] == m2[j]:
                gen_m.append(m1[i])
            j += 1
        i += 1
    print('Untreated list:', gen_m)
    #print('Processed list: ', list(set(gen_m)))
    #
    len_gen = len(gen_m)
    i = 0
    j = 1
    while i < len_gen:
        j = i+1
        while True:
            if j <= len_gen-1:
                if gen_m[i] == gen_m[j]:
                    del gen_m[j]
                    len_gen = len(gen_m)
                    continue
                j += 1
            else: break
        i += 1
    print('Processed list: ', gen_m)

    print('tack3:')
    my_list = []
    my_list1 = []
    size = 100
    i = 0
    number = 1
    while i < size:
        if number % 7 == 0 and number % 5 != 0:
            my_list1.append(number)
        my_list.append(number)
        number += 1
        i += 1
    print(f'number % 7 == 0 and number % 5 != 0 :\n{my_list1}')
