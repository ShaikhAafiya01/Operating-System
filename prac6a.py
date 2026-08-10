from collections import deque

processes = [
    ("P1", 0, 5),
    ("P2", 4, 2),
    ("P3", 5, 4)
]

quantum = 2


def round_robin(processes, quantum):
    processes = sorted(processes, key=lambda x: x[1])
    remaining = {p[0]: p[2] for p in processes}
    completion = {}
    queue = deque()

    time = 0
    index = 0

    while index < len(processes) or queue:
        while index < len(processes) and processes[index][1] <= time:
            queue.append(processes[index][0])
            index += 1

        if not queue:
            time = processes[index][1]
            continue

        pid = queue.popleft()
        execution = min(quantum, remaining[pid])
        time += execution
        remaining[pid] -= execution

        while index < len(processes) and processes[index][1] <= time:
            queue.append(processes[index][0])
            index += 1

        if remaining[pid] > 0:
            queue.append(pid)
        else:
            completion[pid] = time

    results = []

    for pid, arrival, burst in processes:
        turnaround = completion[pid] - arrival
        waiting = turnaround - burst

        results.append([
            pid,
            arrival,
            burst,
            completion[pid],
            turnaround,
            waiting
        ])

    return results


def fcfs(processes):
    processes = sorted(processes, key=lambda x: x[1])
    time = 0
    results = []

    for pid, arrival, burst in processes:
        if time < arrival:
            time = arrival

        time += burst
        completion = time
        turnaround = completion - arrival
        waiting = turnaround - burst

        results.append([
            pid,
            arrival,
            burst,
            completion,
            turnaround,
            waiting
        ])

    return results


def display_table(title, results):
    print("\n" + title)
    print("-" * 75)
    print(
        f"{'Process':<10}"
        f"{'Arrival':<10}"
        f"{'Burst':<10}"
        f"{'Completion':<15}"
        f"{'Turnaround':<15}"
        f"{'Waiting':<10}"
    )
    print("-" * 75)

    total_turnaround = 0
    total_waiting = 0

    for row in results:
        print(
            f"{row[0]:<10}"
            f"{row[1]:<10}"
            f"{row[2]:<10}"
            f"{row[3]:<15}"
            f"{row[4]:<15}"
            f"{row[5]:<10}"
        )

        total_turnaround += row[4]
        total_waiting += row[5]

    print("-" * 75)
    print(f"Average Turnaround Time: {total_turnaround / len(results):.2f} ms")
    print(f"Average Waiting Time: {total_waiting / len(results):.2f} ms")


rr_results = round_robin(processes, quantum)
fcfs_results = fcfs(processes)

display_table("ROUND ROBIN (Time Quantum = 2 ms)", rr_results)
display_table("FCFS", fcfs_results)
