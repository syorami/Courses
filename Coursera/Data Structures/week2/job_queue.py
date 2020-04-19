# python3

import random

from collections import namedtuple

Job = namedtuple('Job', ['id', 'next_end_time'])
StartJob = namedtuple('Start', ['id', 'start_time'])

class JobQueue:

    def __init__(self):
        self.queues = []
        self.startjob = []

    def swap(self, a, b):
        self.queues[a], self.queues[b] = self.queues[b], self.queues[a]

    def compare(self, a, b):
        if self.queues[a].next_end_time < self.queues[b].next_end_time: return a
        elif self.queues[a].next_end_time == self.queues[b].next_end_time and self.queues[a].id < self.queues[b].id: return a
        else: return b

    def makeheap(self):
        LENGTH = len(self.queues)
        for i in range(LENGTH // 2, -1, -1):
            self.siftdown(i)

    def siftup(self, index):
        if index != 0:
            parent = (index - 1) // 2
            if self.compare(parent, index) == index:
                self.swap(parent, index)
                self.siftup(parent)

    def siftdown(self, index):
        if 2 * index + 2 <= len(self.queues) - 1:
            leftchild, rightchild = 2 * index + 1, 2 * index + 2
            min_index = self.compare(leftchild, rightchild)
            if self.compare(min_index, index) != index:
                self.swap(index, min_index)
                self.siftdown(min_index)
        elif 2 * index + 1 == len(self.queues) - 1:
            if self.compare(2 * index + 1, index) != index:
                self.swap(index, 2 * index + 1)

    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))

        assert m == len(self.jobs)

    def write_response(self):
        for i in range(len(self.startjob)):
            print(self.startjob[i].id, self.startjob[i].start_time)

    def fast_assign_jobs(self):
        for i in range(min(self.num_workers, len(self.jobs))):
            self.queues.append(Job(i, self.jobs[i]))
            self.startjob.append(StartJob(i, 0))

        self.makeheap()

        for i in range(min(self.num_workers, len(self.jobs)), len(self.jobs)):
            self.startjob.append(StartJob(self.queues[0].id, self.queues[0].next_end_time))
            current_id, next_time = self.queues[0].id, self.queues[0].next_end_time + self.jobs[i]
            self.swap(0, -1)
            self.queues.pop(-1)
            self.siftdown(0)
            self.queues.append(Job(current_id, next_time))
            self.siftup(len(self.queues) - 1)

    def solve(self):
        self.read_data()
        self.fast_assign_jobs()
        self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()

