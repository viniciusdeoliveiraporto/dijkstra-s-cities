# 📍 dijkstra-s-cities

A Python project that implements Dijkstra’s algorithm to find the shortest path between cities represented as a weighted graph. Perfect for route systems, GPS-like applications, and network analysis.

---

## 🚀 Features

- Graph-based representation of cities and connections.
- Shortest path calculation using Dijkstra’s algorithm.
- Automated unit tests with `pytest`.
- Code coverage reports using `pytest-cov`.

---

## 🛠️ Installation

1. Clone the repository:

git clone https://github.com/your-username/dijkstra-s-cities.git
cd dijkstra-s-cities

2. Install dependencies:

pip install -r requirements.txt

3. To run all unit tests with pytest:

python -m pytest <path/to/file>  // It's mandatory that you run the previous command from the root of the directory
                                 // Otherwise FileNotFoundErrors will be thrown 

4. To generate a coverage report using pytest-cov:

python -m pytest tests --cov=src

This will produce a detailed coverage report for the src folder.
