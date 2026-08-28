def count_vowels(text):
    count = 0
    vowels = ('a', 'e', 'i', 'o', 'u')
    for letter in text:
        for letters in vowels:

            if letter == letters:
                count +=1
    return count

print(count_vowels('incognito'))
print(count_vowels('missiiiissippi'))
print(count_vowels('xyz'))
