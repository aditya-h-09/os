def best_fit(memory_partitions, processes):
    allocation = {}
    for process, size in processes.items():
        best_fit_partition = None
        min_space = float('inf')
        for partition in memory_partitions:
            if partition >= size and partition - size < min_space:
                best_fit_partition = partition
                min_space = partition - size
        if best_fit_partition is not None:
            allocation[process] = best_fit_partition
            memory_partitions.remove(best_fit_partition)
            print(f"Allocated Process {process} to Memory Partition {best_fit_partition} ({size}K)")
        else:
            print(f"Process {process} is waiting for memory.")
    print("\nFinal Memory Allocation:")
    for process, partition in allocation.items():
        print(f"Process {process} is allocated to Memory Partition {partition} ({processes[process]}K)")
    for partition in memory_partitions:
        print(f"Memory Partition {partition} is free.")


memory_partitions = [100, 500, 200, 300, 600]  
processes = {
    'A': 212,
    'B': 417,
    'C': 112,
    'D': 426
}

print("Best Fit Memory Allocation:")
best_fit(memory_partitions, processes)
