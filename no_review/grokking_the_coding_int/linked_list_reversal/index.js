class Node {
  constructor(val, next) {
    this.val = val;
    this.next = next;
  }

  print() {
    let temp = this;
    while (temp) {
      process.stdout.write(`${temp.val} `);
      temp = temp.next;
    }
    console.log();
  }
}

// Reverse a LinkedList (easy)
const reverse = (head) => {
  let [curr, prev] = [head, null];

  while (curr) {
    let next = curr.next;
    curr.next = prev;
    prev = curr;
    curr = next;
  }

  return prev;
};

const reverseSubList = (head, p, q) => {
  if (p === q) {
    return head;
  }

  let [curr, prev] = [head, null];
  let i = 0;

  while (curr && i < p - 1) {
    prev = curr;
    curr = curr.next;
    i++;
  }

  let lastNodeFirstPart = prev;
  let lastNodeSublist = curr;

  i = 0;

  while (curr && i < q - p + 1) {
    const next = curr.next;
    curr.next = prev;
    prev = curr;
    curr = next;
    i++;
  }

  if (lastNodeFirstPart) {
    lastNodeFirstPart.next = prev;
  } else {
    head = prev;
  }

  lastNodeSublist.next = curr;

  return head;
};

const reverseEveryKElements = (head, k) => {
  if (k <= 1 || !head) {
    return head;
  }

  let [curr, prev] = [head, null];

  while (curr) {
    let lastNodeFirstPart = prev;
    let lastNodeSublist = curr;

    let i = 0;

    while (curr && i < k) {
      const next = curr.next;
      curr.next = prev;
      prev = curr;
      curr = next;
      i++;
    }

    if (lastNodeFirstPart) {
      lastNodeFirstPart.next = prev;
    } else {
      head = prev;
    }

    lastNodeSublist.next = curr;
    prev = lastNodeSublist;
  }

  return head;
};

const reverseEveryKAlternateElements = (head, k) => {
  if (k <= 1 || !head) {
    return head;
  }

  let [curr, prev] = [head, null];

  while (curr) {
    let lastNodeFirstPart = prev;
    let lastNodeSublist = curr;

    let i = 0;

    while (curr && i < k) {
      const next = curr.next;
      curr.next = prev;
      prev = curr;
      curr = next;
      i++;
    }

    if (lastNodeFirstPart) {
      lastNodeFirstPart.next = prev;
    } else {
      head = prev;
    }

    lastNodeSublist.next = curr;
    prev = lastNodeSublist;

    while (curr && i) {
      prev = curr;
      curr = curr.next;
      i--;
    }
  }

  return head;
};

const head = new Node(1);
head.next = new Node(2);
head.next.next = new Node(3);
head.next.next.next = new Node(4);
head.next.next.next.next = new Node(5);
head.next.next.next.next.next = new Node(6);
head.next.next.next.next.next.next = new Node(7);
head.next.next.next.next.next.next.next = new Node(8);

process.stdout.write("Nodes of original LinkedList are: ");
head.print();
const result = reverseEveryKAlternateElements(head, 2);
process.stdout.write("Nodes of reversed LinkedList are: ");
result.print();
