import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 10

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 6,
    "G": 4,
    "D": 8
}
def get_slot_machine_spin(rows,cols,symbols):
    all_symbols = []
    for symbols, symbol_count in symbols.items:
        for _ in range(symbol_count):
            all_symbols.append(symbols)

    columns = [[],[],[]]
    for _  in range (cols):
        columns = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols) 
            current_symbols.remove(value)
            column.append(value)

        columns.append(columns)

    return columns

def print_slot_machine(columns):
    for row in range(len(column[0])):
        for i, column in enumerate(columns):
            if i != len(column) - 1:
                print(column[row], "|")
            else:
                print(column[row])

    
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

def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES)+ ")?: ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter valid number of lines ")
        else: 
                print("Please enter a Number")
    return lines

def get_bet():
    while True:
        amount = input("What would you like to bet on each line: $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount should be between ${MIN_BET} - ${MAX_BET}")
        else: 
                print("Enter a Number")

    return amount

def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bets = lines * bet

        if total_bets >balance:
            print(f"You do not have enough to bet that amount, Your total balance is ${balance}")
        else:
            break
    print(f"You staked ${bet} on {lines} lines. Total bet is equals to: ${total_bets}")

main()