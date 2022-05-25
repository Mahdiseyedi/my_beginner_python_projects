import random

target_number = random.randint(1, 101)

def compare_answer(num_1, num_2):
    if num_1 > num_2:
        return "too high !"
    elif num_2 > num_1:
        return "too low !"
    else:
        return "Well done u did it !!!"

flag=True
i=0

game_mode=input("pick easy or hard mode :\n")

if game_mode=="easy":
    for i in range(10) :
        user_guess = int(input("guess your number:\n"))
        print(compare_answer(user_guess, target_number))
        i+=1
        if user_guess==target_number:
            break 
        
elif game_mode=="hard":
    for i in range(5) :
        user_guess = int(input("guess your number:\n"))
        print(compare_answer(user_guess, target_number))
        i+=1
        if user_guess==target_number:
            break
        
if user_guess!=target_number: 
    print("you lose baby!")   
print(f"correct answer was {target_number }")