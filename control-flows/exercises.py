name: str = 'Gorka'

# 1) Call `print` with a different string using a single conditional expression
print(f'{name} is longer than the avg name in the US') if len(name) >= 6 \
    else print(f'{name} is shorter than the avg name in the US')

# 2) Set `message` using a single conditional expression
message = f'The first letter in {name} is among the five most common' \
    if name.lower() in ["a", "j", "m", "e", "l"] \
    else f'The first letter of {name} is not among the five most common'

print(message)

# 3) Change the string passed to the `print` function using a conditional expression
for letter in name:
    print(f'{letter} is a vowel') if letter.lower() in ["a", "e", "i", "o", "u"] \
        else print(f'{letter} is a consonant')
