from .tasks import Task_upgrade_mex, Task_build_storage, Task_wait

def bo_mex_upgrade_together_storage(loops, delay_time):
    queue = []
    for i in range(loops):
        queue.append(Task_upgrade_mex(f"Mex #{i + 1}"))
        for j in range(4):
            queue.append(Task_build_storage(f"Mex #{i + 1} - Storage #{j + 1}"))
        if i < loops - 1:
            queue.append(Task_wait(f"Wait {delay_time}s", delay_time))
    return queue

def bo_mex_upgrade_then_storage(loops, delay_time):
    queue = []
    for i in range(loops):
        queue.append(Task_upgrade_mex(f"Mex #{i + 1}"))
        if i < loops - 1:
            queue.append(Task_wait(f"Wait {delay_time}s", delay_time))
    for i in range(loops-1, -1, -1):
        for j in range(4):
            queue.append(Task_build_storage(f"Mex #{i + 1} - Storage #{j + 1}"))
        if i > 0:
            queue.append(Task_wait(f"Wait {delay_time}s", delay_time))
    return queue