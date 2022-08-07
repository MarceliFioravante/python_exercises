'''Sum of Integers in String
Given a sentence or cluster of words, find out if there are any integers inside the string.
Print out the total number of integers. If there’s at least 1 integer present, find the
sum of all of the integers found and print out the sum.
For example:
If string = “200 plus 500 is equal to”
2 integers found
sum: 700'''
string = str(input('Escreva a somatória que deseja fazer: '))
pieces = string.split()
sum = 0
tot = 0
for i in range(len(pieces)):
    if pieces[i].isnumeric():
        pieces[i] = int(pieces[i])
        tot += 1
        sum += pieces[i]
print(f'{tot} integers found.')
print(f'sum = {sum}.')



