import random
user_choice=int(input("Enter your chioce either rock 'r',paper 'p',scissor 's' to check:\n"))
computer_choice=random.randint(0,2)
print(f"Computer chose {computer_choice}")

if user_choice==0 and computer_choice==2:
   print("You Win!")
elif computer_choice>user_choice:
   print("You lose!")
elif computer_choice==user_choice:
   print("It's draw")
else:
   print("You types an invalid number,you lose!")

