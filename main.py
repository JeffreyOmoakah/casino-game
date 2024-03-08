
def deposit():
    while True:
        amount = input("Enter the amount you want to deposit?: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount should be greater than zero")
        else: 
                print("Enter a Number")

    return amount


