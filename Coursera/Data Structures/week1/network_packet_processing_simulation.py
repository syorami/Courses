# python3

from collections import namedtuple

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])
RequestQueue = namedtuple('Queue', ['finish_time', 'Request'])

class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = []
        self.queue = []

    def process(self, request):
        # write your code here

        # first request
        if len(self.finish_time) == 0:
            finish_time = request.arrived_at + request.time_to_process
            self.finish_time.append(finish_time)
            self.queue.append(RequestQueue(finish_time, request))
            return Response(False, request.arrived_at)

        if request.arrived_at >= self.finish_time[-1]:
            self.queue.pop(0)
            finish_time = request.arrived_at + request.time_to_process
            self.finish_time.append(finish_time)
            self.queue.append(RequestQueue(finish_time, request))
            return Response(False, request.arrived_at)
        else:
            if self.queue[0].finish_time <= request.arrived_at:
                self.queue.pop(0)
            if len(self.queue) < self.size:
                finish_time = self.finish_time[-1] + request.time_to_process
                self.queue.append(RequestQueue(finish_time, request))
                self.finish_time.append(finish_time)
                return Response(False, self.finish_time[-2])
            else:
                return Response(True, -1)


def process_requests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.process(request))
    return responses


def main():
    buffer_size, n_requests = map(int, input().split())
    requests = []
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))

    buffer = Buffer(buffer_size)
    responses = process_requests(requests, buffer)

    for response in responses:
        print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
