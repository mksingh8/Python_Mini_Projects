import random

pass_len = int(input("Enter length of password: "))
p = random.sample("abcdefghijklmnopqrstuvwxyz1234567890!@#$%ABCDEFGHIJKLMNOPQRSTUVWXYZ", pass_len)
password = "".join(p)
print(password)

