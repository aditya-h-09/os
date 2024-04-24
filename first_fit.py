def first_fit(memory_partitions, processes):
    allocated_processes = {}
    for process_name, process_size in processes.items():
        allocated = False
        for i, partition_size in enumerate(memory_partitions):
            if partition_size >= process_size:
                allocated_processes[process_name] = i
                memory_partitions[i] -= process_size
                allocated = True
                break
        if not allocated:
            print(f"Process {process_name} (Size: {process_size}K) is waiting for memory.")

    print("\nMemory Status After Allocation:")
    for process_name, partition_index in allocated_processes.items():
        print(f"Process {process_name} is allocated to Memory Partition {partition_index + 1}.")

    print("\nFinal Memory Status:")
    for i, partition_size in enumerate(memory_partitions):
        print(f"Memory Partition {i + 1}: {partition_size}K")


memory_partitions = [100, 500, 200, 300, 600]  
processes = {
    'A': 212,
    'B': 417,
    'C': 112,
    'D': 426
}

print("First Fit Memory Allocation Simulation:")
first_fit(memory_partitions, processes)
