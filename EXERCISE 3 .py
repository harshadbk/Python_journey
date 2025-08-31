import time
timestrap = time.strftime('%H:%M:%S')
print(timestrap)
# thistime = int(time.strftime('%H'))
thistime = float(input("enter the time"))
print(thistime)
if(thistime>=4 and thistime<=12):
    print("good morning sir ")
elif(thistime>=12 and thistime<=18):
    print("good afternoon sir ")
else:
    print("good night sir ")