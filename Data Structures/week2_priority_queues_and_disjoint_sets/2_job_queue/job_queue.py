# python3

from collections import namedtuple

class Buffer:
    def __init__(self):
        self.H = []
        self.queue = []
        
    def Parent(self,i):
        return i//2
    def LeftChild(self,i):
        return 2*i+1
    def RightChild(self,i):
        return 2*i+2
    
    def SiftDown(self,i):
        minIndex = i

        l = self.LeftChild(i)
        if l<len(self.H) and self.H[l].process_time<self.H[minIndex].process_time:
            minIndex = l
        elif l<len(self.H) and self.H[l].process_time==self.H[minIndex].process_time and self.H[l].worker<self.H[minIndex].worker:
            minIndex = l

        r = self.RightChild(i)
        if r<len(self.H) and self.H[r].process_time<self.H[minIndex].process_time:
            minIndex = r
        elif r<len(self.H) and self.H[r].process_time==self.H[minIndex].process_time and self.H[r].worker<self.H[minIndex].worker:
            minIndex = r

        if minIndex != i:
            self.H[i], self.H[minIndex] = self.H[minIndex], self.H[i]
            self.SiftDown(minIndex)
            
    def BuildHeap(self):
        size = len(self.H)
        for i in range((size//2), -1, -1):
            self.SiftDown(i)


# AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])
AssignedJob = namedtuple("AssignedJob", ["worker", "started_at", "process_time"])


def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    # result = []
    # next_free_time = [0] * n_workers
    # for job in jobs:
    #     next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
    #     result.append(AssignedJob(next_worker, next_free_time[next_worker]))
    #     next_free_time[next_worker] += job

    # return result

    obj = Buffer()
    #result = []
    i = 0
    if n_workers >= len(jobs):
        for job in jobs:
            q = AssignedJob(i,0,job)
            print(q.worker, q.started_at)
            # obj.queue.append(AssignedJob(i,0,job))
            i += 1
    else:
        for job in jobs:
            if not(n_workers == i):
                # obj.queue.append(AssignedJob(i,0,job))
                q = AssignedJob(i,0,job)
                print(q.worker, q.started_at)
                obj.H.append(AssignedJob(i,0,job))
                i += 1
                if n_workers == i:
                    obj.BuildHeap()
            else:
                output = obj.H[0]
                q = AssignedJob(output.worker,output.process_time,output.process_time+job)
                print(q.worker, q.started_at)
                obj.H[0] = AssignedJob(output.worker,output.process_time,output.process_time+job)
                obj.SiftDown(0)
    ## another solution
    # if n_workers >= len(jobs):
    #     for job in jobs:
    #         obj.queue.append(AssignedJob(i,0,job))
    #         i += 1
    # else:
    #     for j in range(n_workers):
    #         obj.queue.append(AssignedJob(i,0,jobs[j]))
    #         obj.H.append(AssignedJob(i,0,jobs[j]))
    #         i += 1
    #     obj.BuildHeap()
    #     #print(obj.H)
    #     for j in range(n_workers,len(jobs)):
    #         output = obj.H[0]
    #         obj.queue.append(AssignedJob(output.worker,output.process_time,output.process_time+jobs[j]))
    #         #obj.ExtractMin(AssignedJob(output.worker,output.process_time,output.process_time+job))
    #         obj.H[0] = AssignedJob(output.worker,output.process_time,output.process_time+jobs[j])
    #         obj.SiftDown(0)
    #         #print(obj.H)
    #         #result.append(output)
    #         #print(output.worker, output.started_at)
    #         #print(output)
    # while obj.queue!=[]:
    #     output = obj.queue.pop(0)
    #     print(output.worker, output.started_at)


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    # assigned_jobs = assign_jobs(n_workers, jobs)
    assign_jobs(n_workers, jobs)
    # assign_jobs(10000, [1]*100000)

    # for job in assigned_jobs:
    #     print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
