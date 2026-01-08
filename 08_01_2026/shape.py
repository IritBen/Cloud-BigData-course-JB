"""This is the abstract shape class it contains the number of edges and nodes"""

from abc import ABC, abstractmethod

class Shape(ABC):

    def __init__(self, edges, nodes):
        super().__init__()
        self.edges = edges
        self.nodes = nodes

    def how_many_edges(self):
        return self.edges

    def how_many_nodes(self):
        return self.nodes
    
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass
        
