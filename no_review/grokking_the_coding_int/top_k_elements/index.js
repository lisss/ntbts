const Heap = require("collections/heap");
const Deque = require("collections/deque");

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

const minimumCostToConnectRopes = (ropeLengths) => {
  const minHeap = new Heap([], null, (a, b) => b - a);

  ropeLengths.forEach((x) => minHeap.push(x));
  let maxLen = 0;

  while (minHeap.length > 1) {
    const fst = minHeap.pop();
    const snd = minHeap.pop();
    const sum = fst + snd;
    maxLen += sum;
    minHeap.push(sum);
  }

  return maxLen;
};

const findKFrequentNumbers = (nums, k) => {
  topNumbers = [];
  const minHeap = new Heap([], null, (a, b) => b[0] - a[0]);

  const freqMap = {};

  nums.forEach((x) => {
    if (!(x in freqMap)) {
      freqMap[x] = 0;
    }
    freqMap[x] += 1;
  });

  Object.keys(freqMap).forEach((x) => {
    minHeap.push([freqMap[x], x]);
    if (minHeap.length > k) {
      minHeap.pop();
    }
  });

  while (minHeap.length) {
    topNumbers.push(minHeap.pop()[1]);
  }

  return topNumbers;
};

const sortCharacterByFrequency = (str) => {
  const freqMap = {};
  const minHeap = new Heap([], null, (a, b) => a[0] - b[0]);
  let res = "";

  for (let i = 0; i < str.length; i++) {
    const x = str[i];
    if (!(x in freqMap)) {
      freqMap[x] = 0;
    }
    freqMap[x] += 1;
  }

  Object.keys(freqMap).forEach((x) => minHeap.push([freqMap[x], x]));

  while (minHeap.length) {
    const [freq, char] = minHeap.pop();
    for (let i = 0; i < freq; i++) {
      res += char;
    }
  }

  return res;
};

class KthLargestNumberInStream {
  constructor(nums, k) {
    this.k = k;
    this.minHeap = new Heap([], null, (a, b) => b - a);

    nums.forEach((x) => this.add(x));
  }

  add(num) {
    this.minHeap.push(num);
    if (this.minHeap.length > this.k) {
      this.minHeap.pop();
    }
    return this.minHeap.peek();
  }
}

// 'K' Closest Numbers (medium)

const binarySearch = (arr, target) => {
  let left = 0,
    right = arr.length - 1;

  while (left <= right) {
    const mid = Math.floor(left + (right - left) / 2);
    const midNum = arr[mid];
    if (midNum === target) {
      return mid;
    }

    if (midNum < target) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }

  if (left > 0) {
    return left - 1;
  }
  return left;
};

const findClosestElements = (arr, K, X) => {
  const result = [];
  const heap = new Heap([], null, (a, b) => b[0] - a[0]);

  const y = binarySearch(arr, X);

  const low = Math.max(y - K, 0);
  const high = Math.min(y + K, arr.length - 1);

  for (let i = low; i <= high; i++) {
    heap.push([Math.abs(arr[i] - X), arr[i]]);
  }

  for (i = 0; i < K; i++) {
    result.push(heap.pop()[1]);
  }

  return result.sort();
};

const findClosestElements2 = (arr, K, X) => {
  const result = Deque();
  const y = binarySearch(arr, X);

  let left = y,
    right = y + 1,
    n = arr.length;

  for (let i = 0; i < K; i++) {
    if (left >= 0 && right < n) {
      const dLeft = Math.abs(arr[left] - X);
      const dRight = Math.abs(arr[right] - X);

      if (dLeft <= dRight) {
        result.unshift(arr[left]);
        left--;
      } else {
        result.push(arr[right]);
        right++;
      }
    } else if (left >= 0) {
      result.unshift(arr[left]);
      left--;
    } else if (right < n) {
      result.push(arr[right]);
      right++;
    }
  }

  return result.toArray();
};
// ---

const findMaximumDistinctElements = (nums, k) => {
  const freqMap = {};
  const minHeap = new Heap([], null, (a, b) => b - a);
  let distinct = 0;

  if (nums.length <= k) return 0;

  nums.forEach((x) => {
    if (!(x in freqMap)) {
      freqMap[x] = 0;
    }
    freqMap[x]++;
  });

  Object.keys(freqMap).forEach((x) => {
    if (freqMap[x] > 1) {
      minHeap.push(freqMap[x]);
    } else {
      distinct++;
    }
  });

  while (k && minHeap.length) {
    const freq = minHeap.pop();
    k -= freq - 1;
    if (k >= 0) {
      distinct++;
    }
  }

  if (k > 0) {
    distinct -= k;
  }

  return distinct;
};

