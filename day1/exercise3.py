# excercise_3.py

while(True):
    user_input = int(input("enter any number from 1-12:"))
    if user_input > 12 or user_input<1:
        user_input = input("enter any number from 1-12:")
    else:
        for i in range(1,11):
            print(f"{i} * {user_input} = {i*user_input}\n")
    