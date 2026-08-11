print("Aafiya Shaikh")

def sjf(processes):
    n = len(processes)
    completed = 0
    time = 0
    visited = [False] * n
    result = []

    while completed < n:
        idx = -1
        min_bt = float('inf')

        for i in range(n):
            if not visited[i] and processes[i][1] <= time:
                if processes[i][2] < min_bt:
                    min_bt = processes[i][2]
                    idx = i

        if idx == -1:
            time += 1
        else:
            pid, at, bt = processes[idx]

            wt = time - at
            time += bt
            tat = time - at

            result.append([pid, at, bt, wt, tat])
            visited[idx] = True
            completed += 1

    total_wt = sum(p[3] for p in result)
    total_tat = sum(p[4] for p in result)

    print("\nNon-Preemptive SJF Scheduling")
    print("-" * 50)
    print("Process\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time")
    print("-" * 50)

    for p in result:
        print(f"P{p[0]}\t{p[1]}\t\t{p[2]}\t\t{p[3]}\t\t{p[4]}")

    print("-" * 50)
    print(f"Average Waiting Time = {total_wt / n:.2f} ms")
    print(f"Average Turnaround Time = {total_tat / n:.2f} ms")

    print("\nGantt Chart:")
    print("|", end=" ")

    for p in result:
        print(f"P{p[0]} |", end=" ")

    print()


processes = [
    [1, 0, 7],
    [2, 2, 4],
    [3, 4, 1],
    [4, 5, 4]
]

sjf(processes)
