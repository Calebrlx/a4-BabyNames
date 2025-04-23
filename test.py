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
        return self.births > other.births

    def __lt__(self, other):
        return self.births < other.births

def load_names_from_data(data):
    """Takes raw multiline string data and returns a list of nameobj"""
    lst = []
    for line in data.strip().split('\n'):
        parts = line.strip().split()
        if len(parts) == 3:
            lst.append(nameobj(parts[0], parts[1], parts[2]))
    return lst

# Sample hardcoded data (top 10 names only for each gender)
boy_data = """
1 Noah 19511
2 Liam 18281
3 Mason 16535
4 Jacob 15816
5 William 15809
6 Ethan 14991
7 James 14705
8 Alexander 14460
9 Michael 14321
10 Benjamin 13608
"""

girl_data = """
1 Emma 20355
2 Olivia 19553
3 Sophia 17327
4 Ava 16286
5 Isabella 15504
6 Mia 14820
7 Abigail 12311
8 Emily 11727
9 Charlotte 11332
10 Harper 10241
"""

def ask(q1, q2):
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

# main logic
boys = load_names_from_data(boy_data)
print('after reading boynames, the total number of class objects =', nameobj.count)
girls = load_names_from_data(girl_data)
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