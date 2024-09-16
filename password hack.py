from random import *
import os

os.system("color a")
u_pwd=input("Enter Password: ")
pwd_alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
pwd_num=['1','2','3','4','5','6','7','8','9','0']
#pwd=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0']
pw=""
while(pw!=u_pwd):
    pw=""
    for letter in range(0,len(u_pwd)):
        if u_pwd[-(letter+1)] not in pwd_num and u_pwd[-(letter+1)] not in pwd_alpha :
            print("Invalid Password Format")
            u_pwd=input("Enter Password:")
        elif u_pwd[-(letter+1)] not in pwd_alpha:
            guess_pwd =pwd_num[randint(0,9)]
            pw=str(guess_pwd)+str(pw)
            print("Cracking Password...please wait")
            print(str(pw))
            u_pwd=str(u_pwd)
            os.system("cls")
            
        elif u_pwd[-(letter+1)] not in pwd_num:
            guess_pwd =pwd_alpha[randint(0,25)]
            pw=str(guess_pwd)+str(pw)
            print("Cracking Password...please wait")
            print(str(pw))
            u_pwd=str(u_pwd)
            os.system("cls")
       
        

print("Your password:",pw)
os.system('pause')

'''
 else:
            guess_pwd =pwd[randint(0,35)]
            pw=str(guess_pwd)+str(pw)
            print("Cracking Password...please wait")
            print(str(pw))
            u_pwd=str(u_pwd)
            os.system("cls")

'''
