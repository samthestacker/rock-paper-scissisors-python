import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_image=[rock,paper,scissors]
a=int(input('0 for rock,1 for paper,2 for scissors'))
if a>=0 and a<=2 :
    print(game_image[a])
else:
    print("chose correctly")
b=random.randint(0,2)

print(f"computer chose{b}")
print(game_image[b])
if a>=3 or a<0 :
    print('you choose wrong number')
elif a==0 and b==2 :
    print("you win")
elif b==0 and a==2:
    print("you loose")
elif b>a:
    print("you loose")
elif a>b:
    print("you winnn")
elif a==b:
    print("it's a draw!!")
