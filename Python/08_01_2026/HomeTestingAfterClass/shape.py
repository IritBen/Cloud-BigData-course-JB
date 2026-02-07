"""This is abstract shape class it contains the number of edges and nodes"""

from abc import ABC, abstractmethod

class Shape(ABC):

    def __init__(self, edges, nodes):
        super().__init__()
        self.edges = edges
        self.nodes = nodes

    def get_edges(self):
        return self.edges

    def get_nodes(self):
        return self.nodes
    
    @abstractmethod
    def calaulate_area(self):
        pass

    @abstractmethod
    def calculate_parimeter(self):
        pass





