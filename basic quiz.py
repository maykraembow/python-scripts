# Mayk Rambeau
# using Pycharm - Python 3.5.2
countit = 0;
totalNum = 6; # hard code here

print("Six questions game on Capitals in the USA" + '\n')
ques1 = input("What is the Capital of Oregon? " +'\n')
if ques1.lower() == "salem":
    print("correct" + '\n')
    countit += 1
else:
    print("Wrong answer" + '\n')
ques2 = input("What is the Capital of California? " + '\n')
if ques2.lower() == "sacramento":
    print("correct"+ '\n')
    countit += 1
else:
    print("Wrong answer"+ '\n')
ques3 = input("What is the Capital of Montana?"+ '\n')
if ques3.lower() == "helena":
    print("correct"+ '\n')
    countit += 1
else:
    print("Wrong answer"+ '\n')
ques4 = input("What is the Capital of New York"+ '\n')
if ques4.lower() == "albany":
    print("correct"+ '\n')
    countit += 1
else:
    print("Wrong answer"+ '\n')
ques5 = input("What is the Capital of Arizona?"+ '\n')
if ques5.lower() == "phoenix":
    print("correct"+ '\n')
    countit += 1
else:
    print("Wrong answer"+ '\n')
ques6 = input("What is the Capital of New Mexico"+ '\n')
if ques6.lower() == "santa fe":
    print("correct"+ '\n')
    countit += 1
else:
    print("Wrong answer"+ '\n')

print("you got {} out of {}".format(countit, totalNum)) #no hard coding here
