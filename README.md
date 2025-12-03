# Echo-Chamber Signals in Twitch Language Communities

## Authors
Adrian Abraham · Reichen Brown · Matthew Carranza · Angelo Cervana · Russell Harral

## Abstract
Echo chambers consistently present challenges within social networks. They shape how users interact with information exchanged with others online and how that information traverses among those users. Therefore, they can limit a user’s exposure to diverse content by reinforcing community homogeneity. This report analyzes how the social platform, Twitch, which utilizes language-based community systems, exhibits properties also associated with echo chambers. We construct community networks to compute the density, average degree, clustering coefficient, average path length, modularity, and edge betweenness. The results of the metrics display patterns suggesting that Twitch’s language communities contain fragmentation. By primarily relying on a few weak ties to circulate information, Twitch is prone to homogeneous communities, which reflects the dynamics present in echo chambers.

## Project Overview
This repository measures whether Twitch’s language-specific communities display structural traits commonly linked to echo chambers. We build undirected graphs from Twitch’s `musae` dataset, annotate them with streamer attributes, and evaluate network-level metrics along with visual subgraphs to highlight fragmentation and bridging edges.

## Repository Structure
- `main.py` – end-to-end driver that loads the language graphs, runs all metrics, and writes subgraph visualizations.
- `algorithms.py` – reusable `GraphAnalysis` utilities for density, degree, clustering, approximate path length, Louvain modularity, bridge detection, neighborhood overlap, and visualization helpers.
- `twitch-dataset/` – raw Twitch `musae` data grouped by language (`DE`, `ENGB`, `ES`, `FR`, `PTBR`, `RU`). Each folder contains `*_edges.csv`, `*_target.csv` (node attributes), and some include `*_features.json`.
- `subgraphs/` – generated PNGs showing representative subgraph layouts per language with detected communities and highlighted bridges.
- `requirements.txt` – Python dependencies.

## Metrics and Outputs
For every language-specific graph we compute:
- **Network size** – node and edge counts for overall community scale.
- **Density & average degree** – connectivity level indicating how tightly users cluster.
- **Average clustering coefficient** – prevalence of triadic closure within the language.
- **Approximate average path length** – assessed on the largest connected component using sampling-based shortest paths.
- **Louvain modularity & sub-community count** – strength and number of partitions revealing fragmentation.
- **Top bridge edges** – derived from edge betweenness centrality to surface weak ties across clusters.
- **Neighborhood overlap statistics** – summarizes strong vs. weak ties via proportion of shared neighbors.
- **Subgraph visualizations** – 200–400 node samples stored under `subgraphs/*.png`, colored by detected communities with bridge edges highlighted.

Console output lists each metric per language; image files provide qualitative insight into the detected structures.

## Environment & Tooling
- Python 3.10+
- Key libraries: `pandas`, `networkx`, `matplotlib`, `typing`.
- Optional: `venv` or any virtual environment manager.

### Setup
```bash
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Running the Analysis
```bash
python main.py
```

The script will:
1. Load every language graph from `twitch-dataset/`.
2. Print metric tables to stdout.
3. Produce language-specific PNGs inside `subgraphs/`.

Depending on machine specs, Louvain community detection and betweenness centrality can take several minutes on the largest graphs.