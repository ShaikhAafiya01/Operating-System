print("S128 Aafiya Shaikh")

import threading
import time

BUFFER_SIZE = 5
ITEMS = 10

buffer = [None] * BUFFER_SIZE
in_index = 0
out_index = 0

empty = threading.Semaphore(BUFFER_SIZE)
full = threading.Semaphore(0)
mutex = threading.Lock()


def producer():
    global in_index

    for item in range(1, ITEMS + 1):
        empty.acquire()

        with mutex:
            buffer[in_index] = item
            print("Produced:", item)
            in_index = (in_index + 1) % BUFFER_SIZE

        full.release()
        time.sleep(1)


def consumer():
    global out_index

    for _ in range(ITEMS):
        full.acquire()

        with mutex:
            item = buffer[out_index]
            print("Consumed:", item)
            out_index = (out_index + 1) % BUFFER_SIZE

        empty.release()
        time.sleep(2)


producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()
