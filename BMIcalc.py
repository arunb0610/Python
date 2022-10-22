weight = int(input("Enter your weight : "))
height = float(input("Enter your height : "))

BMI = weight/float(height*height)

if BMI < 18.5 :
    print("Underweight")
    print("Tip : Need to gain some weight")

if BMI>=18.5 and BMI<25 :
    print("Normal")
    print("Nothing to worry")

if BMI >= 25 and x < 30 :
    print("Overweight")
    print("Tip : Need to workout")

if BMI >= 30:
    print("Obesity")
    print("Need to Lose more weight")
