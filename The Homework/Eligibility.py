A = int(input("Enter your total marks obtained: "))

if A>49:
    if A>101:
      print("Unacceptable due to the marks reaching higher than the maximum limit")
      
if A>49:
  if 101>A:
    print("You passed, you lost", 100-A,"marks")

else:
    print("Unfortunately, you did not pass the exam", A, "< 50")