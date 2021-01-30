
import time

for1= time.time()
k=0
while k<45:
    print("Printing 45 in while loop")
    k+=1
print("The total time taken by while loop is: ",time.time()-for1," seconds")
for2= time.time()
for i in range(45):
    print("Printing 45 in for loop")
print("The total time taken by for loop is: ",time.time()-for2," seconds")
print("\n\n")
local_time= time.asctime(time.localtime(time.time())) #your current time
print(local_time)