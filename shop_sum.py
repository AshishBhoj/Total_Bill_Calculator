sum = 0
while True:
    number = input("Enter the item price or press q to quit : ")
    if number != 'q':
        sum += int(number)
        print(f"Order total so far {sum}")
    else:
        print(f"Your bill total is {sum}")
        print("Thanks for shopping")
        break