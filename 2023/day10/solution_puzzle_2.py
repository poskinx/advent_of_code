"""
    | is a vertical pipe connecting north and south.
    - is a horizontal pipe connecting east and west.
    L is a 90-degree bend connecting north and east.
    J is a 90-degree bend connecting north and west.
    7 is a 90-degree bend connecting south and west.
    F is a 90-degree bend connecting south and east.
    . is ground; there is no pipe in this tile.
    S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.

"""

import matplotlib.pyplot as plt
import networkx as nx
import numpy as np


def parse_input(input_lines):
    # Convert the input into a list of strings
    grid = [list(line.strip()) for line in input_lines]
    return grid


def create_graph(grid, rows, cols):
    G = nx.Graph()

    start_node = None  # To store the starting position node
    south = ["|", "7", "F", "S"]
    north = ["|", "L", "J", "S"]
    east = ["-", "L", "F", "S"]
    west = ["-", "J", "7", "S"]

    for i in range(rows):
        for j in range(cols):
            # Add nodes for pipes
            value = grid[i][j]
            if value != ".":
                G.add_node((i, j))

                # Add edges for connections
                if i - 1 >= 0 and grid[i - 1][j] in south and value in north:
                    G.add_edge((i, j), (i - 1, j))
                if i + 1 < rows and grid[i + 1][j] in north and value in south:
                    G.add_edge((i, j), (i + 1, j))
                if j - 1 >= 0 and grid[i][j - 1] in east and value in west:
                    G.add_edge((i, j), (i, j - 1))
                if j + 1 < cols and grid[i][j + 1] in west and value in east:
                    G.add_edge((i, j), (i, j + 1))

                # Mark the starting position node
                if value == "S":
                    start_node = (i, j)
                    G.nodes[start_node]["is_start"] = True
                else:
                    G.nodes[(i, j)]["is_start"] = False

    return G, start_node


"""
Not used at the end
def find_longest_loop(graph, start_node):
    longest_cycle = []
    for cycle in nx.simple_cycles(graph):
        if start_node not in cycle:
            continue
        else:
            if len(cycle) > len(longest_cycle):
                longest_cycle = cycle
    print(f"Longest cycle: {longest_cycle}")
    print(f"Longest cycle length: {len(longest_cycle)}")
    return longest_cycle, len(longest_cycle)
"""


def tiles_enclosed_by_loop(points, rows, cols):
    """
    Returns the area covered by N 2D-points provided in a 'points' array
        points = [ (x1,y1), (x2,y2), ... , (xN, yN) ]
    'grid_size' gives the number of grid cells in x and y direction the
    'points' bounding box is divided into for calculation of the area.
    Larger 'grid_size' values mean smaller grid cells, higher precision
    of the area calculation and longer runtime.
          area_of_points() requires installed matplotlib module.
    """
    pts_x = [int(y) for x, y in points]
    pts_y = [int(x) for x, y in points]
    pts_bb_area = (max(pts_x) - min(pts_x)) * (max(pts_y) - min(pts_y))
    print(pts_bb_area)
    grid_size = [cols, rows]
    range = [[0, cols], [0, rows]]
    h2D, _, _, _ = plt.hist2d(pts_x, pts_y, range=range, cmin=1)
    numberOfWhiteBins = np.count_nonzero(np.isnan(h2D))
    print(np.isnan(h2D))
    print(numberOfWhiteBins)
    numberOfAll2Dbins = h2D.shape[0] * h2D.shape[1]
    print(numberOfAll2Dbins)
    plt.show()
    return numberOfAll2Dbins - numberOfWhiteBins


def main():
    # with open("input.txt", "r") as file:
    with open("test_input_puzzle_3.txt", "r") as file:
        input_lines = file.readlines()

    grid = parse_input(input_lines)
    rows = len(grid)
    cols = len(grid[0])
    graph, start_node = create_graph(grid, rows, cols)
    print(graph, f"- Start node: {start_node}")

    # Uncomment for visualitzation with test data
    # CAVEAT: do not use with full input
    # nx.draw(graph, with_labels=True, font_weight='bold')
    # plt.show()

    # longest_cycle, _len = find_longest_loop(graph, start_node)
    main_loop = nx.find_cycle(graph, source=start_node)
    main_loop_set = set()
    for x, y in main_loop:
        main_loop_set.add(x)
        main_loop_set.add(y)
    print(main_loop_set)
    print(f"Puzzle solution {tiles_enclosed_by_loop(main_loop_set, rows, cols)}.")


if __name__ == "__main__":
    main()
