#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")
bill=(float(input("What was the total bill amount? $")))
n=int(input("How many people to spilt the bill with?\n"))
tip=int(input("What % of tip would you like to give? 10, 12 or 15?\n"))
cost_p_person= (bill/n)*(1+tip/100)
cost= round(cost_p_person,2)
print(f"Each person should pay: ${cost}")