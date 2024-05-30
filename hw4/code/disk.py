import random as rand
from copy import deepcopy

class Algorithm:
    def __init__ (self, disk_request, head):
        self.disk_request = deepcopy(disk_request)
        self.head = head
        self.movement = 0

    def get_closest_to_head(self):
        index = len(self.disk_request) - 1
        smallest = int(1e9)
        for i in range(len(self.disk_request)-1, 0, -1):
            if self.disk_request[i] < self.head:
                break
            if self.disk_request[i] < smallest:
                smallest = self.disk_request[i]
                index = i
        return index
    
    def get_movement(self):
        return self.movement

class Fcfs(Algorithm):
    def get_movement(self):
        self.movement = 0
        for i in range(len(self.disk_request)):
            self.movement += abs(self.head - self.disk_request[i])
            self.head = self.disk_request[i]
        return self.movement

class Scan(Algorithm):
    def get_movement(self):
        self.movement = 0
        self.disk_request.sort()
        index = self.get_closest_to_head()
        for i in range(index, len(self.disk_request)):
            self.movement += abs(self.head - self.disk_request[i])
            self.head = self.disk_request[i]
        for i in range(index, -1, -1):
            self.movement += abs(self.head - self.disk_request[i])
            self.head = self.disk_request[i]
        return self.movement

class Cscan(Algorithm):
    def get_movement(self):
        self.movement = 0
        self.disk_request.sort()
        index = self.get_closest_to_head()
        for i in range(index, len(self.disk_request)):
            self.movement += abs(self.head - self.disk_request[i])
            self.head = self.disk_request[i]
        self.head = self.disk_request[0]
        for i in range(1, index):
            self.movement += abs(self.head - self.disk_request[i])
            self.head = self.disk_request[i]
        return self.movement

def get_disk_request(n):
    request = []
    for i in range(n):
        request.append(rand.randint(0, 4999))
    return request

def main():
    disk_request = get_disk_request(1000)
    head = int(input("Enter the head: "))

    fcfs = Fcfs(disk_request, head)
    fcfs_movement = fcfs.get_movement()
    print("FCFS: ", fcfs_movement)

    scan = Scan(disk_request, head)
    scan_movement = scan.get_movement()
    print("SCAN: ", scan_movement)

    cscan = Cscan(disk_request, head)
    cscan_movement = cscan.get_movement()
    print("CSCAN: ", cscan_movement)

main()