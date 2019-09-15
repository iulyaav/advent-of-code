import sys


class MemoryManeuver:
    """
    Given a tree-like structure of the form
    CHILDREN--METADATA-CHILD_NODES-[METADATA_ENTRIES...]
    this class holds information about the sum of all the
    metadata entries.
    """

    def __init__(self, input_data):
        self.tree_data = [int(number) for number in input_data.split(' ')]
        self.sum_metadata_entries = 0
        self.solve()

    def solve(self):
        """Recursively add all the metadata entries to the
        total sum of the tree structure. The recursive method
        is nested in order to prevent overriding the sum by
        running the solve function multiple times."""

        def _parse (current_index):
            children = self.tree_data[current_index]
            child_index = current_index + 2
            metadata_entries = self.tree_data[current_index + 1]

            for i in range(children):
                child_index = _parse(child_index)

            metadata_last_entry = child_index + metadata_entries
            self.sum_metadata_entries += sum(self.tree_data[child_index:metadata_last_entry])
            return metadata_last_entry

        self.sum_metadata_entries = 0
        _parse(0)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            mm = MemoryManeuver(sys.argv[1])
            print("Your result is {}".format(mm.sum_metadata_entries))
        except (ValueError, IndexError):
            print("You did something wrong there when writing the input data.")
    else:
        test_input = input()
        if not test_input:
            print("You haven't entered any input. The test input is going to run.")
            test_input = "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"
        mm = MemoryManeuver(test_input)
        print("For the test input [{}] the result is {}".format(test_input, mm.sum_metadata_entries))
