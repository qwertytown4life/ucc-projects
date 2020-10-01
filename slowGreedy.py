molla = int(input('Enter number of cents: '))
amounts = [200, 100, 25, 10, 5, 1]
pointer = 0
temp = 0
while molla >= 0 and pointer < len(amounts):
    if molla - amounts[pointer] >= 0:
        molla -= amounts[pointer]
        temp += 1
    else:
        print(f"{temp} x ${round(amounts[pointer]/100,2)}")
        temp = 0
        pointer += 1
