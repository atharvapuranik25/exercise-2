def factor():
    """
    Input:      temp, temperature of the wind in fahrenheit
                vel, wind speed in miles per hour
    Returns:    wind_chill, wind chill factor in fahrenheit
    """
    temp = float(input("Temperature of the Wind (in degree fahrenheit):"))

    vel = float(input("Wind Speed (in miles per hour):"))

    wind_chill = 35.74 + (0.6215 * temp) - (35.75 * (vel**0.16)) + ((0.4275 * temp) * (vel**0.16))

    wind_chill = str(wind_chill)
    #casting float "wind_chill" to string

    print("The wind chill is ", wind_chill + " degree F.")

#calling the function
factor()
