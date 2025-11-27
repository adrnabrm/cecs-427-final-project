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
   * Average degree [DONE BY ADRIAN]
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
## 🔬 What Each Metric Tells Us (Based on Your To-Do List)

### **1️⃣ Nodes & Edges**

→ Establish the size and connection volume of each language community.
→ Larger networks tend to be more fragmented; smaller ones tend to be denser.

---

### **2️⃣ Density & Average Degree**

→ Measure how connected users are within their language group.  
→ Higher density & degree = tighter communities → greater echo-chamber potential.

---

### **3️⃣ Clustering Coefficient**

→ Shows how often “friends of friends” are also friends (triadic closure).  
→ High clustering = closed, tightly-woven groups → stronger internal cohesion.

---

### **4️⃣ Average Path Length**

→ Indicates how quickly information can flow within the network.  
→ Shorter paths = faster spread of trends/behaviors → faster reinforcement loops.

---

### **5️⃣ Modularity & Sub-Community Count**

→ Reveal how strongly the network splits into clusters or cliques.  
→ High modularity + many sub-communities = fragmentation and isolated “micro-echo-chambers.”

---

### **6️⃣ Bridge Nodes (Weak Ties)**

→ Identify users who connect otherwise separate communities.  
→ Few bridges = limited cross-community interaction → information stays trapped in clusters.

---

### **7️⃣ Subgraph Visualizations (200–500 nodes)**

→ Let us *see* the structure behind the metrics.  
→ Visually highlight tightly-knit clusters, sparse regions, and any bridging nodes.
