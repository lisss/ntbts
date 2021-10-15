class Graph {
  constructor() {
    this.adjList = {
      'A': ['B', 'C'],
      'B': ['A', 'D'],
      'C': ['A', 'E'],
      'D': ['B', 'E', 'F'],
      'E': ['C', 'D', 'F'],
      'F': ['D', 'E'],
    };
  }

  addVertex(vertex) {
    if (!this.adjList[vertex]) this.adjList[vertex] = [];
  }

  addEdge(v1, v2) {
    if (this.adjList[v1]) this.adjList[v1].push(v2);
    if (this.adjList[v2]) this.adjList[v2].push(v1);
  }

  removeEdge(v1, v2) {
    if (this.adjList[v1]) {
       this.adjList[v1] = this.adjList[v1].filter(x => x !== v2);
    }
    if (this.adjList[v2]) {
       this.adjList[v2] = this.adjList[v2].filter(x => x !== v1);
    }
  }

  removeVertex(v) {
    if (this.adjList[v]) {
      this.adjList[v].forEach(x => this.removeEdge(v, x));
      delete this.adjList[v];
    }
  }

  dfsReq(vertex) {
    const res = [];
    const visited = {};

    const _do = (vertex) => {
      if (!vertex || !this.adjList[vertex]) return

      res.push(vertex);
      visited[vertex] = true;
      this.adjList[vertex].forEach(x => {
        if (!visited[x]) _do(x);
      })
    }
    _do(vertex);
    return res;
  }

  dfsIter(vertex) {
    if (!this.adjList[vertex]) return;

    const res = [];
    const stack = [vertex];
    const visited = {};
    let currV;

    visited[vertex] = true;

    while (stack.length) {
      currV = stack.pop();
      res.push(currV);
      this.adjList[currV].forEach(x => {
        if (!visited[x]) {
          stack.push(x);
          visited[x] = true;
        }
      })
      
    }
    return res;
  }

  bfs(vertex) {
    if (!this.adjList[vertex]) return;

    const res = [];
    const queue = [vertex];
    const visited = {};
    let currV;

    visited[vertex] = true;

    while (queue.length) {
      currV = queue.shift();
      res.push(currV);
      this.adjList[currV].forEach(x => {
        if (!visited[x]) {
          queue.push(x);
          visited[x] = true;
        }
      })
      
    }
    return res;
  }
}

module.exports = {
  Graph,
}