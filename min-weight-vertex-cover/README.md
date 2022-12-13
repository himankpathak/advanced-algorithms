
## Instructions

### Problem 1
Implement a recursive solution to the Minimum Weight Vertex Cover problem
that runs in time O(1.5^n) on graphs of size n.

`command line args: "dat_file weights_file"`
- `python min_weight_vertex_cover.py Graphs/g11.dat Graphs/g11.weights`
- `python min_weight_vertex_cover.py pd_graphs/g14.dat pd_graphs/g14.weights`


### Problem 2
For graphs that are trees, implement that dynamic programming algorithm
to solve this problem exactly in linear time. A program check_tree.cc
determines whether the input graph is a tree.
`command line args: "dat_file weights_file"`
- `python tree_vertex_cover.py Trees/t30.dat Trees/t30.weights`


### Problem 3
Implement that bounded search tree algorithm to find the
Minimum Weighted Vertex Cover of size k or smaller. Your
program will take an extra parameter on the command line (k) and
determine whether there is a vertex cover of size k on the graph. If
there is no such vertex cover, your program will print “No such vertex
cover”. Otherwise, it will return the vertex of size k or smaller of
minimum weight.
`command line args: "dat_file weights_file k_value"`
- `python bst_vertex_cover.py pd_graphs/g14.dat pd_graphs/g14.weights 8`


### Problem 4
Implement an algorithm to find the Minimum Weighted
Vertex Cover in graphs of bounded path width. Your program will
take an extra parameter that is the name of a file that contains the
path decomposition of the graph. Your program will return the minimum
weight vertex cover in the graph
`command line args: "dat_file weights_file path_decomposition_file"`
- `python pd_vertex_cover.py pd_graphs/g20.dat pd_graphs/g20.weights pd_graphs/g20.pd`

