import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import os
from typing import Dict
from algorithms import GraphAnalysis

def load_data() -> Dict[str, nx.Graph]:
    language_graphs = {}
    for f in os.listdir("./twitch-dataset"):
        path = os.path.join("./twitch-dataset", f)
        if f in ['DE', 'ENGB', 'ES', 'FR', 'PTBR', 'RU']:
            edges = pd.read_csv(f"twitch-dataset/{f}/musae_{f}_edges.csv")
            nodes = pd.read_csv(f"twitch-dataset/{f}/musae_{f}_target.csv")

            G = nx.from_pandas_edgelist(edges, source="from", target="to")

            # Convert to dictionary {id: attribute}
            partner_dict = nodes.set_index("new_id")["partner"].to_dict()
            views_dict = nodes.set_index("new_id")["views"].to_dict()
            mature_dict = nodes.set_index("new_id")["mature"].to_dict()

            # Add to graph
            nx.set_node_attributes(G, partner_dict, "partner")
            nx.set_node_attributes(G, views_dict, "views")
            nx.set_node_attributes(G, mature_dict, "mature")

            language_graphs[f] = G
    return language_graphs

if __name__ == "__main__":
    # Loading graphs
    graphs: Dict[str, nx.Graph] = load_data()
    print(f"--Node and edge counts for each graph--")

    # Print num nodes/edges
    # Denotes size of each community and connections between individuals
    for lang, G in graphs.items():
        print(f"{lang}: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges")
    print()

    # Print density
    # Shows how interconnected each community is
    densities = GraphAnalysis.density(graphs)
    for lang, density in densities.items():
        print(f"{lang} Density: {density}")
    print()

    # Print average degree of each node in each graph
    # High interconnectivity shows tighter communities
    avg_degrees = GraphAnalysis.average_degree(graphs)
    for lang, avg_deg in avg_degrees.items():
        print(f"{lang} Average Degree Count: {avg_deg}")
    print()

    # Print clustering coefficient
    # Measures how tightly knit the neighborhoods are in each community
    clustering_coeffs = GraphAnalysis.clustering_coefficient(graphs)
    for lang, coeff in clustering_coeffs.items():
        print(f"{lang} Average Clustering Coefficient: {coeff}")
    print()

    # Print average shortest path length
    # Must be computed on largest connected component
    avg_paths = GraphAnalysis.average_path_length(graphs)
    for lang, path in avg_paths.items():
        print(f"{lang} Average Path Length (LCC): {path}")
    print()

    # Print modularity and sub-community count
    # High modularity indicates strong community structure (fragmentation)
    # More sub-communities suggests micro-echo-chambers within language groups
    print(f"--Modularity and Community Detection--")
    modularity_results = GraphAnalysis.modularity_and_communities(graphs)
    for lang, (modularity, num_communities, _) in modularity_results.items():
        if modularity is not None:
            print(f"{lang} Modularity: {modularity:.4f} | Sub-communities: {num_communities}")
        else:
            print(f"{lang} Modularity: Error computing")
    print()

    # Identify bridge nodes (weak ties connecting communities)
    # High betweenness centrality edges are critical connections between clusters
    # Few/weak bridges = stronger echo chambers with limited cross-community flow
    print(f"--Bridge Nodes Analysis (Top 5 per language)--")
    bridge_results = GraphAnalysis.identify_bridge_nodes(graphs, top_n=5)
    for lang, bridges in bridge_results.items():
        print(f"\n{lang} Top Bridge Edges:")
        if bridges:
            for i, (node1, node2, score) in enumerate(bridges, 1):
                print(f"  {i}. Edge ({node1}, {node2}): Betweenness = {score:.6f}")
        else:
            print("  Error or no bridges found")
    print()
