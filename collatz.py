#Collatz's hypothesis

c0 = int(input("enter number: "))
steps = 0

def oddeven(number):
    if number % 2 == 0:
      return "Even"
         
    else:
     return "Odd"

while c0 != 1:    
    if oddeven(c0) == "Even":
            c0 = int(c0 / 2)
            print(c0)
            steps = steps + 1
    else:
            c0 = int(3 * c0 + 1)
            print(c0)
            steps = steps + 1
        
if c0 == 1:
    print("steps: ", steps)
    
