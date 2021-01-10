const Deque = require("collections/deque");

const printOrders = (tasks, prerequisites) => {
  const sortedOrders = [];

  if (!tasks) {
    return;
  }

  const inDegree = new Array(tasks).fill(0);
  const graph = new Array(tasks).fill(0).map(() => new Array());

  prerequisites.forEach(([u, v]) => {
    graph[u].push(v);
    inDegree[v]++;
  });

  const sources = [];

  for (let i = 0; i < inDegree.length; i++) {
    if (inDegree[i] === 0) {
      sources.push(i);
    }
  }

  const _doPrint = (graph, inDegree, sources, sortedOrders) => {
    sources.forEach((vertex) => {
      sortedOrders.push(vertex);
      const sourcesForNextCall = [...sources];
      sourcesForNextCall.splice(sourcesForNextCall.indexOf(vertex), 1);

      graph[vertex].forEach((child) => {
        inDegree[child]--;
        if (inDegree[child] === 0) {
          sourcesForNextCall.push(child);
        }
      });

      _doPrint(graph, inDegree, sourcesForNextCall, sortedOrders);

      sortedOrders.splice(sortedOrders.indexOf(vertex), 1);
      graph[vertex].forEach((child) => {
        inDegree[child]++;
      });
    });
    if (sortedOrders.length === tasks) {
      console.log(sortedOrders);
    }
  };

  _doPrint(graph, inDegree, sources, sortedOrders);

  console.log();
};

const findOrder = (words) => {
  if (!words.length) {
    return "";
  }

  const inDegree = {};
  const graph = {};

  words.forEach((word) => {
    for (const char of word) {
      graph[char] = [];
      inDegree[char] = 0;
    }
  });

  for (let i = 0; i < words.length - 1; i++) {
    const [w1, w2] = [words[i], words[i + 1]];

    for (let j = 0; j < Math.min(w1.length, w2.length); j++) {
      const [parent, child] = [w1[j], w2[j]];
      if (parent !== child) {
        graph[parent].push(child);
        inDegree[child]++;
        break;
      }
    }
  }

  const sources = new Deque();
  const sorderOrder = [];

  Object.keys(inDegree).forEach((k) => {
    if (inDegree[k] === 0) {
      sources.push(k);
    }
  });

  while (sources.length) {
    const vertex = sources.shift();
    sorderOrder.push(vertex);

    graph[vertex].forEach((child) => {
      inDegree[child]--;
      if (inDegree[child] === 0) {
        sources.push(child);
      }
    });
  }

  if (sorderOrder.length !== Object.keys(inDegree).length) {
    return "";
  }

  return sorderOrder.join("");
};

const findTrees = (nodes, edges) => {
  if (!nodes) {
    return [];
  }
  const inDegree = {};
  const graph = {};

  for (let i = 0; i < nodes; i++) {
    graph[i] = [];
    inDegree[i] = 0;
  }

  edges.forEach(([u, v]) => {
    graph[u].push(v);
    graph[v].push(u);
    inDegree[u]++;
    inDegree[v]++;
  });

  leaves = new Deque();
  Object.keys(inDegree).forEach((k) => {
    if (inDegree[k] === 1) {
      leaves.push(k);
    }
  });

  let totalNodes = nodes;
  while (totalNodes > 2) {
    const leavesSize = leaves.length;
    totalNodes -= leavesSize;
    for (let i = 0; i < leavesSize; i++) {
      const vertex = leaves.shift();

      graph[vertex].forEach((child) => {
        inDegree[child]--;
        if (inDegree[child] === 1) {
          leaves.push(child);
        }
      });
    }
  }

  return leaves.toArray();
};

console.log(
  `Roots of MHTs: ${findTrees(5, [
    [0, 1],
    [1, 2],
    [1, 3],
    [2, 4],
  ])}`
);
console.log(
  `Roots of MHTs: ${findTrees(4, [
    [0, 1],
    [0, 2],
    [2, 3],
  ])}`
);
console.log(
  `Roots of MHTs: ${findTrees(4, [
    [1, 2],
    [1, 3],
  ])}`
);
