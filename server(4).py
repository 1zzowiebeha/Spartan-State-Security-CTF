import re

print("The alphabet doesn't belong in math! This is a calculator.")
def calculate(expression):
    print(eval(expression))

expression = input('>>> ').strip()

evil = re.search(r'[a-z]', expression)
if not evil:
    calculate(expression)
else:
    print("Letters don't belong in math! Get out of here!")
