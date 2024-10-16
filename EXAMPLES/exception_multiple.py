
try:
    x = 5
    y = "cheese"
#    z = x + y
    f = open("sesame.txt")
    print("Bottom of try")

except (IOError, TypeError) as err:  # Use a tuple of 2 or more exception types
    print(type(err))
    print("Naughty programmer! ", err)
