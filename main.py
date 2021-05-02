import time
import ray
from matplotlib import pyplot as plt

@ray.remote
def stress_function(num):
    return sum([i*j*k for i in range(num) for j in range(i) for k in range(j)])

if __name__ == "__main__":
    ray.init(redis_address = "auto")
    inp = int(input("Enter a number: "))
    czas = []

    for i in range(inp):
        start = time.time()
        futures = [stress_function.remote(i) for i in range(inp)]
        x = ray.get(futures)
        czas.append(time.time() - start)

    dev_x = [i for i in range(inp)]
    dev_y = [czas[i] for i in range(inp)]

    plt.xlabel("Number of iterations")
    plt.ylabel("Time in seconds")
    plt.title("Time of compilation by number of iterations")

    plt.plot(dev_x, dev_y)

    plt.legend(["Stress Function"])

    plt.show()

