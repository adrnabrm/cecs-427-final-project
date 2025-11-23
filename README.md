# cecs-427-final-proiject

## Setup Virtual Environment (Shared)

```bash
python3 -m venv .venv
source .venv/bin/activate   # or .venv\Scripts\activate
pip install -r requirements.txt
```
make separate files pls :p
## TODO:
- Compute metrics for each graph:
   * Nodes, edges [DONE]
   * Density
   * Average degree
   * Clustering coefficient (`nx.average_clustering`)
   * Average path length (`nx.average_shortest_path_length`)
   * Modularity (`nx.community.louvain_communities`)
- Count detected sub-communities.
- Identify top bridge nodes via **edge betweenness centrality**.
- Plot a small subgraph (≈200–500 nodes) per language.
- Color by detected community.
- Optionally visualize bridges or central nodes.
