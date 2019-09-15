import sys


class Node:
    def __init__(self):
        self.leaves = []
        self.node_sum = 0


class MemoryManeuver:
    """
    Given a tree-like structure of the form
    CHILDREN--METADATA-CHILD_NODES-[METADATA_ENTRIES...]
    this class tries to recreate the tree-structure and
    it also computes the value of the node as follows

    - if a node has no child nodes, its value is the sum of its metadata entries
    - if a node does have child nodes, the metadata entries become indexes which refer to those child nodes
    """

    def __init__(self, input_data):
        self.tree_data = [int(number) for number in input_data.split(' ')]
        self.tree = None
        self.solve()

    def solve(self):
        """Recreate the tree structure recursively."""

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
    if len(sys.argv) > 1:
        try:
            mm = MemoryManeuver(sys.argv[1])
            print("Your result is {}".format(mm.tree.node_sum))
        except (ValueError, IndexError):
            print("You did something wrong there when writing the input data.")
    else:
        test_input = input()
        if not test_input:
            print("You haven't entered any input. The test input is going to run.")
            test_input = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"
        mm = MemoryManeuver(test_input)
        print("For the test input [{}] the result is {}".format(test_input, mm.tree.node_sum))
