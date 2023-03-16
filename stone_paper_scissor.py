import random

def gameWin(comp,you):
    if comp==you:
        return None
    elif comp=='s':
        if you=='w':
            return False
        elif you=='g':
            return True
    elif comp=='w':
        if you=='g':
            return False
        elif you=='s':
            return True
    elif comp=='g':
        if you=='s':
            return False
        elif you=='w':
            return True

print("Comp turn: stone(s) scissor(w) or paper(g)")
      
randNO=random.randint(1,3)
if randNO==1:
    comp='s'
elif randNO==2:
    comp='w'
elif randNO==3:
    comp='g'


you=input("your turn: stone(s) scissor(w) or paper(g)?, please select:")
a=gameWin(comp,you)
print(f"computer choose {comp}")
print(f"You Choose {you}")

if a==None:
    print("The game is Tie!!")
elif a:
    print("You Win!!")
else:
    print("You Lose!!")