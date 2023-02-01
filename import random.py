import random
import threading

done = False
print('if the number does not divide it will go forever, have fun!')
divided = float(input('the number to be divided '))
divisor = float(input('the number that divideds '))
counter1 = int(1)
counter2 = int(0)
precision = 100000
answer = 0
attempts = 0

def getRandomNum():
     x = random.randint(precision, int(divided*precision))/precision
     return x

def randCalc(divided, divisor, precision):
    global done, answer, attempts, counter1, counter2
    while done == False:
        x = getRandomNum()
        if round((float(divided) / x), 5) == round(float(divisor),5):
            if round((float(divisor) * x), 5) == round(float(divided),5):
                done = True
                answer = x
                attempts = (counter2*precision) + int(counter1)
            else:
                done = True
                print("python bad")
        else:
            if counter1 == precision:
                counter2 += 1
                counter1 = 1
            else:
                counter1 += 1

threads = []
for i in range(40): # create threads
    t = threading.Thread(target=randCalc, args=(divided, divisor, precision))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("the answer is " + str(answer))
print("the total amount of attempt is " + str(attempts))
