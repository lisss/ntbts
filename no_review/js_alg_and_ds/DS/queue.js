class Node {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

class Queue {
  constructor() {
    this.first = null;
    this.last = null;
    this.size = 0;
  }

  enqueue(val) {
    const node = new Node(val);

    if(!this.first) {
      this.first = node;
      this.last = node;
    } else {
      this.last.next = node;
      this.last = node;
    }

    return ++this.size;
  }

  dequeue() {
    if (!this.size) return null;
    const toRemove = this.first;

    if (this.size === 1) {
      this.last = null;
    }

    this.first = toRemove.next;
    this.size--;

    return toRemove.val;
  }
}

module.exports = {
  Queue,
}