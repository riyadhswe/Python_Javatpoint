marks = int(input("Enter the marks:"))
if(marks>=90):
    print("Excellent")
elif(marks<90 and marks>=75):
    print("Very Good")
elif(marks<75 and marks>=60):
    print("Good")
else:
    print("Average")