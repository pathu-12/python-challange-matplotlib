import matplotlib.pyplot as plt
import time as t
times=[]
mistakes=0
print("Here is the test to check how you can type")
print("write the word dog 5 times")  # giving a word to user
input("press enter to continue")

while len(times)<5:
    start=t.time()
    word=input("type the word :")
    end=t.time()
    time_ellapsed=start-end
    times.append(time_ellapsed)

    if word.lower()!="dog":
        mistakes+=1


print("your mistakes are",mistakes)
print("lets see your evolution")
t.sleep(3)
x=[1,2,3,4,5]
y=times
legend=["1","2","3","4","5"]
plt.xticks(x,legend)
plt.xlabel("number of attempts")
plt.ylabel("number of seconds")
plt.title("your progress")
plt.plot(x,y)
plt.show()