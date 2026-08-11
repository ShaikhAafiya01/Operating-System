print("Aafiya Shaikh")

def fcfs(processes):
    processes.sort(key=lambda x: x[1])
    time = 0
    total_wt = total_tat = 0

    print("\nGantt Chart:")
    print("|", end=" ")

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

        print(f"P{pid} |", end=" ")

    print("\n")
    print("PID\tAT\tBT\tWT\tTAT")

    for p in processes:
        print(f"P{p[0]}\t{p[1]}\t{p[2]}\t{p[3]}\t{p[4]}")

    print(f"\nAverage Waiting Time = {total_wt / len(processes):.2f}")
    print(f"Average Turnaround Time = {total_tat / len(processes):.2f}")


def sjf(processes):
    n = len(processes)
    completed = 0
    time = 0
    visited = [False] * n
    result = []

    print("\nGantt Chart:")
    print("|", end=" ")

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

            print(f"P{pid} |", end=" ")

    total_wt = sum(x[3] for x in result)
    total_tat = sum(x[4] for x in result)

    print("\n")
    print("PID\tAT\tBT\tWT\tTAT")

    for p in result:
        print(f"P{p[0]}\t{p[1]}\t{p[2]}\t{p[3]}\t{p[4]}")

    print(f"\nAverage Waiting Time = {total_wt / n:.2f}")
    print(f"Average Turnaround Time = {total_tat / n:.2f}")


print("CPU Scheduling Algorithms")
print("1. FCFS")
print("2. Non-Preemptive SJF")

choice = int(input("Enter your choice: "))
n = int(input("Enter number of processes: "))

processes = []

for i in range(n):
    print(f"\nProcess P{i + 1}")
    at = int(input("Arrival Time: "))
    bt = int(input("Burst Time: "))
    processes.append([i + 1, at, bt])

if choice == 1:
    fcfs(processes)
elif choice == 2:
    sjf(processes)
else:
    print("Invalid Choice!")
