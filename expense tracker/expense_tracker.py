from expense import Expense

def main():
    print(lavender(f"Expense Tracker"))
    expense_file_path="expense.csv"
    
    budget=int(input("Enter Your Budget"))
    
    #get user expense input
    expense=get_user_expense()
    
    #write that expense to csv file
    save_expense_to_file(expense,expense_file_path)
    
    #read file and summarize expense
    summarize_expense(expense_file_path, budget)
    

def get_user_expense():
    expense_name=input("enter expense name:")
    expense_amount=float(input("enter your expense amount(in rupees):"))
    # print(f"your entry is {expense_name}, {expense_amount}")
    
    expense_categories=[
        "WORK",
        "TRAVEL",
        "HOME",
        "FOOD",
        "COSMETICS", 
        "GAMES",
        "OTHER"
              
    ]
    
    while True:
        print("select any category: ")
        for i,category_name in enumerate(expense_categories):
            print(f"{i+1}.{category_name}")
            
        value_range=f"[1-{len(expense_categories)}]"
        selected_index=int(input(f"enter any category between {value_range}: "))-1
        
        if i in range(len(expense_categories)):
            selected_category=expense_categories[selected_index]
            new_expense=Expense(
                name=expense_name, category=selected_category, amount=expense_amount
            )
            return new_expense
        else:
            print("Invalid catergory!!! Please choose again!")
            

def save_expense_to_file(expense, expense_file_path):
    print(f"user expense saved: {expense} to {expense_file_path}")
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")

def summarize_expense(expense_file_path, budget):
    print("Summarizing Expenses")
    expenses=[]
    with open(expense_file_path,"r") as f:
        lines=f.readlines()
        for line in lines:
            expense_name,expense_amount,expense_category=line.strip().split(",")
            line_expense=Expense(
                name=expense_name, amount=float(expense_amount), category=expense_category 
            )
            # print(line_expense)
            expenses.append(line_expense)
    # print(expenses)
    
    amount_by_category={}
    for expense in expenses:
        key=expense.category
        if key in amount_by_category:
            amount_by_category[key]+=expense.amount
        else:
            amount_by_category[key]=expense.amount
    
    print(cyan("Expenses by category"))
    for key,amount in amount_by_category.items():
        print(f"  {key}:{amount:.2f}")
        
#  total spent
    total_spent=sum([exp.amount for exp in expenses])
    print(green(f" Total Spent: {total_spent:.2f}"))
    
# get remaining budget
    budget_remaining=budget-total_spent
    print(red(f" Budget Remaining: {budget_remaining:.2f}")) 

# color a text   
def green(text):
    return f"\033[92m{text}\033[0m"    

def red(text):
    return f"\033[91m{text}\033[0m"  

def lavender(text):
    return f"\033[95m\033[1m{text}\033[0m"

def cyan(text):
    return f"\033[96m{text}\033[0m"


if __name__=="__main__":
    main()