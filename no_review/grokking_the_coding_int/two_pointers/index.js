// 1. Pair with Target Sum (easy)

const pair_with_targetsum = (arr, targetSum) => {
  let start = 0;
  let end = arr.length - 1;

  while (start !== end) {
    const sum = arr[start] + arr[end];

    if (sum === targetSum) {
      return [start, end];
    } else if (sum > targetSum) {
      end -= 1;
    } else {
      start += 1;
    }
  }
  return [-1, -1];
};

// 2. Remove Duplicates (easy)
const remove_duplicates = (arr) => {
  let nextNonDup = 1,
    i = 1;

  while (i < arr.length) {
    if (arr[nextNonDup - 1] !== arr[i]) {
      arr[nextNonDup] = arr[i];
      nextNonDup += 1;
    }
    i += 1;
  }
  return nextNonDup;
};

const remove_elem = (arr, key) => {
  let nextElem = 0;

  arr.forEach((x) => {
    if (x != key) {
      arr[nextElem] = x;
      nextElem += 1;
    }
  });

  return nextElem;
};

// 3. Squaring a Sorted Array (easy)
const make_squares = (arr) => {
  const n = arr.length;
  const squares = new Array(n);

  let left = 0;
  let right = n - 1;
  let maxSqNum = n - 1;

  while (left <= right) {
    const sqLeft = arr[left] ** 2;
    const sqRight = arr[right] ** 2;

    if (sqLeft > sqRight) {
      squares[maxSqNum] = sqLeft;
      left += 1;
    } else {
      squares[maxSqNum] = sqRight;
      right -= 1;
    }
    maxSqNum -= 1;
  }

  return squares;
};

const search_triplets = (arr) => {
  arr.sort((a, b) => a - b);
  const triplets = [];

  for (let i = 0; i < arr.length; i++) {
    if (i > 0 && arr[i] == arr[i - 1]) {
      continue;
    }
    searchPair(arr, -arr[i], i + 1, triplets);
  }

  return triplets;
};

const searchPair = (arr, targetSum, start, triplets) => {
  let end = arr.length - 1;

  while (start < end) {
    const currSum = arr[start] + arr[end];
    if (currSum === targetSum) {
      triplets.push([-targetSum, arr[start], arr[end]]);
      start += 1;
      end -= 1;

      while (start < end && arr[start] === arr[start - 1]) {
        start += 1;
      }
      while (start < end && arr[end] === arr[end + 1]) {
        end -= 1;
      }
    } else if (currSum < targetSum) {
      start += 1;
    } else {
      end -= 1;
    }
  }
};

const triplet_sum_close_to_target = (arr, targetSum) => {
  arr.sort((a, b) => a - b);

  let smallestDiff = Infinity;

  for (let i = 0; i < arr.length - 2; i++) {
    let left = i + 1;
    let right = arr.length - 1;

    while (left < right) {
      const targetDiff = targetSum - arr[i] - arr[left] - arr[right];

      if (targetDiff === 0) {
        return targetSum;
      }

      if (
        Math.abs(targetDiff) < Math.abs(smallestDiff) ||
        (Math.abs(targetDiff) === Math.abs(smallestDiff) &&
          targetDiff > smallestDiff)
      ) {
        smallestDiff = targetDiff;
      }

      if (smallestDiff > 0) {
        left += 1;
      } else {
        right -= 1;
      }
    }
  }

  return targetSum - smallestDiff;
};

const triplet_with_smaller_sum = (arr, targetSum) => {
  const inner = (arr, start, target) => {
    let count = 0,
      left = start + 1,
      right = arr.length - 1;

    while (left < right) {
      if (arr[left] + arr[right] < target) {
        count += right - left;
        left += 1;
      } else {
        right -= 1;
      }
    }

    return count;
  };

  arr.sort((a, b) => a - b);

  return arr.reduce((c, p, i) => c + inner(arr, i, targetSum - p), 0);
};

// Subarrays with Product Less than a Target (medium)
const find_subarrays = (arr, target) => {
  const result = [];
  let product = 1;
  let left = 0;

  for (let i = 0; i < arr.length; i++) {
    product *= arr[i];

    while (product >= target && left < arr.length) {
      product /= arr[left];
      left += 1;
    }

    const tempArr = [];
    for (let j = i; j > left - 1; j--) {
      tempArr.unshift(arr[j]);
      const t = tempArr.concat();
      result.push(t);
    }
  }

  return result;
};

const dutch_flag_sort = (arr) => {
  let low = 0,
    high = arr.length - 1,
    i = 0;

  while (i <= high) {
    if (arr[i] === 0) {
      const tmp = arr[low];
      arr[low] = arr[i];
      arr[i] = tmp;
      low += 1;
      i += 1;
    } else if (arr[i] === 1) {
      i += 1;
    } else {
      const tmp = arr[high];
      arr[high] = arr[i];
      arr[i] = tmp;
      high -= 1;
    }
  }

  return arr;
};

const search_quadruplets = (arr, target) => {
  const quadrs = [];
  arr.sort((a, b) => a - b);

  for (let i = 0; i < arr.length - 3; i++) {
    if (i > 0 && arr[i] === arr[i - 1]) {
      continue;
    }

    for (let j = i + 1; j < arr.length - 2; j++) {
      if (j > i + 1 && arr[j] === arr[j - 1]) {
        continue;
      }
      searchPairQ(arr, target, i, j, quadrs);
    }
  }

  return quadrs;
};

const searchPairQ = (arr, target, fst, snd, quadrs) => {
  let left = snd + 1;
  let right = arr.length - 1;

  while (left < right) {
    const currSum = arr[left] + arr[right] + arr[fst] + arr[snd];
    if (currSum === target) {
      quadrs.push([arr[fst], arr[snd], arr[left], arr[right]]);
      left += 1;
      right -= 1;
      while (left < right && arr[left] === arr[left - 1]) {
        left += 1;
      }

      while (left < right && arr[right] === arr[right + 1]) {
        right -= 1;
      }
    } else if (currSum < target) {
      left += 1;
    } else {
      right -= 1;
    }
  }
};

const backspace_compare = (str1, str2) => {
  const getNextIdx = (str, index) => {
    let toSkip = 0;

    while (index >= 0) {
      if (str[index] === "#") {
        toSkip += 1;
      } else if (toSkip > 0) {
        toSkip -= 1;
      } else {
        break;
      }
      index -= 1;
    }

    return index;
  };

  let index1 = str1.length - 1;
  let index2 = str2.length - 1;

  while (index1 || index2) {
    if (index1 < 0 && index2 < 0) {
      return true;
    }
    if (index1 < 0 || index2 < 0) {
      return false;
    }
    const next1 = getNextIdx(str1, index1);
    const next2 = getNextIdx(str2, index2);
    if (str1[next1] !== str2[next2]) {
      return false;
    }
    index1 = next1 - 1;
    index2 = next2 - 1;

    return true;
  }
};

console.log(backspace_compare("xy#z", "xzz#"));
console.log(backspace_compare("xy#z", "xyz#"));
console.log(backspace_compare("xp#", "xyz##"));
console.log(backspace_compare("xywrrmp", "xywrrmu#p"));
