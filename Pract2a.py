from multiprocessing import Process, Queue
import time
import random

# Producer function
def producer(queue):
    """
    Produces 10 random numbers and puts them into the queue.
    The producer blocks if the queue is full.
    """
    for i in range(10):
        item = random.randint(1, 100)
        print(f"Producer produced: {item}")

        queue.put(item)  # Blocks if queue is full
        print(f"Item {item} added to queue")

        time.sleep(0.5)  # Producer speed


# Consumer function
def consumer(queue):
    """
    Consumes 10 items from the queue.
    The consumer blocks if the queue is empty.
    """
    for i in range(10):
        time.sleep(1.5)  # Consumer is slower

        item = queue.get()  # Blocks if queue is empty
        print(f"Consumer consumed: {item}")


if __name__ == "__main__":
    # Queue with maximum size of 3
    q = Queue(maxsize=3)

    # Create producer and consumer processes
    p1 = Process(target=producer, args=(q,))
    p2 = Process(target=consumer, args=(q,))

    # Start processes
    p1.start()
    p2.start()

    # Wait for both to finish
    p1.join()
    p2.join()

    print("Producer and Consumer have finished.")
