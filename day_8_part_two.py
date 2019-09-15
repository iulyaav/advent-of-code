class Node:
    def __init__(self):
        self.leaves = []
        self.node_sum = 0


class MemoryManeuver:

    def __init__(self, input_data):
        self.tree_data = [int(number) for number in input_data.split(' ')]
        self.tree = None
        self.solve()

    def solve(self):
        def _parse(current_index):
            children = self.tree_data[current_index]
            child_index = current_index + 2
            metadata_entries = self.tree_data[current_index + 1]

            current_node = Node()

            if children == 0:
                metadata_last_entry = child_index + metadata_entries
                current_node.node_sum += sum(self.tree_data[child_index:child_index + metadata_entries])
            else:
                for _ in range(children):
                    child_index, child_node = _parse(child_index)
                    current_node.leaves.append(child_node)
                metadata_last_entry = child_index + metadata_entries
                for i in range(child_index, child_index + metadata_entries):
                    entry = self.tree_data[i]
                    if entry <= children:
                        current_node.node_sum += current_node.leaves[entry - 1].node_sum

            return metadata_last_entry, current_node

        self.tree = _parse(0)[1]


if __name__ == "__main__":
    mm = MemoryManeuver("2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2")
    print(mm.tree.node_sum)
