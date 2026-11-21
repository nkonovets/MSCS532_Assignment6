import csv
import os
import time



def time_recorder(select_algorithm, data, k):

    numbers = data.copy()                                #copy so the original data stays unosrted

    start = time.perf_counter()                          #record time using the difference between each timestamp
    result = select_algorithm(numbers, 0, len(numbers) - 1, k, )
    total_time = time.perf_counter() - start

    return result, total_time * 1000                             #seconds to milliseconds



def save_results(algorithm_name, select_algorithm, data, filename, k):

    result, ms = time_recorder(select_algorithm, data, k)             

    new_file = not os.path.exists("results.csv")         #check if results.csv already exists

    with open("results.csv", "a", newline="") as f:      #"a" adds a new row instead of overwriting

        writer = csv.writer(f)

        if new_file:
            writer.writerow(["algorithm", "file", "n", "k", "result", "time_ms"])

        writer.writerow([algorithm_name, filename, len(data), k, result, round(ms, 2)])

    print(f"{algorithm_name}  {filename}  n={len(data)}  {ms:.2f} ms")