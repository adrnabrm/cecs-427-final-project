import networkx as nx
from typing import Dict
import random

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