import pandas as pd
import matplotlib.pyplot as plt

expenses_list = []
amount_list = []
categories = {"Rent":0,"Food":0,"Groceries":0,"Entertainment":0,"Transport":0,"Other":0}
selected_category = []
all_expenses = {"Category":selected_category, "Expenses":expenses_list,"Amount":amount_list}

while True:
    print("1.Add expenses")
    print("2.View all expenses")
    print("3.Delete expense")
    print("4.Quit")
    answer = int(input("Press 1,2,3 or 4 to confirm your options: " ))
    if answer == 1 or answer == 2 or answer == 3 or answer == 4:
        if answer == 1:
            print(categories)
            category_select = input("Select the category of your expense: ")
            category_select = category_select.capitalize()
            if category_select in categories:
                selected_category.append(category_select)
                new_expense = input("Name your expense: ")
                expenses_list.append(new_expense)
                amount = int(input("Add the amount required for this transaction: "))
                amount_list.append(amount)
                categories[category_select] = categories[category_select] + amount
                print("Expense added.")
            else:
                print("Invalid category, try again")

        elif answer == 2:
            for i in range(len(expenses_list)):
                print(i+1,".",selected_category[i],"-",expenses_list[i],"-",amount_list[i])
        elif answer == 3:
            if len(expenses_list) == 0:
                print("Nothing to delete")
            else:
                print(all_expenses)
                selection = int(input("Enter the position number of the expense you want to drop: "))-1
                if 0<= selection <len(expenses_list):
                    cat_to_remove = selected_category.pop(selection)
                    expenses_list.pop(selection)
                    amt_to_remove = amount_list.pop(selection)
                    categories[cat_to_remove] = categories[cat_to_remove] - amt_to_remove
                else:
                    print("Invalid input")
        elif answer == 4:
            print("Quit successfully")
            break
                    
        else:
            print("Wrong input")
    else:
        print("Either press 1,2 or 3")

        
plt.bar(categories.keys(),categories.values())
plt.title("Amount of expenditure by category")
plt.xlabel("Category")
plt.ylabel("Amount")
plt.show()

