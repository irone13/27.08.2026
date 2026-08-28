def apply_discount(price, percent = 10):
    new_price = float(price * (1 - percent /100))



    return new_price

print(apply_discount(200))
print(apply_discount(200, 25))
print(apply_discount(200, percent=50))
print(apply_discount(price=80, percent=5))