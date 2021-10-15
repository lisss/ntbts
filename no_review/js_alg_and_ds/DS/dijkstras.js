const { PriorityQueue } = require('./heap')

class WeightedGraph {
  constructor() {
    this.adjList = {};
  }

  addVertex(vertex) {
    if (!this.adjList[vertex]) this.adjList[vertex] = [];
  }

  addEdge(v1, v2, weight) {
    if (this.adjList[v1]) {
      this.adjList[v1].push({ node: v2, weight })
    };
    if (this.adjList[v2]) {
      this.adjList[v2].push({ node: v1, weight })
    };
  }

  dijkstra(start, end) {
    const distances = {};
    const previous = {};
    const nodes = new PriorityQueue();
    let smallest;
    const path = [];

    Object.keys(this.adjList).forEach(k => {
      const val = this.adjList[k];
      const dist = k === start ? 0 : Infinity
      previous[k] = null;
      distances[k] = dist;
      nodes.enqueue(k, dist)
    })

    while (nodes.values.length) {
      smallest = nodes.dequeue().value;

      if (smallest === end) {
        while (previous[smallest]) {
          path.push(smallest);
          smallest = previous[smallest];
        }
        path.push(smallest);
        break;
      }

      if (smallest || distances[smallest] !== Infinity) {
        this.adjList[smallest].forEach(nextNode => {
          const candidate = distances[smallest] + nextNode.weight;
          const nextNeigbor = nextNode.node;
          
          if (candidate < distances[nextNeigbor]) {
            distances[nextNeigbor] = candidate;
            previous[nextNeigbor] = smallest;
            nodes.enqueue(nextNeigbor, candidate);
          }
        })
      }
    }

    return path.reverse();
  }
}

module.exports = {
  WeightedGraph,
  PriorityQueue,
}