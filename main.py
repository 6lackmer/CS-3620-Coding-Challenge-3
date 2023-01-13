# Part 1:
def student_discount(x):
    # Student discount always gets buyer discount. Calculate student discount then buyer discount off of that rate.
    return regular_buyer_discount(x * 0.9)

def regular_buyer_discount(x):
    return x * 0.95

print(student_discount(100))
print(regular_buyer_discount(100))


# Part 2:

# Part 3:

# Part 4:

# Part 5: