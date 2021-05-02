import time
from matplotlib import pyplot as plt

def stress_function(num):
    return sum([i*j*k for i in range(num) for j in range(i) for k in range(j)])

inp = int(input("Enter a number: "))
czas = []

for i in range(inp):
    start = time.time()
    test = stress_function(i)
    czas.append(time.time() - start)


dev_x = [i for i in range(inp)]
dev_y = [czas[i] for i in range(inp)]

plt.xlabel("Number of iterations")
plt.ylabel("Time in seconds")
plt.title("Time of compilation by number of iterations")

plt.plot(dev_x, dev_y)

plt.legend(["Stress Function"])

plt.show(block=True)
