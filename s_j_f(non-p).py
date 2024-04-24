def sjf_scheduling(processes, n, arrival_time, burst_time):
    completion_time = [0] * n
    turnaround_time = [0] * n
    waiting_time = [0] * n


    process_list = [(processes[i], arrival_time[i], burst_time[i]) for i in range(n)]
    process_list.sort(key=lambda x: (x[1], x[2]))  

    current_time = 0
    for i in range(n):
        process_id, arrival_t, burst_t = process_list[i]
        if current_time < arrival_t:
            current_time = arrival_t
        current_time += burst_t
        completion_time[processes.index(process_id)] = current_time


    total_turnaround_time = 0
    total_waiting_time = 0
    for i in range(n):
        process_id, arrival_t, _ = process_list[i]
        index = processes.index(process_id)
        turnaround_time[index] = completion_time[index] - arrival_t
        waiting_time[index] = turnaround_time[index] - burst_time[index]
        total_turnaround_time += turnaround_time[index]
        total_waiting_time += waiting_time[index]


    avg_turnaround_time = total_turnaround_time / n
    avg_waiting_time = total_waiting_time / n


    for i in range(n):
        print(f"{processes[i]}\t{arrival_time[i]}\t\t{burst_time[i]}\t\t{completion_time[i]}\t\t{turnaround_time[i]}\t\t{waiting_time[i]}")

    print(f"\nAverage Turnaround Time: {avg_turnaround_time}")
    print(f"Average Waiting Time: {avg_waiting_time}")



if __name__ == "__main__":
    processes = [1, 2, 3, 4]
    n = len(processes)

    arrival_time = [1, 2, 1, 4]
    burst_time = [3, 4, 2, 4]

    sjf_scheduling(processes, n, arrival_time, burst_time)
