const merge = (arr1, arr2) => {
  const res = []
  let i = 0;
  let j = 0;

  while (i < arr1.length && j < arr2.length) {
    if (arr1[i] < arr2[j]) {
      res.push(arr1[i]);
      i++;
    } else {
      res.push(arr2[j]);
      j++;
    }
  }

  while (i < arr1.length) {
    res.push(arr1[i]);
    i++;
  }
  while (j < arr2.length) {
    res.push(arr2[j]);
    j++;
  }

  return res;
}

const mergeSort = (arr) => {
  if (arr.length <= 1) return arr;
  const mid = Math.floor(arr.length / 2)
  const left = mergeSort(arr.slice(0, mid))
  const right = mergeSort(arr.slice(mid))
  return merge(left, right)
}

const swap = (arr, i, j) => ([arr[j], arr[i]] = [arr[i], arr[j]]);

const pivot = (arr, start = 0, end = arr.length + 1) => {
  const pivot = arr[start];
  let swapIdx = start;

  for (let i = start + 1; i <= end; i++) {
    if (pivot > arr[i]) {
      swapIdx++;
      swap(arr, swapIdx, i);
    }
  }
  swap(arr, start, swapIdx);
  return swapIdx;
};

const quickSort = (arr, left = 0, right = arr.length - 1) => {

  if (left < right) {
    const pivotIdx = pivot(arr, left, right)
    quickSort(arr, left, pivotIdx - 1)
    quickSort(arr, pivotIdx + 1, right)
  };
  return arr;
}

// radix sort

const getDigit = (num, place) =>
  Math.floor(Math.abs(num) / Math.pow(10, place)) % 10;

const digitCount = (num) => {
  if (num === 0) return 1;
  return Math.floor(Math.log10(Math.abs(num))) + 1;
}

const mostDigits = nums => {
  let maxDigits = 0;

  for (let i = 0; i < nums.length; i++) {
    maxDigits = Math.max(maxDigits, digitCount(nums[i]));
  }

  return maxDigits;
}

const radixSort = (arr) => {
  const maxDigits = mostDigits(arr);
  let res = [];

  for (let i = 0; i < maxDigits; i++) {
    const buckets = Array.from({length: 10}, () => []);
    for (let j = 0; j < arr.length; j++) {
      const d = getDigit(arr[j], i);
      buckets[d].push(arr[j]);
    }
    res = [].concat(...buckets);
  }

  return res;
}

module.exports = {
  merge,
  mergeSort,
  pivot,
  quickSort,
  digitCount,
  mostDigits,
  radixSort,
}