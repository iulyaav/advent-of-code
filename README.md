# Advent of Code problems

This repo will eventually have all the problems from the Advent of Code 2018. All of them are solved using Python 3.6.

## How to run
Each problem will have a name of the form `day_<day_number>_part_<part_number>.py`. If the problem consists of
only one part, then the file name will reflect this. To run it, I've provided you with three options. All of the work on
the assumption that you will run them from a console. For now, no external packages have been used, hence the lack of a
requirements file, but this is not excluded in the future. In this case, a new step will be added to this description.

1. If simply run the file, then the test input from the puzzle's statement has been provided
    `python day_8.py`

2. You can provide input either py piping a file or by writing it by hand. In the later case, please add quotes around
the example.
    * `puython day_8.py < input_file.txt`
    * `python day_8.py "This is my input"`
    

## Day 8
You are given a tree-like structure. Below is the explanation from the 8th day's puzzle.

```text
The tree is made up of nodes; a single, outermost node forms the tree's root, and it contains all other nodes in the 
tree (or contains nodes that contain nodes, and so on).

Specifically, a node consists of:

- A header, which is always exactly two numbers:
- The quantity of child nodes.
- The quantity of metadata entries.
- Zero or more child nodes (as specified in the header).
- One or more metadata entries (as specified in the header).

Each child node is itself a node that has its own header, child nodes, and metadata.
```
