from scipy.io import mmread
from graph_tool import Graph

# Return a graph_tool Graph object from a Matrix Market file
def load_mtx(path, directed):
    matrix = mmread(path, spmatrix=True).tocsr() # Read Matrix Market file
    n, m = matrix.shape

    g = Graph(directed=directed) # Create graph_tool graph
    g.add_vertex(n)

    coo = matrix.tocoo() # Convert in coordinate format for easy access to non-zero entries
    rows = coo.row
    cols = coo.col
    if not directed: # If the graph is undirected, we only want to add edges in one direction to avoid duplicates
        mask = rows < cols
        rows = rows[mask]
        cols = cols[mask]

    g.add_edge_list(zip(rows, cols))
    #print(g)
    return g

#load_mtx("../data/bio-celegans/bio-celegans.mtx", directed=False)