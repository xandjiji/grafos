# Minimum spanning trees and communities

From any dataset, we can generate a MST using Prim's algorithm. By cutting edges on our graph (based on their weights) we can separate our group in smaller subgroups within our community.

The dataset used as our study object was [Thurman Office](http://www.casos.cs.cmu.edu/computational_tools/datasets/external/thuroff/index2.html) (already included in this repository)

This project was made using Python and a few libraries already included (```Numpy```, ```NetworkX``` and ```matplotlib```)

---

### Results

Original dataset graph:
<p align="center">
  <img src="https://raw.githubusercontent.com/xandjiji/grafos/master/grafo%20office.png">
</p>

Minimum spanning tree:
<p align="center">
  <img src="https://raw.githubusercontent.com/xandjiji/grafos/master/MST%20de%20office.png">
</p>

Divided in 2 subgroups:
<p align="center">
  <img src="https://raw.githubusercontent.com/xandjiji/grafos/master/office%20em%202%20grupos.png">
</p>

Divided in 5 subgroups:
<p align="center">
  <img src="https://raw.githubusercontent.com/xandjiji/grafos/master/office%20em%205%20grupos.png">
</p>
