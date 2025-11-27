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
