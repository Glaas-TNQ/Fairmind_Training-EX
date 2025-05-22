# Exercise 2: Basic Data Visualization Class
# ------------------------------------------
# This script defines a minimal data visualization tool using matplotlib.
# The goal is to critique the design as a contributor to open-source libraries,
# and identify improvements that could bring it closer to the functionality and
# robustness of mature tools like Seaborn or Plotly.

import matplotlib.pyplot as plt

class DataVisualizer:
   def __init__(self, data):
       self.data = data
       
   def plot(self, kind='line'):
       if kind == 'line':
           plt.plot(self.data)
       elif kind == 'bar':
           plt.bar(range(len(self.data)), self.data)
       plt.show()

# Example usage
visualizer = DataVisualizer([10, 20, 30, 40, 50])
visualizer.plot('bar')
