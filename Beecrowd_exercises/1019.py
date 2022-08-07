'''Read an integer value, which is the duration in seconds of a certain event in a factory,
and inform it expressed in hours:minutes:seconds.
Input
The input file contains an integer N.
Output
Print the read time in the input file (seconds) converted in hours:minutes:seconds like the following example.'''
N = int(input())
h = N / 3600
min = (N%3600) / 60
seg = N%60
if seg == 1:
    h = 0
    min = 0
print(f'{int(h)}:{int(min)}:{int(seg)}')
