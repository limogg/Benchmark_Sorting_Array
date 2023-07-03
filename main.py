import random
import time

def quicksort(array):
    if len(array) <= 1:
        return array

    pivot = array[random.randint(0, len(array) - 1)]
    smaller = [x for x in array if x < pivot]
    equal = [x for x in array if x == pivot]
    greater = [x for x in array if x > pivot]

    return quicksort(smaller) + equal + quicksort(greater)

# Generowanie losowej tablicy 100 000 000 liczb dziewięciocyfrowych
random.seed(42)
array = [random.randint(1000, 9999) for _ in range(10000000)]

# Sortowanie i mierzenie czasu
start_time = time.time()
sorted_array = quicksort(array)
end_time = time.time()
execution_time = end_time - start_time

print("Czas sortowania:", execution_time, "sekundy")
