#def functionTest(x):
    #print('Hello', x)


#def main():
    #var = input("Enter a name\n")
    #functionTest(var)

#if __name__ == '__main__':  # de aflat dece folosim si conditia data
    #main()



#def calc(a, b):
    #print(a + b) # hello + name = helloname
    #print(a - b)
    #print(a * b) # hello * 2 = hellohello
    #print(a / b)

#a = int(input('Enter first number...\n'))
#b = int(input('Enter second number...\n'))

#calc(a, b)

#def calc(*args):
    #print(*args[0] + *args[1])
    #print(*args[0] - *args[1])
    #print(*args[0] * *args[1])
    #print(*args[0] / *args[1])

#a = 2
#b = 3


#def to_uppercase(word):
    #return word.upper()  # recieve result


#def to_uppercase(word):
    #print(word.upper())  # display result

#to_uppercase('hello')
#print(to_upper('hello'))


#for i in range(3, 4):
    #if i == 4:
        #print("done")
        #continue # continua
        #break # opreste


#def will_be_used_in_future():
    #pass # trece peste fara erori


pers_name = input("Set the name ")
pers_hp = 100
max_pers_hp = 100
armor = 50
nr_hits = 1


def attack(pers_hp, dmg=10):
    global armor, nr_hits

    if armor - dmg > 0:
        armor = armor - dmg
    else:
        pers_hp = pers_hp - dmg
    return pers_hp


def heal(pers_hp, live):
    global max_pers_hp

    if pers_hp + live > max_pers_hp:
        pers_hp = max_pers_hp
    else:
        pers_hp = pers_hp + live

    return pers_hp


pers_hp = attack(pers_hp, 40)
print(pers_hp)

pers_hp = heal(pers_hp, 20)
print(pers_hp)

# Make a battle
for i in range(1, 100):

    if pers_hp > 0:
        pers_hp = attack(pers_hp)
    else:
        break

    print("Live ", pers_hp)
    print("Armor", armor)
    print("Hit nr ", i)

print("You are dead")

# Bonus
for i in range(1, 100):

    if pers_hp > 0:
        nr_hits = nr_hits + 1

        if nr_hits % 3 == 0:
            pass
        else:
            pers_hp = attack(pers_hp)
        print("----" + pers_name + "---")
        print("Live ", pers_hp)
        print("Armor", armor)
        print("Hit nr ", nr_hits)

    else:
        break

print("You are dead")
