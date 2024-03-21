#time taken to run a function
from timer import perf_counter
start_time=perf_counter()
for i in range(100):
    print(i)
end_time=perf_counter()
total_time=end_time-start_time
print(f"Total time for program execution:{total_time}")
