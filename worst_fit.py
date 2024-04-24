def worst_fit(memory_partitions, processes):
    memory_status = {partition: None for partition in memory_partitions}
    
    for process_name, process_size in processes.items():
        worst_fit_partition = None
        max_remaining_size = -1
        
        for partition, allocated_process in memory_status.items():
            if allocated_process is None and partition >= process_size:
                remaining_size = partition - process_size
                if remaining_size > max_remaining_size:
                    worst_fit_partition = partition
                    max_remaining_size = remaining_size
        
        if worst_fit_partition is not None:
            memory_status[worst_fit_partition] = process_name
            print(f"Process {process_name} ({process_size}K) allocated to {worst_fit_partition}K memory")
        else:
            print(f"Process {process_name} ({process_size}K) is waiting for memory")
    
    print("\nFinal Memory Status:")
    for partition, allocated_process in memory_status.items():
        if allocated_process is None:
            print(f"{partition}K memory: Free")
        else:
            print(f"{partition}K memory: Allocated to Process {allocated_process} ({processes[allocated_process]}K)")



memory_partitions = [100, 500, 200, 300, 600]  


processes = {
    'Process A': 212,
    'Process B': 417,
    'Process C': 112,
    'Process D': 426
}

print("Worst Fit Memory Allocation:")
worst_fit(memory_partitions, processes)
