# cecs-427-final-proiject

## Setup Virtual Environment (Shared)

```bash
python3 -m venv .venv
source .venv/bin/activate   # or .venv\Scripts\activate
pip install -r requirements.txt
```
make separate files pls :p
## Main idea:
Do Twitch streamer communities exhibit echo-chamber–like behavior, and how does this differ across language groups?

## TODO:
- Compute metrics for each graph:
   * Nodes, edges [DONE BY ADRIAN]
   * Density [DONE BY ADRIAN]
   * Average degree
   * Clustering coefficient (`nx.average_clustering`)
   * Average path length (`nx.average_shortest_path_length`)
   * Modularity (`nx.community.louvain_communities`)
- Count detected sub-communities.
- Identify top bridge nodes via **edge betweenness centrality**.
- Plot a small subgraph (≈200–500 nodes) per language.
- Color by detected community.
- Optionally visualize bridges or central nodes.

once we get all these stats we can go further by having chat analyze them to see what it finds
chats pretty good at summarizing data

most likely smth like this:
## 🔬 What your statistics directly answer
###  1️⃣ Density & Average Degree

→ Are users mostly connected to people within their language group?
→ Higher density = stronger potential echo chambers.

### 2️⃣ Clustering Coefficient

→ Do users’ friends all know each other?
→ High clustering = closed, insular communities (triadic closure).

### 3️⃣ Average Path Length

→ How easily does information flow inside the community?
→ Shorter paths in dense groups → faster reinforcement of beliefs.

### 4️⃣ Modularity & Sub-Communities

→ How strongly segmented is each language network into smaller cliques?
→ High modularity = community fragmentation and echo-chamber risk.

### 5️⃣ Bridge Nodes (Weak Ties)

→ Are there users that connect isolated groups?
→ Few bridges = information stays stuck inside clusters.
