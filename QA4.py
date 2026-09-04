years = int(input("Enter Years of Service: ")) 
rating = input("Enter Performance Rating 
(Good/Poor): ") 
attendance = int(input("Enter Attendance (%): ")) 
 
if years >= 5 and rating == "Good" and 
attendance >= 90: 
    print("Bonus Eligible") 
else: 
    print("Not Eligible")