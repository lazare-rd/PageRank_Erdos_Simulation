# Using the previous Pagerank to initialize a new calculation and Erdos graph generation

## Simulation
We propose an algorithm that simulates the evolution of the web graph from one month to the next, based on an Erdos graph generation algorithm (update_erdos.py)

An implementation of Pagerank (implementation_PageRank.py)

## Comparison

A tool to compare the converging speed of Pagerank initialized with the vector $$x$$ defined by $$\left(x_i\right)^t_{i\ \in \{1,..,N\}}$$ with $$x_i = \frac1N \ \forall \ i \ and \ \forall \ t$$
with Pagerank initialized with the previous month's result.

## Matrix format

You can find matrixs to test the code here https://sparse.tamu.edu/SNAP/soc-Slashdot0902

**Requirements**

Type : square binary

Format : .mtx
