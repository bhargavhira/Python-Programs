import random 

def calculate_percentage(count,number):
    return count/(float(number))*100

num = int(input("Enter number of times the coin should be tossed "))

head_count = 0
tail_count = 0

if num>0:

    for i in range (0,num):

        value = random.random()

        if value>0.5:
            h_count += 1
        else:
            t_count += 1

print(f"Percentage of Heads = {calculate_percentage(head_count,num)}%")
print(f"Percentage of tails = {calculate_percentage(tail_count,num)}%")