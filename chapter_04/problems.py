# 1. Bug Collector
'''A bug collector collects bugs every day for five days. Write a program that keeps a running total  of  the  number  of  bugs  collected  during  the  five  days.  The  loop  should  ask  for  the  number of bugs collected for each day, and when the loop is finished, the program should display the total number of bugs collected'''

bugs_list = []
days = 5

for day in range(1, days + 1):
    user_input = int(input(f"Enter the total number of bugs collected in Day {day}: "))
    bugs_list.append(user_input)

print(f"List of bugs collected: {bugs_list}")
print(f"Total number of bugs collected in {day} days: {sum(bugs_list)}")

#2. Calories Burned
'''Running on a particular treadmill you burn 4.2 calories per minute. Write a program that uses a loop to display the number of calories burned after 10, 15, 20, 25, and 30 minutes.'''

time_list = [10,15,20,25,30]
calories_burnt = []

calories_per_minute = 4.2

for cal in time_list:
    calories_burn_calculation = calories_per_minute*cal
    calories_burnt.append(calories_burn_calculation)

print(f"Calories burned: {calories_burnt}")

#3. Lap Times
'''Write a program that asks the user to enter the number of times that they have run around a racetrack, and then uses a loop to prompt them to enter the lap time for each of their laps. When the loop finishes, the program should display the time of their fastest lap, the time of their slowest lap, and their average lap time.'''

import numpy as np

number_of_laps = int(input("Enter the number of laps you've run around the racetrack: "))
lap_time_list = []

for i in range(number_of_laps):
    lap_time = float(input(f"Enter the lap time for lap {i+1}: "))
    lap_time_list.append(lap_time)

fastest_lap = min(lap_time_list)
slowest_lap = max(lap_time_list)
average_lap_time = np.mean(lap_time_list)

print(f"\nYour fastest lap time: {fastest_lap}\nYour slowest lap time: {slowest_lap}\nYour average lap time: {average_lap_time:.2f}")

#4. Distance Traveled
'''The distance a vehicle travels can be calculated as follows:distance 5 speed3 timeFor  example,  if  a  train  travels  40  miles  per  hour  for  three  hours,  the  distance  traveled  is  120 miles. Write a program that asks the user for the speed of a vehicle (in miles per hour) and the number of hours it has traveled. It should then use a loop to display the distance the vehicle has traveled for each hour of that time period. Here is an example of the desired output:What is the speed of the vehicle in mph? 40EnterHow many hours has it traveled?'''

speed_of_vehicle = int(input("Enter the speed of the vehicle: "))
number_of_hours = int(input("Enter the number of hours that the vehicle has travelled: "))

for i in range(number_of_hours):
    distance = speed_of_vehicle * (i+1)
    if i == 0:    
        print(f"Your vehicle travelled {distance} miles in {i+1} hour.")
    else:
        print(f"Your vehicle travelled {distance} miles in {i+1} hours.")

#5. Sleep Debt
'''A  “sleep  debt”  represents  the  difference  between  a  person’s  desirable  and  actual  amount  of sleep. Write a program that prompts the user to enter how many hours they slept each day over a period of seven days. Using 8 hours per day as the desirable amount of sleep, determine their sleep debt by calculating the total hours of sleep they got over the seven-day period and subtracting that from the total hours of sleep they should have got. If the user does not have a sleep debt, display a message expressing your jealousy.'''

days = 7
desirable_hours_of_sleep_per_day= 8
total_desirable_hours_of_sleep = desirable_hours_of_sleep_per_day * days
sleep_hour_list = []

for day in range(1, days + 1):
    sleep_hour = int(input(f"Enter the number of hours you slept in Day {day}: "))
    sleep_hour_list.append(sleep_hour)

total_sleep_hour = sum(sleep_hour_list)
print(f"Total time you've slept in {days} days: {total_sleep_hour} hours")

if total_desirable_hours_of_sleep > total_sleep_hour:
    sleep_debt = (total_desirable_hours_of_sleep - total_sleep_hour)
    print(f"Your sleep debt: {sleep_debt} hours")

elif total_desirable_hours_of_sleep < total_sleep_hour:
    jealousy_debt = (total_sleep_hour - total_desirable_hours_of_sleep)
    print(f"I'm jealous that you got to sleep for extra {jealousy_debt} hours.")

elif total_desirable_hours_of_sleep == total_sleep_hour:
    print(f"You have a healthy sleeping habit.")

#6. Write a program that uses nested loops to draw this pattern:
'''
*******
******
*****
****
***
**
*
'''

for i in range(7, 0, -1):
    for j in range(i):
        print('*', end='')
    print()

#7. Pennies for Pay
'''Write a program that calculates the amount of money a person would earn over a period of time if his or her salary is one penny the first day, two pennies the second day, and contin-ues to double each day. The program should ask the user for the number of days. Display a table showing what the salary was for each day, then show the total pay at the end of the period. The output should be displayed in a dollar amount, not the number of pennies.'''

number_of_days = int(input("Enter the number of days: "))
print(f"Day\tSalary")
print("---------------")

total_pay = []
for i in range(1, number_of_days + 1):
    pay = 2 ** (i - 1)
    print(f"{i}\t${pay / 100:,.2f}")
    total_pay.append(pay)

grand_total = sum(total_pay) / 100

print("---------------")
print(f"Your total pay at the end of {number_of_days} days is ${grand_total:,.2f}")




