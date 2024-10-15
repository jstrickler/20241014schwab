person = "Bill", "Gates", "Microsoft", "1955-10-28",

x = 5  # int
y = 5, # tuple with 1 value
z = () # tuple with 0 values (ie, empty tuple)

print(f"{person[3] = }")
print(f"{person[-1] = }")
print(f"{person[0:2] = }")

# person[0], person[1], ...
first_name, last_name, product, dob = person   # unpack the tuple

