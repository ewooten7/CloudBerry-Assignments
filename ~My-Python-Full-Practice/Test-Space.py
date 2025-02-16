#10. Truthy & Falsy Values: Predict the output:
values = [0, 1, "", "Hello", [], [1,2,3], None]
for v in values:
    if v:
        print(f"{v} is Truthy")
    else:
        print(f"{v} is Falsy")
#Response:
'Iteration 1: v = 0'
if 0:   # 0 is falsy
    print("0 is Truthy")  
else:
    print("0 is Falsy")

' Iteration 2: v = 1'
if 1:   # 1 is truthy
    print("1 is Truthy")

'Iteration 3: v = "" (Empty String)'
if "":   # Empty string is falsy
    print('"" is Truthy')  
else:
    print('"" is Falsy')

'Iteration 4: v = "Hello" (Non-empty String)'
if "Hello":  # Non-empty strings are truthy
    print("Hello is Truthy")

'Iteration 5: v = [] (Empty List)'
if []:   # Empty list is falsy
    print("[] is Truthy")  
else:
    print("[] is Falsy")

'Iteration 6: v = [1,2,3] (Non-empty List)'
if [1,2,3]:   # Non-empty lists are truthy
    print("[1,2,3] is Truthy")

'Iteration 7: v = None'
if None:   # None is falsy
    print("None is Truthy")  
else:
    print("None is Falsy")