// Sum of Elements (medium)
const findSumOfElements = (nums, k1, k2) => {
  let sum = 0;
  const heap = Heap(nums, null, (a, b) => b - a);

  for (let i = 0; i < k1; i++) {
    heap.pop();
  }

  for (let i = k1; i < k2 - 1; i++) {
    sum += heap.pop();
  }

  return sum;
};

function findSumOfElements2(nums, k1, k2) {
  const maxHeap = new Heap();
  // keep smallest k2 numbers in the max heap
  for (i = 0; i < nums.length; i++) {
    if (i < k2 - 1) {
      maxHeap.push(nums[i]);
    } else if (nums[i] < maxHeap.peek()) {
      // as we are interested only in the smallest k2 numbers
      maxHeap.pop();
      maxHeap.push(nums[i]);
    }
  }

  // get the sum of numbers between k1 and k2 indices
  // these numbers will be at the top of the max heap
  let elementSum = 0;
  for (i = 0; i < k2 - k1 - 1; i++) {
    elementSum += maxHeap.pop();
  }

  return elementSum;
}

// ----

const rearrangeString = (str) => {
  const freqMap = {};
  const heap = Heap([], null, (a, b) => a[0] - b[0]);
  res = [];

  for (i = 0; i < str.length; i++) {
    if (!(str[i] in freqMap)) {
      freqMap[str[i]] = 0;
    }
    freqMap[str[i]]++;
  }

  Object.keys(freqMap).forEach((x) => heap.push([freqMap[x], x]));

  while (heap.length) {
    const [_, ch] = heap.pop();
    res.push(ch);
    if (res.length > 1) {
      const prev = res[res.length - 2];
      freqMap[prev]--;

      if (freqMap[prev]) {
        heap.push([freqMap[prev], prev]);
      }
    }
  }

  return res.length === str.length ? res.join("") : "";
};

const reorganizeString = (str, k) => {
  const freqMap = {};
  const heap = Heap([], null, (a, b) => a[0] - b[0]);
  res = [];

  for (i = 0; i < str.length; i++) {
    if (!(str[i] in freqMap)) {
      freqMap[str[i]] = 0;
    }
    freqMap[str[i]]++;
  }

  Object.keys(freqMap).forEach((x) => heap.push([freqMap[x], x]));

  while (heap.length) {
    const [_, ch] = heap.pop();
    res.push(ch);
    if (res.length >= k) {
      const prev = res[res.length - k];
      freqMap[prev]--;

      if (freqMap[prev]) {
        heap.push([freqMap[prev], prev]);
      }
    }
  }

  return res.length === str.length ? res.join("") : "";
};

const scheduleTasks = (tasks, k) => {
  let intervalCount = 0;
  const freqMap = {};
  const heap = Heap([], null, (a, b) => a[0] - b[0]);

  tasks.forEach((t) => {
    if (!(t in freqMap)) {
      freqMap[t] = 0;
    }
    freqMap[t]++;
  });

  Object.keys(freqMap).forEach((x) => heap.push([freqMap[x], x]));

  while (heap.length) {
    const waitList = [];
    let n = k + 1;

    while (n && heap.length) {
      intervalCount++;
      const [freq, ch] = heap.pop();
      if (freq > 1) {
        waitList.push([freq - 1, ch]);
      }
      n--;
    }
    waitList.forEach((x) => heap.push(x));

    if (heap.length) {
      intervalCount += n;
    }
  }

  return intervalCount;
};

class Elem {
  constructor(num, freq, seq) {
    this.num = num;
    this.freq = freq;
    this.seq = seq;
  }

  compare(other) {
    if (this.freq !== other.freq) {
      return this.freq - other.freq;
    }
    return this.seq - other.seq;
  }
}

class FrequencyStack {
  constructor() {
    this.heap = Heap([], null, (a, b) => a.compare(b));
    this.freqMap = {};
    this.seq = 0;
  }

  push(num) {
    if (!(num in this.freqMap)) {
      this.freqMap[num] = 0;
    }
    this.freqMap[num]++;
    this.heap.push(new Elem(num, this.freqMap[num], this.seq));
    this.seq++;
  }

  pop() {
    if (!this.heap.length) {
      return -1;
    }

    const num = this.heap.pop().num;
    if (this.freqMap[num] > 1) {
      this.freqMap[num]--;
    } else {
      delete this.freqMap[num];
    }
    return num;
  }
}

module.exports = {
  Point,
  KthLargestNumberInStream,
  FrequencyStack,
  findKLargestNumbers,
  findKthSmallestNumber,
  findClosestPoints,
  minimumCostToConnectRopes,
  findKFrequentNumbers,
  sortCharacterByFrequency,
  findClosestElements,
  findClosestElements2,
  findMaximumDistinctElements,
  findSumOfElements,
  rearrangeString,
  reorganizeString,
  scheduleTasks,
};
