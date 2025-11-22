import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import os
from typing import Dict

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
    for lang, G in graphs.items():
        print(f"{lang}: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges")
