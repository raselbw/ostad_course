
score = input("Enter your score: ")
score = int(score)
if score in range(90, 101):
    print("You got an A")
elif score in range(80, 90):
    print("You got a B")
elif score in range(70, 80):
    print("You got a C")
elif score in range(60, 70):
    print("You got a D")
elif score in range(50, 60):
    print("You got an E")
elif score in range(40, 50):
    print("You got an E-")
else:
    print("You got an F")
    
