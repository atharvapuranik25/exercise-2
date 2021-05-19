def conversion():
    """
    Input:      c, temperature in celsius
    Returns:    f, temperature in fahrenheit
    """
    c = float(input("Temperature Value in degree Celsius:"))

    f = (c * 1.8) + 32
    #converting celsius value to fahrenheit
    f = str(f)
    #casting float "f" to string
    print("Temperature in Fahrenheit will be", f + " degrees.")

#calling the function
conversion()
