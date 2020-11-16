class Node {
  constructor(head, next = null) {
    this.head = head;
    this.next = next;
  }
}

const has_cycle = (head) => {
  let fast = head,
    slow = head;
  while (fast && fast.next) {
    fast = fast.next.next;
    slow = slow.next;
    if (fast === slow) {
      return true;
    }
  }
  return false;
};

const find_cycle_length = (head) => {
  let fast = head,
    slow = head;
  while (fast && fast.next) {
    fast = fast.next.next;
    slow = slow.next;
    if (fast === slow) {
      return calculateCycleLen(slow);
    }
  }
  return 0;
};

const calculateCycleLen = (slow) => {
  let current = slow;
  let len = 0;

  while (true) {
    current = current.next;
    len += 1;
    if (current === slow) {
      break;
    }
  }

  return len;
};

const main = () => {
  const head = new Node(1);
  head.next = new Node(2);
  head.next.next = new Node(3);
  head.next.next.next = new Node(4);
  head.next.next.next.next = new Node(5);
  head.next.next.next.next.next = new Node(6);
  head.next.next.next.next.next.next = head.next.next;
  console.log(`LinkedList cycle length: ${find_cycle_length(head)}`);

  head.next.next.next.next.next.next = head.next.next.next;
  console.log(`LinkedList cycle length: ${find_cycle_length(head)}`);
};

main();
