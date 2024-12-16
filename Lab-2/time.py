import time

start = time.time()
time.sleep(2)
end = time.time()
if (end - start > 2):
    print(end-start)