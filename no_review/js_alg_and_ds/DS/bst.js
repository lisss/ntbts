class Node {
  constructor(val) {
    this.val = val;
    this.left = null;
    this.right = null;
  }
}

class BST {
  constructor() {
    this.root = null;
  }

  insert(val) {
    const node = new Node(val);
    if (!this.root) {
      this.root = node;
      return this;
    }
    
    let curr = this.root;
    while (true) {
      if (curr.val === val) return;
      if (val > curr.val) {
        if (curr.right) {
          curr = curr.right;
        } else {
          curr.right = node;
          return this;
        }
      } else {
        if (curr.left) {
          curr = curr.left;
        } else {
          curr.left = node;
          return this;
        }
      }
    }
  }

  find(val) {
    if (!this.root) {
      return false;
    }

    let curr = this.root;
    let found = false;
    while (curr && !found) {
      if (val === curr.val) return true;
      if (val > curr.val) {
        curr = curr.right;
      } else {
        curr = curr.left;
      }
    }

    return false;
  }

  bfs() {
    const queue = []
    const res = []
    let curr = this.root

    queue.push(curr);

    while (queue.length) {
      curr = queue.shift();
      res.push(curr.val);
      if (curr.left) {
        queue.push(curr.left)
      }
      if (curr.right) {
        queue.push(curr.right)
      }
    }

    return res
  }

  dfsPre() {
    const res = [];

    const _do = (node) => {
      res.push(node.val);
      if (node.left) _do(node.left);
      if (node.right) _do(node.right);
    }

    _do(this.root);
    return res;
  }

  dfsPost() {
    const res = [];

    const _do = (node) => {
      if (node.left) _do(node.left);
      if (node.right) _do(node.right);
      res.push(node.val);
    }

    _do(this.root);
    return res;
  }

  dfsIn() {
    const res = [];

    const _do = (node) => {
      if (node.left) _do(node.left);
      res.push(node.val);
      if (node.right) _do(node.right);
    }

    _do(this.root);
    return res;
  }
}

module.exports = {
  BST,
}