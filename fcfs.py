def fcfs_scheduling(processes, n, arrival_time, burst_time):
    completion_time = [0] * n
    turnaround_time = [0] * n
    waiting_time = [0] * n


    current_time = 0
    for i in range(n):
        if current_time < arrival_time[i]:
            current_time = arrival_time[i]
        current_time += burst_time[i]
        completion_time[i] = current_time


    total_turnaround_time = 0
    total_waiting_time = 0
    for i in range(n):
        turnaround_time[i] = completion_time[i] - arrival_time[i]
        waiting_time[i] = turnaround_time[i] - burst_time[i]
        total_turnaround_time += turnaround_time[i]
        total_waiting_time += waiting_time[i]


    avg_turnaround_time = total_turnaround_time / n
    avg_waiting_time = total_waiting_time / n


    print("Process\tArrival Time\tBurst Time\tCompletion Time\tTurnaround Time\tWaiting Time")
    for i in range(n):
        print(f"{processes[i]}\t{arrival_time[i]}\t\t{burst_time[i]}\t\t{completion_time[i]}\t\t{turnaround_time[i]}\t\t{waiting_time[i]}")

    print(f"\nAverage Turnaround Time: {avg_turnaround_time}")
    print(f"Average Waiting Time: {avg_waiting_time}")



if __name__ == "__main__":
    processes = [1, 2, 3, 4]
    n = len(processes)

    arrival_time = [0, 1, 5, 6]
    burst_time = [2, 2, 3, 4]

    fcfs_scheduling(processes, n, arrival_time, burst_time)
