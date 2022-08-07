'''FizzBuzz
Cycle through every number from 1 to some number that the user provides as input.
 (only integers) and print each one onscreen. If the number is divisible by 4, then
  instead of printing the number itself, print “Fizz”. If the number is divisible by 6,
  then instead of printing the number itself, print “Buzz”. If the number is divisible by both 4 and 6,
  print “FizzBuzz”. If the number doesn’t satisfy any of these conditions, simply print the number itself.
For example:
If max = 13
The range would be 1 to 13'''
max = int(input('If max = '))
for i in range(1, max+1):
    if (i) % 4 == 0 and (i) % 6 == 0:
        print('FizzBuzz')
    elif (i) % 4 == 0:
        print('Fizz')
    elif (i) % 6 == 0:
        print('Buzz')
    else:
        print(i)