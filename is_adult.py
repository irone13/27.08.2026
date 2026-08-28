def is_adult (age = 0):
    if age > 18 :
        return True
    else:
        return False

print(is_adult())
print(is_adult(17))
print(is_adult(18))
print(is_adult(age=40))