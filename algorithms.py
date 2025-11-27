import networkx as nx
from typing import Dict

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