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
Here’s the tight, no-fluff recap of **what each metric means** and **why it matters for your comparative analysis**:

---

## **1. Nodes & Edges**

**What it means:** Size of the community and how many friendships exist.
**Why it matters:** Larger or smaller networks behave differently; gives context for all other metrics.

---

## **2. Density**

**What it means:** Fraction of possible edges that actually exist.
**Why it matters:** Shows how tightly knit or sparse a language community is.

---

## **3. Average Degree**

**What it means:** Average number of connections per user.
**Why it matters:** Measures how socially active or isolated users are in each language.

---

## **4. Clustering Coefficient**

**What it means:** Likelihood that friends of a user are also friends with each other.
**Why it matters:** High clustering = strong triadic closure → tight subcommunities.

---

## **5. Average Path Length**

**What it means:** Average number of steps needed to reach another user.
**Why it matters:** Tests the “small-world” property; shorter paths mean faster information flow.

---

## **6. Modularity**

**What it means:** How strongly the network splits into communities.
**Why it matters:** High modularity = strong echo-chamber structure and deep community fragmentation.

---

## **7. Sub-community Count**

**What it means:** How many distinct groups the algorithm finds.
**Why it matters:** Shows how fragmented or unified each language network is.

---

## **8. Edge Betweenness Centrality (Bridge Nodes)**

**What it means:** Edges that lie on many shortest paths; connectors between groups.
**Why it matters:** Identifies weak ties that are essential for cross-community communication.

---

## **9. Visualization of Subgraphs**

**What it means:** A small, visible slice of the network.
**Why it matters:** Lets you *show* the structural differences across languages — not just state them.

---

Each metric contributes a different dimension of understanding:
**cohesion, fragmentation, connectivity, and information flow** — the core themes of your report.
