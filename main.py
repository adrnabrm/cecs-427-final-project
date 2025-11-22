import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # Load edges
    edges = pd.read_csv("twitch-dataset/DE/musae_DE_edges.csv")

    # Load node attributes
    nodes = pd.read_csv("twitch-dataset/DE/musae_DE_target.csv")

    G = nx.from_pandas_edgelist(edges, source="from", target="to")
    
    # Convert to dictionary {id: attribute}
    partner_dict = nodes.set_index("new_id")["partner"].to_dict()
    views_dict = nodes.set_index("new_id")["views"].to_dict()
    mature_dict = nodes.set_index("new_id")["mature"].to_dict()

    # Add to graph
    nx.set_node_attributes(G, partner_dict, "partner")
    nx.set_node_attributes(G, views_dict, "views")
    nx.set_node_attributes(G, mature_dict, "mature")

    # Sample a small subgraph (e.g., 200 nodes)
    sub_nodes = list(G.nodes())[:200]
    subG = G.subgraph(sub_nodes)

    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(subG, seed=42)
    nx.draw(subG, pos, node_size=40, edge_color="gray", alpha=0.6)
    plt.title("Twitch DE Subgraph (sample of 200 nodes)")
    plt.show()



