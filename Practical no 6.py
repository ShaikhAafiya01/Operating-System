from collections import deque


def fcfs(processes):
    time = 0
    results = []

    for pid, arrival, burst in processes:
        if time < arrival:
            time = arrival

        start = time
        completion = time + burst
        turnaround = completion - arrival
        response = start - arrival

        results.append({
            "pid": pid,
            "completion": completion,
            "turnaround": turnaround,
            "response": response
        })

        time = completion

    return results


def round_robin(processes, quantum):
    processes = sorted(processes, key=lambda x: (x[1], x[0]))
    queue = deque()
    remaining = {pid: burst for pid, arrival, burst in processes}
    completion = {}
    response = {}
    arrived = set()

    time = 0
    index = 0
    context_switches = 0
    last_process = None

    while index < len(processes) or queue:
        while index < len(processes) and processes[index][1] <= time:
            pid, arrival, burst = processes[index]
            queue.append(pid)
            arrived.add(pid)
            index += 1

        if not queue:
            time = processes[index][1]
            continue

        pid = queue.popleft()

        if last_process is not None and last_process != pid:
            context_switches += 1

        if pid not in response:
            arrival = next(p[1] for p in processes if p[0] == pid)
            response[pid] = time - arrival

        execution_time = min(quantum, remaining[pid])
        time += execution_time
        remaining[pid] -= execution_time

        while index < len(processes) and processes[index][1] <= time:
            new_pid, arrival, burst = processes[index]
            queue.append(new_pid)
            arrived.add(new_pid)
            index += 1

        if remaining[pid] > 0:
            queue.append(pid)
        else:
            completion[pid] = time

        last_process = pid

    results = []

    for pid, arrival, burst in processes:
        turnaround = completion[pid] - arrival

        results.append({
            "pid": pid,
            "completion": completion[pid],
            "turnaround": turnaround,
            "response": response[pid]
        })

    return results, context_switches


def display_results(name, results, context_switches=None):
    print(f"\n{name}")
    print("-" * 55)
    print(f"{'PID':<10}{'Completion':<15}{'Turnaround':<15}{'Response':<10}")
    print("-" * 55)

    total_turnaround = 0
    total_response = 0

    for result in results:
        print(
            f"{result['pid']:<10}"
            f"{result['completion']:<15}"
            f"{result['turnaround']:<15}"
            f"{result['response']:<10}"
        )

        total_turnaround += result["turnaround"]
        total_response += result["response"]

    count = len(results)

    print("-" * 55)
    print(f"Average Turnaround Time: {total_turnaround / count:.2f}")
    print(f"Average Response Time: {total_response / count:.2f}")

    if context_switches is not None:
        print(f"Context Switches: {context_switches}")


processes = [
    ("P1", 0, 5),
    ("P2", 1, 4),
    ("P3", 2, 2),
    ("P4", 3, 1)
]

quantum = 2

fcfs_results = fcfs(processes)
rr_results, rr_context_switches = round_robin(processes, quantum)

display_results("FCFS", fcfs_results)
display_results("Round Robin", rr_results, rr_context_switches)
