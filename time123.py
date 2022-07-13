import time

initial = time.time()
k = 0
while(k<10):
    print("shreya")
    time.sleep(1)
    k+=1
print("while loop ran in", time.time() - initial, "Seconds")


initial2 = time.time()
for i in range(10):
    print("shreya")
print("for loop ran in", time.time() - initial2, "Seconds")

localtime = time.asctime(time.localtime(time.time()))
print(localtime)