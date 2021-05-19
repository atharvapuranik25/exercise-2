def arithmetic():
    """
    Input:      x, a positive int, no. of apples purchased
                y, a positive float, cost of 1 apple
                z, a positive int, no. of people splitting bill
    Returns:    x*y, total amount to be paid
                (x*y)/z, amount each person needs to pay
    """
    x = int(input("How many apples did you purchase (input integer):"))

    y = float(input("Cost of 1 apple (in Rupees):"))

    print("The amount to be paid to the shopkeeper is Rs.", x*y)

    z = int(input("The bill will be split among how many people (enter only if 2 or above):"))

    print("Each person has to pay Rs.", (x*y)/z)

#calling the function
arithmetic()
