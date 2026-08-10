n = 3
arrival = [0, 1, 2]
burst = [5, 3, 6]
remaining = burst.copy()
completion = [0] * n
turnaround = [0] * n
waiting = [0] * n

quantum = 2
time = 0
completed = 0
queue = []
visited = [False] * n

while completed < n:
    for i in range(n):
        if arrival[i] <= time and not visited[i]:
            queue.append(i)
            visited[i] = True

    if not queue:
        time += 1
        continue

    i = queue.pop(0)

    execution_time = min(quantum, remaining[i])
    time += execution_time
    remaining[i] -= execution_time

    for j in range(n):
        if arrival[j] <= time and not visited[j]:
            queue.append(j)
            visited[j] = True

    if remaining[i] > 0:
        queue.append(i)
    else:
        completion[i] = time
        completed += 1

for i in range(n):
    turnaround[i] = completion[i] - arrival[i]
    waiting[i] = turnaround[i] - burst[i]

avg_tat = sum(turnaround) / n
avg_wt = sum(waiting) / n

print("Process\tAT\tBT\tCT\tTAT\tWT")

for i in range(n):
    print(f"P{i + 1}\t{arrival[i]}\t{burst[i]}\t"
          f"{completion[i]}\t{turnaround[i]}\t{waiting[i]}")

print(f"\nAverage Turnaround Time = {avg_tat:.2f} ms")
print(f"Average Waiting Time = {avg_wt:.2f} ms")
