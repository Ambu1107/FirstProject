def cal(marks,courses):
    if any (mark<40 for mark in marks):
        return "Fail"
    total=sum(marks)
    agg=(total/(courses*100)*100)
    if (agg>75):
        grade="Distinction"
    elif (agg>=60):
        grade="First Division"
    elif (agg>=50):
        grade="Second Division"
    elif (agg>=40):
        grade="Third Division"
    return (agg,grade)
courses= int(input("Enter number of courses: "))
marks=list(map(int,input("Enter marks: ").split()))
result=cal(marks,courses)
if (result=="Fail"):
    print("Fail")
else:
    agg,grade=result
    print(f"Aggregate Percentage:{agg:.2f}")
    print(f"Grade:{grade}")

