'''Given an input by the user in the form of a positive integer,
the program should print out a triangle-shaped pattern made of
the star character (*). The input should be stored in a variable called N.
N represents the number of rows in the pattern. The number of stars in each row increases by 2 each time.'''
N = int(input('N: '))
x = 1
'''for i in range(0, N):
    for j in range(0, i+1):
       print(f"{carac:^5}", end= '')
    print('')'''
for i in range(N, 0, -1):
    spaces = i - 1
    caracteres = N - i + x
    print(' ' * spaces, '*' * caracteres)
    x = x + 1

