print("Welcome to the office of Rachael Vex.")
print("Dr. Vex is not to be disturbed.")
print()
print("Please enter the computation you need executed.")
print()

def pass_to_grad_student(computation):
    print(eval(computation))

def shush(computation):
    for c in computation:
        if c in 'abcdefghijklmnopqrstuvwxyz' and c not in 'Rachael Vex'.lower():
            print('Shush!')
            exit()

computation = input("> ")

shush(computation)

pass_to_grad_student(computation)

print("Computation completed.")
