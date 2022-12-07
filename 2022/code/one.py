
import heapq

def main(arg: str, data: str):
    elf = 0
    top_elfs = []
    heapq.heapify(top_elfs)
    for line in data.split('\n'):
        if line == "":
            heapq.heappush(top_elfs, -1 * elf)
            elf = 0
        else:
            elf += int(line)
    if arg in ["a", "test"]:
        print(-1 * heapq.heappop(top_elfs))
    elif arg == "b":
        print(sum([-1 * heapq.heappop(top_elfs) for _ in range(3) ]))

