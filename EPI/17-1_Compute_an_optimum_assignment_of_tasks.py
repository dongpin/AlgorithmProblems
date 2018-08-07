# 17.1 Compute an optimum assignment of tasks
#

def optimum_task_assignment(task_durations):
    task_durations.sort()
    return [(task_durations[i], task_durations[~i]) for i in range(len(task_durations)//2)]

def main():
    assignment = optimum_task_assignment([2,9,4,4,3,7,5,8])
    print(assignment)

    longest_assigment = max([i[0]+i[1] for i in assignment])
    print(longest_assigment)

if __name__ == '__main__':
    main()