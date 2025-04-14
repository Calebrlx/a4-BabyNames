#########################################
# caleb forestal
# assignment 4
# april 14 2025
#
# guess which name is more popular
#########################################

import random

class nameobj:
    """stores rank, name, and number of births"""
    count = 0

    def __init__(self, r, n, b):
        """init w/ rank (int), name (str), births (int)"""
        self.rank = int(r)
        self.name = n
        self.births = int(b)
        nameobj.count += 1

    def __gt__(self, other):
        """returns true if this name is more popular"""
        return self.births > other.births

    def __lt__(self, other):
        """returns true if this name is less popular"""
        return self.births < other.births

def load_names(file):
    """
    reads names from txt file
    input: file name (str)
    output: list of nameobj
    """
    lst = []
    try:
        with open(file, 'r') as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) == 3:
                    lst.append(nameobj(parts[0], parts[1], parts[2]))
    except:
        print('something went wrong with the file')
    return lst

def ask(q1, q2):
    """
    asks user to choose which name is more popular
    input: two nameobj instances
    output: bool, True if guess is correct
    """
    print(f'in 2015, was the name {q1.name} (1) or {q2.name} (2) more popular (enter 1 or 2)? ', end='')
    ans = input().strip()
    while ans not in ['1', '2']:
        print(f'in 2015, was the name {q1.name} (1) or {q2.name} (2) more popular (enter 1 or 2)? ', end='')
        ans = input().strip()
    guess = q1 if ans == '1' else q2
    right = q1 if q1 > q2 else q2
    if guess == right:
        print('correct!')
    else:
        print('nope.')
    print(f'there were {q1.births} people named {q1.name}, and {q2.births} named {q2.name}')
    return guess == right

# main
boys = load_names('boynames2015.txt')
print('after reading boynames, the total number of class objects =', nameobj.count)
girls = load_names('girlnames2015.txt')
print('after reading girlnames, the total number of class objects =', nameobj.count)

total = 0
correct = 0
play = 'y'
while play.lower() == 'y':
    b = random.choice(boys)
    g = random.choice(girls)
    if ask(g, b):  # mix up order sometimes
        correct += 1
    total += 1
    print('do you want to play again y/n? ', end='')
    play = input().strip().lower()
    while play not in ['y', 'n']:
        print('you must enter y or n ...')
        print('do you want to play again y/n? ', end='')
        play = input().strip().lower()

print('thanks for playing!')
if total > 0:
    print(f'you answered {round(correct/total*100,1)}% correct')
else:
    print("you didn’t even try bro")