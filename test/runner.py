
import time
import pandas as pd

# TODO: Define a common interface for algorithms (input and output)

# Run a single instance of the algorithm on the graph and motif
def single_run(graph, algorithm, graph_name, algorithm_name, motif):
    start = time.perf_counter() # Measure execution time
    result = algorithm(graph, motif)
    execution_time = time.perf_counter() - start
    # Collect results
    return {
        "graph": graph_name,
        "algorithm": algorithm_name,
        "motif": motif,
        "estimate": result["estimate"],
        "execution_time": execution_time
    }

# Run the algorithm multiple times and collect results
def multiple_runs(graph, algorithm, graph_name, algorithm_name, motif, num_runs=10):
    results = []

    for run in range(num_runs):
        result = {"iteration": run + 1} | single_run(graph, algorithm, graph_name, algorithm_name, motif)
        results.append(result)

    return results

# Run experiments for all combinations of graphs and algorithms
def experiment(graphs, algorithms, motif, num_runs=10):
    all_results = []

    for graph_name, graph in graphs.items():
        for algorithm_name, algorithm in algorithms.items():
            print(f"Running {algorithm_name} on {graph_name}...")
            results = multiple_runs(graph, algorithm, graph_name, algorithm_name, motif, num_runs)
            all_results.extend(results)

    df = pd.DataFrame(all_results)
    print(df)
    return df

# Save the raw results to a CSV file
def save_raw_data(results, output_path):
    results.to_csv(output_path, index=False)


# Compute the mean, standard deviation, and 95% confidence interval for each group of results
def save_aggregated_data(results, output_path):
    pass

# Compare performance of different algorithms on the same graph and motif
def compare():
    pass







def mock_alg1(graph, motif):
    time.sleep(0.1)  # Simulate some computation time
    return {"estimate": 42}  # Mock result

def mock_alg2(graph, motif):
    time.sleep(0.2)  # Simulate some computation time
    return {"estimate": 332}  # Mock result

if __name__ == "__main__":
    datasets={
        "bio-celegans":"../data/bio-celegans/bio-celegans.mtx",
        "bio-diseasome":"../data/bio-disease/bio-disease.mtx",
        "bio-yeast":"../data/bio-yeast/bio-yeast.mtx"
    }

    algorithms = {
        "mock_algorithm1": mock_alg1,
        "mock_algorithm2": mock_alg2
    }

    motif = "some_motif"

    results = experiment(datasets, algorithms, motif)
    save_raw_data(results, "../output/raw_results.csv")