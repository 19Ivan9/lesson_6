import random

if __name__ == '__main__':
    print('tack1:')
    my_list = []
    size = 10
    i = 0
    while i < size:
        number = random.randint(1, 100)
        my_list.append(number)
        i += 1
    #max(my_list)
    #min(my_list)
    i = 0
    j = 0
    min = my_list[0]
    max = my_list[0]
    while i < size:
        if my_list[i] < min:
            min = my_list[i]
        elif my_list[i] > max:
            max = my_list[i]
        i += 1
    print(f'My list: {my_list}\nmin= {min}\nmax= {max}')

    print('tack2:')
    string = tuple(input('Enter the string: '))
    print(string[::2])

    print('tack3:')
    my_list = []
    exit = 'q'
    while True:
        name = input(f'Enter the names of player\nClick to finish {exit}')
        if name == exit:
            print('Exit')
            my_list.sort()
            break
        my_list.append(name)

    print(my_list)

    size_list = len(my_list)
    i = 0
    j = 1
    if size_list%2 != 0:
        x = int(size_list/2)
        print(my_list[x], 'Has no pair')
        del my_list[x]
        size_list = len(my_list)
    while i < size_list/2:
        print(f'{my_list[i]} vs {my_list[-j]}')
        i += 1
        j += 1

        print('tack4:')
        my_list = []
        size = 10
        i = 0
        while i < size:
            number = random.randint(1, 100)
            my_list.append(number)
            i += 1
        print('First list:',my_list)
        my_list1 = []
        i = 0
        j = 1
        while i < size and j <= size:
            my_list1.append(my_list[-j])
            i += 1
            j += 1
        print('Final list:',my_list1)