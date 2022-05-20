# TODO

h = int(input())

while h!=-9999:
    w = int(input())
    bmi = w/((h/100)**2)
    
    print(f"BMI: {bmi:.2f}")
    
    if bmi<18.5:
        print("State: under weight")
    elif 18.5<=bmi<25:
        print("State: normal")
    elif 20.5<=bmi<30:
        print("State: over weight")
    else:
        print("State: fat")
    
    h = int(input())


"""
fat
over weight
normal
under weight
BMI: _
State: _
"""