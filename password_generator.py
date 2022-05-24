import random

lett_list=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
num_list=['0','1','2','3','4','5','6','7','8','9']
symb_list=['!','@','#','$','%','^','&','*','(',')','+']

print("Welcome to the password generator by me :)")

pas_lett=int(input("How many letters do you want in your password?"))
pas_symb=int(input("How many symbols do you want in your password?"))
pas_num=int(input("How many numbers do you want in your password?"))

final_password_list=[]
while len(final_password_list)!=pas_lett:
    final_password_list.append(random.choice(lett_list))
while (len(final_password_list)-pas_lett)!=pas_symb:
    final_password_list.append(random.choice(symb_list)) 
while (len(final_password_list)-pas_lett-pas_symb)!=pas_num:
    final_password_list.append(random.choice(num_list))   

random.shuffle(final_password_list)

for item in final_password_list:
    print(item , end='')