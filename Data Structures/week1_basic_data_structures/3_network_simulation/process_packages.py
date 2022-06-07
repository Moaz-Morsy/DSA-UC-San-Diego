# python3

from collections import namedtuple

Request = namedtuple("Request", ["arrived_at", "time_to_process", "flag"])
#Response = namedtuple("Response", ["was_dropped", "started_at"])


# class Buffer:
#     def __init__(self, size):
#         self.size = size
#         self.finish_time = []

#     def process(self, request):
#         # write your code here
#         return Response(False, -1)

class Buffer:

    def __init__(self, k):
        self.k = k
        self.queue = []#[None] * k
        self.head = self.tail = -1

    # Insert an element into the circular queue
    def enqueue(self, data):

        if ((self.tail + 1) % self.k == self.head):
            print("The circular queue is full\n")

        elif (self.head == -1):
            self.head = 0
            self.tail = 0
            #self.queue[self.tail] = data
            self.queue.insert(self.tail, data)
        else:
            self.tail = (self.tail + 1) % self.k
            #self.queue[self.tail] = data
            self.queue.insert(self.tail, data)

    # Delete an element from the circular queue
    def dequeue(self):
        if (self.head == -1):
            print("The circular queue is empty\n")

        elif (self.head == self.tail):
            #temp = self.queue[self.head]
            temp = self.queue.pop(self.head)
            self.head = -1
            self.tail = -1
            #self.queue = [None] * self.k
            return temp
        else:
            #temp = self.queue[self.head]
            temp = self.queue.pop(self.head)
            self.head = (self.head + 1) % self.k
            return temp


# def process_requests(requests, buffer):
#     responses = []
#     for request in requests:
#         responses.append(buffer.process(request))
#     return responses

def process(packets, obj):
    
    if list(packets.keys()) != []:
        start = list(packets.keys())[0][0]
    else:
        start = 0
    dummy = []
    SF = namedtuple("SF", ["started_at","finished_at"])
    
    for request in packets.keys():
    
        if len(obj.queue) != obj.k:
            if request[0] <= start: 
                obj.enqueue((request,SF(start, start+request[1])))
                start += request[1]
            else:
                dummy = obj.dequeue()
                packets[dummy[0]] = dummy[1]
                start = request[0]
                obj.enqueue((request,SF(start, start+request[1])))

        elif len(obj.queue) == obj.k:
            if (request[0] >= obj.queue[obj.head][1][1]) and (request[0] <= obj.queue[obj.tail][1][1]):
                dummy = obj.dequeue()
                packets[dummy[0]] = dummy[1]
                obj.enqueue((request,SF(start, start+request[1])))
                start += request[1]
            elif (request[0] > obj.queue[obj.tail][1][1]):
                dummy = obj.dequeue()
                packets[dummy[0]] = dummy[1]
                obj.enqueue((request,SF(request[0], request[1])))
                start = request[1]
            else:
                packets[request] = SF(-1, -1)
            

    # obj.queue = list(reversed(obj.queue))
    # while obj.queue != []:
    #     dummy = obj.queue.pop()
    #     packets[dummy[0]] = dummy[1]

    if obj.queue == []:
        pass
    else:
        for i in range(len(obj.queue)):
                dummy = obj.queue[i]
                packets[dummy[0]] = dummy[1]
    obj.queue = []

        # if (obj.tail >= obj.head):
        #     for i in range(obj.head, obj.tail + 1):
        #         dummy = obj.queue[i]
        #         packets[dummy[0]] = dummy[1]
        # else:
        #     for i in range(obj.head, obj.k):
        #         dummy = obj.queue[i]
        #         packets[dummy[0]] = dummy[1]
        #     for i in range(0, obj.tail + 1):
        #         dummy = obj.queue[i]
        #         packets[dummy[0]] = dummy[1]
 

    return packets

# obj = Buffer(buffer_size)
# packets = { r : None for r in requests }

# packets = process(requests, obj, packets)


def main():
    buffer_size, n_requests = map(int, input().split())
    # requests = []
    # for i in range(n_requests):
    #     arrived_at, time_to_process = map(int, input().split())
    #     requests.append(Request(arrived_at, time_to_process, i))
    packets = {}
    for i in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        packets[Request(arrived_at, time_to_process, i)] = None

    #buffer = Buffer(buffer_size)
    obj = Buffer(buffer_size)
    #packets = { r : None for r in requests }
    #responses = process_requests(requests, buffer)
    # packets = process(requests, obj, packets)
    packets = process(packets, obj)

    # for response in responses:
    #     print(response.started_at if not response.was_dropped else -1)
    for response in packets:
        print(packets[response][0])


if __name__ == "__main__":
    main()
