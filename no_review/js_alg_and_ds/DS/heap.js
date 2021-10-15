class MaxBinaryHeap {
  constructor() {
    this.values = []
  }

  insert(val) {
    this.values.push(val);
    let currIdx = this.values.length - 1;

    while (currIdx > 0) {
      const parentIdx = Math.floor((currIdx - 1) / 2);
      const curr = this.values[currIdx];
      const parent = this.values[parentIdx];

      if (curr <= parent) break;

      [this.values[parentIdx], this.values[currIdx]] = [curr, parent];
      currIdx = parentIdx;
    }

    return this;
  }

  extractMax() {
    if (!this.values.length) return null;

    const max = this.values[0];
    const parent = this.values.pop()
    const len = this.values.length;
    if (!len) return max;
    
    this.values[0] = parent;
    let idx = 0;

    while (true) {
      const leftIdx = idx * 2 + 1;
      const rightIdx = idx * 2 + 2;

      let left, right;
      let swap = null;

      if (leftIdx < len) {
        left = this.values[leftIdx];
        if (left > parent) {
          swap = leftIdx;
        }
      }

      if (rightIdx < len) {
        right = this.values[rightIdx];
        if ((swap === null && right > parent) || (swap !== null && right > left)) {
          swap = rightIdx;
        }
      }

      if (swap === null) break;
      this.values[idx] = this.values[swap];
      this.values[swap] = parent;
      idx = swap;
    }

    return max;
  }
}

class Node {
  constructor(val, priority) {
    this.priority = priority;
    this.value = val;
  }
}

class PriorityQueue {
  constructor() {
    this.values = []
  }

  enqueue(val, priority) {
    const node = new Node(val, priority);
    this.values.push(node);
    let currIdx = this.values.length - 1;
    const elem = this.values[currIdx]

    while (currIdx > 0) {
      const parentIdx = Math.floor((currIdx - 1) / 2);
      const parent = this.values[parentIdx];

      if (elem.priority >= parent.priority) break;

      this.values[parentIdx] = elem;
      this.values[currIdx] = parent;
      currIdx = parentIdx;
    }

    return this;
  }

  dequeue() {
    if (!this.values.length) return null;

    const top = this.values[0];
    const parent = this.values.pop()
    const len = this.values.length;
    if (!len) return top;
    
    this.values[0] = parent;
    let idx = 0;

    while (true) {
      const leftIdx = idx * 2 + 1;
      const rightIdx = idx * 2 + 2;

      let left, right;
      let swap = null;
      const parentPrio = parent.priority

      if (leftIdx < len) {
        left = this.values[leftIdx].priority;
        if (left < parentPrio) {
          swap = leftIdx;
        }
      }

      if (rightIdx < len) {
        right = this.values[rightIdx].priority;
        if ((swap === null && right < parentPrio) || (swap !== null && right < left)) {
          swap = rightIdx;
        }
      }

      if (swap === null) break;
      this.values[idx] = this.values[swap];
      this.values[swap] = parent;
      idx = swap;
    }

    return top;
  }
}

module.exports = {
  MaxBinaryHeap,
  PriorityQueue,
}