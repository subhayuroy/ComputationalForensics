import random
import multiprocessing


def list_append(count, id, out_list):
    # appends the count of number of processes which takes place at a time
    for i in range(count):
        out_list.append(random.random())

    if __name__ == "__main__":
        size = 999
        procs = 2
        # Create a list of jobs and then iterate through
        # the number of processes appending each process to
        # the job list
        jobs = []

    for i in range(0, procs):
        out_list = list()  # list of processes
        process1 = multiprocessing.Process(
            target=list_append, args=(size, i, out_list))

        # appends the list of processes
        jobs.append(process1)

    # Calculate the random number of processes
    for j in jobs:
        j.start()  # initiate the process

    # After the processes have finished execution
    for j in jobs:
        j.join()
        print("List processing complete.")