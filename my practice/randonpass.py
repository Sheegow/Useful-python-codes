import random
pass_len = int(input("enter the lenght of the password: "))

s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

P = "".join(random.sample(s,pass_len))
print(P)