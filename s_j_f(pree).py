class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.start_time = 0
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0
        self.response_time = -1  # Initialize response time to -1

def srtf_scheduling(processes):
    n = len(processes)
    current_time = 0
    finished_processes = 0
    gantt_chart = []

    while finished_processes < n:
        min_remaining_time = float('inf')
        selected_process = None

        for process in processes:
            if process.arrival_time <= current_time and process.remaining_time > 0:
                if process.remaining_time < min_remaining_time:
                    min_remaining_time = process.remaining_time
                    selected_process = process

        if selected_process is None:
            current_time += 1
            gantt_chart.append("Idle")
        else:
            if selected_process.response_time == -1:
                selected_process.response_time = current_time - selected_process.arrival_time
            if selected_process.remaining_time == selected_process.burst_time:
                selected_process.start_time = current_time
            selected_process.remaining_time -= 1
            current_time += 1
            gantt_chart.append(selected_process.pid)

            if selected_process.remaining_time == 0:
                selected_process.completion_time = current_time
                selected_process.turnaround_time = selected_process.completion_time - selected_process.arrival_time
                selected_process.waiting_time = selected_process.turnaround_time - selected_process.burst_time
                finished_processes += 1

    return gantt_chart

def display_table(processes):
    total_waiting_time = 0
    total_turnaround_time = 0
    total_response_time = 0
    
    print("PID\tArrival Time\tBurst Time\tCompletion Time\tTurnaround Time\tWaiting Time\tResponse Time")
    for process in processes:
        total_waiting_time += process.waiting_time
        total_turnaround_time += process.turnaround_time
        total_response_time += process.response_time
        
        print(f"{process.pid}\t{process.arrival_time}\t\t{process.burst_time}\t\t{process.completion_time}\t\t"
              f"{process.turnaround_time}\t\t{process.waiting_time}\t\t{process.response_time}")

    avg_waiting_time = total_waiting_time / len(processes)
    avg_turnaround_time = total_turnaround_time / len(processes)
    avg_response_time = total_response_time / len(processes)
    
    print(f"\nAverage Response Time: {avg_response_time}")
    print(f"Average Turnaround Time: {avg_turnaround_time}")
    print(f"Average Waiting Time: {avg_waiting_time}")
    
if __name__ == "__main__":
    processes = [
        Process("P1", 0, 5),
        Process("P2", 1, 3),
        Process("P3", 2, 4),
        Process("P4", 4, 1)
    ]

    gantt_chart = srtf_scheduling(processes)
    print("\n")

    display_table(processes)
