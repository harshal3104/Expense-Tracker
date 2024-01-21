 expenses=[]
    with open(expense_file_path,"r") as f:
        lines=f.readlines()
        for line in lines:
            expense_name,expense_amount,expense_category=line.strip().split(",")
            line_expense=Expense(
                name=expense_name, amount=expense_amount, category=expense_category 
            )
            print(line_expense)
            expenses.append(line_expense)
    print(expenses)