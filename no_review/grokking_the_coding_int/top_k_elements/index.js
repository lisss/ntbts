const Heap = require("collections/heap");

class Point {
  constructor(x, y) {
    this.x = x;
    this.y = y;
  }

  getPoint() {
    return "[" + this.x + ", " + this.y + "] ";
  }
}

const findKLargestNumbers = (nums, k) => {
  const minHeap = new Heap([], null, (a, b) => b - a);

  for (let i = 0; i < k; i++) {
    minHeap.push(nums[i]);
  }

  for (let i = k; i < nums.length; i++) {
    if (nums[i] > minHeap.peek()) {
      minHeap.pop();
      minHeap.push(nums[i]);
    }
  }

  return minHeap.toArray();
};

const findKthSmallestNumber = (nums, k) => {
  const maxHeap = new Heap();

  for (let i = 0; i < k; i++) {
    maxHeap.push(nums[i]);
  }

  for (let i = k; i < nums.length; i++) {
    if (nums[i] < maxHeap.peek()) {
      maxHeap.pop();
      maxHeap.push(nums[i]);
    }
  }

  return maxHeap.pop();
};

const findClosestPoints = (points, k) => {
  const _getEuclideanDistance = ({ x, y }) => Math.sqrt(x ** 2 + y ** 2);
  const minHeap = new Heap(
    [],
    null,
    (a, b) => _getEuclideanDistance(a) - _getEuclideanDistance(b)
  );

  for (let i = 0; i < k; i++) {
    minHeap.push(points[i]);
  }

  for (let i = k; i < points.length; i++) {
    const di = _getEuclideanDistance(points[i]);
    const dm = _getEuclideanDistance(minHeap.peek());
    if (di < dm) {
      minHeap.pop();
      minHeap.push(points[i]);
    }
  }

  return minHeap.toArray();
};

module.exports = {
  Point,
  findKLargestNumbers,
  findKthSmallestNumber,
  findClosestPoints,
};
