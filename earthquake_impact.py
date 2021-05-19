def impact():
    """
    Input:      M, magnitude of an earthquake as measured on the richter scale
    Returns:    I, intensity of the earthquake
    """
    M = float(input("Magnitude as measured on Richter scale (between 0 to 10):"))

    # according to richter scale M=log(I/I0)
    I = 10 ** M

    print("The intensity of the earthquake is", I)

#calling the function
impact()
