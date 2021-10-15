const linearSearch = (arr, val) => {
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === val) {
      return i
    }
  }

  return -1
}

function binarySearch(arr, val){
  let [left, right] = [0, arr.length - 1];

  while (left < right) {
    const mid = left + Math.round((right - left) / 2);
    const midVal = arr[mid];
    if (midVal === val) {
      return mid;
    }
    if (midVal > val) {
      right = mid - 1;
    } else {
      left = mid;
    }
  }

  return -1;
}

function binarySearch1(arr, val){
  let [left, right] = [0, arr.length - 1];
  let mid = Math.floor((left + right) / 2);

  while (arr[mid] !== val) {
    if (arr[mid] > val) {
      right = mid - 1;
    } else {
      left = mid + 1;
    }
    if (left > right) {
      return -1;
    }
    mid = Math.floor((left + right) / 2);
  }

  return mid;
}

module.exports = {
  linearSearch,
  binarySearch,
  binarySearch1,
}