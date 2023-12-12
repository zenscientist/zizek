
# Online Python - IDE, Editor, Compiler, Interpreter
order = input('What is your order? ')
inventory = ['coffee', 'coffee without cream']
def dowehave(order):
    n=0
    for item in inventory:
        n = n+1
        if order == item:
            return ("Yes we have "+order)
        elif n == len(inventory):
            return("No we don't have "+order)
        
print(dowehave(order))




