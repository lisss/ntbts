class NodeS {
  constructor(val) {
    this.val = val;
    this.next = null;
  }
}

class NodeD {
  constructor(val) {
    this.val = val;
    this.next = null;
    this.prev = null;
  }
}

class LinkedList {
  constructor() {
    this.head = null;
  }

  print() {
    const res = [];
    let curr = this.head;

    while (curr) {
      res.push(curr.val);
      curr = curr.next;
    }
    console.log(res.join(' - '))
  }
}

class SingleLinkedList extends LinkedList {
  constructor() {
    super();
    this.head = null;
    this.tail = null;
    this.length = 0;
  }

  push(val) {
    const node = new NodeS(val);

    if (!this.head) {
      this.head = node;
      this.tail = node;
    } else {
      this.tail.next = node;
      this.tail = node;
    }

    this.length++;

    return this;
  }

  pop() {
    if (!this.head) {
      return;
    }

    let curr = this.head;
    let newTail = curr;

    while (curr.next) {
      newTail = curr;
      curr = curr.next;
    }
    this.tail = newTail;
    newTail.next = null;
    this.length--;

    if (!this.length) {
      this.head = null;
      this.tail = null;
    }
    return curr;
  }

  shift() {
    if (!this.head) {
      return;
    }

    const pre = this.head;
    this.head = pre.next;
    this.length--;

    if (!this.length) {
      this.tail = null;
    }

    return pre;
  }

  unshift(val) {
    const node = new NodeS(val);

    if (!this.head) {
      this.head = node;
      this.tail = node;
    } else {
      node.next = this.head;
      this.head = node;
    }
    this.length++;
    return this;
  }

  get(ind) {
    if (ind < 0 || ind >= this.length) {
      return null;
    }
    let count = 0;
    let curr = this.head;

    while (count < ind) {
      curr = curr.next;
      count++;
    }

    return curr;
  }
  
  set(ind, val) {
    const node = this.get(ind);
    if (!node) return false;
    node.val = val;
    return true;
  }

  insert(ind, val) {
    if (ind < 0 || ind > this.length) return false;
    if (ind === this.length) return !!this.push(val);
    if (ind === 0) return !!this.unshift(val);

    const prev = this.get(ind - 1);
    if (!prev) return false;
    let newNode = new NodeS(val);
    let temp = prev.next;
    prev.next = newNode;
    newNode.next = temp;
    this.length++;

    return true;
  }

  remove(ind) {
    if (ind < 0 || ind >= this.length) return;
    if (ind === this.length - 1) return this.pop();
    if (ind === 0) return this.shift();

    const prev = this.get(ind - 1);
    if (!prev) return false;
    let removed = prev.next;
    prev.next = removed.next;
    this.length--;

    return removed;
  }

  reverse() {
    let curr = this.head;
    [this.head, this.tail] = [this.tail, this.head]

    let prev = null;
    let next = null;

    while (curr) {
      next = curr.next;
      curr.next = prev;
      prev = curr;
      curr = next;
    }
  }
}

class DoublyLinkedList extends LinkedList {
  constructor() {
      super();
      this.head = null;
      this.tail = null;
      this.length = 0;
  }

  push(val) {
     const node = new NodeD(val);

     if (!this.head) {
       this.head = node;
       this.tail = node;
     } else {
       node.prev = this.tail;
       this.tail.next = node;
       this.tail = node;
     }

     this.length++;
     return this;
  }

  pop() {
    if (!this.head) {
      return;
    }

    const oldTail = this.tail;

    if (this.length === 1) {
      this.head = null;
      this.tail = null;
    } else {
      this.tail = oldTail.prev;
      this.tail.next = null;
      oldTail.prev = null;
    }

    this.length--;

    return oldTail;
  }

  shift() {
    if (!this.head) {
      return;
    }

    const pre = this.head;

    if (this.length === 1) {
      this.head = null;
      this.tail = null;
    } else {
      this.head = pre.next;
      this.head.prev = null;
      pre.next = null;
    }

    this.length--;
    return pre;
  }

  unshift(val) {
    const node = new NodeD(val);

    if (!this.head) {
      this.head = node;
      this.tail = node;
    } else {
      this.head.prev = node;
      node.next = this.head;
      this.head = node;
    }
    this.length++;
    return this;
  }

  get(ind) {
    if (ind < 0 || ind >= this.length) {
      return null;
    }

    const mid = this.length / 2;
    let curr;

    if (ind <= mid) {
      let count = 0;
      curr = this.head;

      while (count !== ind) {
        curr = curr.next;
        count++;
      }
    } else {
      let count = this.length - 1;
      curr = this.tail;

      while (count !== ind) {
        curr = curr.prev;
        count--;
      }
    }

    return curr;
  }

  set(ind, val) {
    const node = this.get(ind);
    if (!node) return false;
    node.val = val;
    return true;
  }

  insert(ind, val) {
    if (ind < 0 || ind > this.length) return false;
    if (ind === this.length) return !!this.push(val);
    if (ind === 0) return !!this.unshift(val);

    const beforeNode = this.get(ind - 1);
    if (!beforeNode) return false;

    let newNode = new NodeD(val);
    let afterNode = beforeNode.next;

    beforeNode.next = newNode;
    newNode.prev = beforeNode;
    newNode.next = afterNode;
    afterNode.prev = newNode;

    this.length++;
    return true;
  }

  remove(ind) {
    if (ind < 0 || ind >= this.length) return;
    if (ind === this.length - 1) return this.pop();
    if (ind === 0) return this.shift();

    const removed = this.get(ind);
    if (!removed) return false;
  
    let afterNode = removed.next;
    let beforeNode = removed.prev
    beforeNode.next = afterNode;
    afterNode.prev = beforeNode;
    removed.prev = null;
    removed.next = null;

    this.length--;
    return removed;
  }

  reverse() {
    let temp = null;
    let current = this.head;
      
    while(current){
      temp = current.prev;
      current.prev = current.next;
      current.next = temp;
      current = current.prev;
    }
    
    if (temp != null) { 
      this.head = temp.prev; 
    }
    return this;
  }
}


module.exports = {
  SingleLinkedList,
  DoublyLinkedList,
}