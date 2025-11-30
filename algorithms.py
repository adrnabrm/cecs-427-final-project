import networkx as nx
from typing import Dict, Tuple, List
import random
import networkx.algorithms.community as nx_comm

class GraphAnalysis:

    @staticmethod
    def density(graphs: Dict[str, nx.Graph]) -> Dict[str, float]:
        """Compute density for each language graph."""
        return {lang: nx.density(G) for lang, G in graphs.items()}
    
    @staticmethod
    def average_degree(graphs: Dict[str, nx.Graph]) -> Dict[str, float]:
        """Compute average degree for each node in a language graph"""

        avg_degrees = {}
        for lang, G in graphs.items():
            degrees = dict(G.degree())
            avg_degrees[lang] = sum(degrees.values()) / G.number_of_nodes()
        return avg_degrees
    
    @staticmethod
    def clustering_coefficient(graphs: Dict[str, nx.Graph]) -> Dict[str, float]:
        """Compute average clustering coefficient for each graph"""
        results = {}
        for lang, G in graphs.items():
            try:
                coeff = nx.average_clustering(G)
            except Exception as e:
                print(f"Error computing clustering for {lang}: {e}")
                coeff = None

            results[lang] = coeff

        return results        

    @staticmethod
    def average_path_length(graphs):
        """
        Compute approximate average shortest path length for each graph.
        Uses only the largest connected component (LCC).
        """
        results = {}

        for lang, G in graphs.items():
            try:
                # Largest connected component
                components = list(nx.connected_components(G))
                largest = max(components, key=len)
                LCC = G.subgraph(largest)

                print(f"Computing approximate APL for {lang}... "
                    f"LCC size = {LCC.number_of_nodes()} nodes")

                # Use fast approximation
                apl = approximate_average_path_length(LCC, sample_size=100)

            except Exception as e:
                print(f"Error computing path length for {lang}: {e}")
                apl = None

            results[lang] = apl

        return results

    @staticmethod
    def modularity_and_communities(graphs: Dict[str, nx.Graph]) -> Dict[str, Tuple[float, int, List]]:
        """
        Compute modularity and detect sub-communities using Louvain algorithm.

        Returns:
            Dict mapping language to (modularity_score, num_communities, communities_list)
        """
        results = {}

        for lang, G in graphs.items():
            try:
                print(f"Detecting communities for {lang}...")

                # Use Louvain algorithm for community detection
                communities = nx_comm.louvain_communities(G, seed=42)

                # Compute modularity score
                modularity = nx_comm.modularity(G, communities)

                num_communities = len(communities)

                results[lang] = (modularity, num_communities, communities)

                print(f"  -> Found {num_communities} communities with modularity {modularity:.4f}")

            except Exception as e:
                print(f"Error computing modularity for {lang}: {e}")
                results[lang] = (None, None, None)

        return results

    @staticmethod
    def identify_bridge_nodes(graphs: Dict[str, nx.Graph], top_n: int = 10) -> Dict[str, List[Tuple]]:
        """
        Identify top bridge nodes (weak ties) using edge betweenness centrality.

        Bridge nodes are those that connect different communities. High edge betweenness
        indicates an edge that lies on many shortest paths between nodes, suggesting
        it bridges different clusters.

        Args:
            graphs: Dictionary of language graphs
            top_n: Number of top bridge edges to return per language

        Returns:
            Dict mapping language to list of (node1, node2, betweenness_score) tuples
        """
        results = {}

        for lang, G in graphs.items():
            try:
                print(f"Computing edge betweenness centrality for {lang}...")
                print(f"  (This may take a while for large graphs...)")

                # Compute edge betweenness centrality
                # This measures how many shortest paths pass through each edge
                edge_betweenness = nx.edge_betweenness_centrality(G, k=500, seed=42)

                # Sort edges by betweenness (highest first)
                sorted_edges = sorted(edge_betweenness.items(), key=lambda x: x[1], reverse=True)

                # Get top N bridge edges
                top_bridges = [(edge[0], edge[1], score) for edge, score in sorted_edges[:top_n]]

                results[lang] = top_bridges

                print(f"  -> Identified top {top_n} bridge edges")

            except Exception as e:
                print(f"Error computing bridge nodes for {lang}: {e}")
                results[lang] = []

        return results

# Helper func    
def approximate_average_path_length(G, sample_size=500):
        """
        Approximate the average shortest path length by sampling.
        Much faster than exact APSP on large graphs.
        """
        nodes = list(G.nodes())

        # If graph is small, compute exact value
        if len(nodes) <= sample_size:
            return nx.average_shortest_path_length(G)

        # Randomly sample nodes
        sample = random.sample(nodes, sample_size)
        lengths = []

        for s in sample:
            sp = nx.single_source_shortest_path_length(G, s)
            lengths.extend(sp.values())  # add all distances from node s

        # Compute average
        return sum(lengths) / len(lengths)  