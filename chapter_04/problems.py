# 1. Bug Collector
'''A bug collector collects bugs every day for five days. Write a program that keeps a running total  of  the  number  of  bugs  collected  during  the  five  days.  The  loop  should  ask  for  the  number of bugs collected for each day, and when the loop is finished, the program should display the total number of bugs collected'''

bugs_list = []
days = 5

for day in range(1, days + 1):
    user_input = int(input(f"Enter the total number of bugs collected in Day {day}: "))
    bugs_list.append(user_input)

print(f"List of bugs collected: {bugs_list}")
print(f"Total number of bugs collected in {day} days: {sum(bugs_list)}")

