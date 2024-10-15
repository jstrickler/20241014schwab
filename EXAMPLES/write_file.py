
states = [
    'Virginia',
    'North Carolina',
    'Washington',
    'New York',
    'Florida',
    'Ohio',
]

with open("states.txt", "w") as states_out: # "w" opens for writing, "a" for append
    for state in states:
        states_out.write(state + "\n")  # write() does not automatically add newline
    # states_out.writelines(states)
nums = [800, 80, 1000, 32, -3, 8, 18, 255, 400, 5, 5000]

with open("numbers.txt", "w") as nums_out:
    for number in nums:
        nums_out.write(f"{number}\n")
