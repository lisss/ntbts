class Node {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

class Stack {
  constructor() {
    this.first = null;
    this.last = null;
    this.size = 0;
  }

  push(val) {
    const node = new Node(val);

    if(!this.first) {
      this.first = node;
      this.last = node;
    } else {
      node.next = this.first;
      this.first = node;
    }

    return ++this.size;
  }

  pop() {
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
  Stack,
}