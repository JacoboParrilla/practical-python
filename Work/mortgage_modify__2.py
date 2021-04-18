# mortgage.py
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0
a = input("Do you want to make an extrapayment? :")
if a == "no":
    while principal > 0:
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment
    print('Total paid', total_paid)
elif a == "yes":
    b = int(input('At what month do you want to start an extra payment? :'))
    c = int(input('At what month do you want to end an extra payment? :'))
    d = int(input('how much money do you want to pay extra?: '))

while principal > 0:
    month = month +1 
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    if month >= b and month <= c:
        principal = principal - d
        total_paid = total_paid + d

print('Total paid', round(total_paid,2),'Months: ', round(month,2))
# Exercise 1.9
