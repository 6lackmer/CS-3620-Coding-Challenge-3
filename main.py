# Part 1:
    # Assumption:
        # All students get 10% off
        # All students are regular buyers
        # Regular buyers all get 5% off
def student_discount(x):
    # Student discount always gets buyer discount. Calculate student discount then buyer discount off of that rate.
    return regular_buyer_discount(x * 0.9)

def regular_buyer_discount(x):
    return x * 0.95

print(student_discount(100))
print(regular_buyer_discount(100))

# Part 2:
result = (lambda x: x * (x+5) **2)(5)
print(result)

# Part 3:
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def discount_products_10_percent(x):
    return x * 0.9
result = list(map(discount_products_10_percent, my_list))
print(result)

# Part 4:

# Part 5: