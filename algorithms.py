import networkx as nx
from typing import Dict

class GraphAnalysis:

    def density(graphs: Dict[str, nx.Graph]) -> Dict[str, float]:
        """Compute density for each language graph."""
        return {lang: nx.density(G) for lang, G in graphs.items()}
        