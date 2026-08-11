print("Aafiya Shaikh")

def fcfs(processes):
    processes.sort(key=lambda x: x[1])
    time = 0
    total_wt = 0
    total_tat = 0

    for p in processes:
        pid, at, bt = p

        if time < at:
            time = at

        wt = time - at
        time += bt
        tat = time - at

        p.extend([wt, tat])
        total_wt += wt
        total_tat += tat

    print("\nFCFS Scheduling")
    print("-" * 50)
    print("Process\tArrival Time\tBurst Time\tWaiting Time\tTurnaround Time")
    print("-" * 50)

    for p in processes:
        print(f"P{p[0]}\t{p[1]}\t\t{p[2]}\t\t{p[3]}\t\t{p[4]}")

    print("-" * 50)
    print(f"Average Waiting Time = {total_wt / len(processes):.2f} ms")
    print(f"Average Turnaround Time = {total_tat / len(processes):.2f} ms")

    print("\nGantt Chart:")
    print("|", end=" ")

    for p in processes:
        print(f"P{p[0]} |", end=" ")

    print()


processes = [
    [1, 0, 5],
    [2, 1, 3],
    [3, 2, 8],
    [4, 3, 6]
]

fcfs(processes)
