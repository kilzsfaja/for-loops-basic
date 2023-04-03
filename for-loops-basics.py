# 1. basic - print all integers from 0 - 150

for i in range(151):
    print(i)

# 2. Multiples of Five - Print all the multiples of 5 from 5 to 1,000

for i in range(5, 1001, 5):
    print(i)

# 3. Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".

for i in range(1, 101):
    if i % 10 == 0: # / 10 must come first or else you get doubles
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

# 4. Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.

count = 0
for i in range(500001):
    if i % 2 == 1:
        count += i

print(f"The sum of all integers is {count}")

# 5. Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.

for i in range(2018, -1, -4):
    print(i)

# 6. Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)

low_num = 0
high_num = 37
mult = 6
count= []
for i in range(low_num, high_num, 1):
    if i % mult == 0:
        count.append(i)

print(count)