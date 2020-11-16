const non_repeat_substring = (str) => {
  const savedChars = {};
  let maxLength = 0,
    windowStart = 0;

  str.split("").forEach((nextChar, windowEnd) => {
    if (nextChar in savedChars) {
      // this is tricky; in the current window, we will not have any 'rightChar' after its previous index
      // and if 'windowStart' is already ahead of the last index of 'rightChar', we'll keep 'windowStart'
      windowStart = Math.max(windowStart, savedChars[nextChar] + 1);
    }
    // insert the 'rightChar' into the map
    savedChars[nextChar] = windowEnd;
    // remember the maximum length so far
    maxLength = Math.max(maxLength, windowEnd - windowStart + 1);
  });

  return maxLength;
};

const length_of_longest_substring = (str, k) => {
  const frequencyMap = {};
  let maxLength = 0,
    windowStart = 0,
    maxFrequency = 0;

  const chars = str.split("");
  chars.forEach((rightChar, windowEnd) => {
    if (!(rightChar in frequencyMap)) {
      frequencyMap[rightChar] = 0;
    }
    frequencyMap[rightChar] += 1;

    maxFrequency = Math.max(maxFrequency, frequencyMap[rightChar]);

    if (windowEnd - windowStart + 1 - maxFrequency > k) {
      const leftChar = chars[windowStart];
      frequencyMap[leftChar] += 1;
      windowStart += 1;
    }

    maxLength = Math.max(maxLength, windowEnd - windowStart + 1);
  });

  return maxLength;
};

const length_of_longest_subarray = (arr, k) => {
  let maxLength = 0,
    windowStart = 0,
    maxOnesCount = 0;

  arr.forEach((rightChar, windowEnd) => {
    if (rightChar === 1) {
      maxOnesCount += 1;
    }

    if (windowEnd - windowStart + 1 - maxOnesCount > k) {
      if (arr[windowStart] == 1) {
        maxOnesCount -= 1;
      }
      windowStart += 1;
    }

    maxLength = Math.max(maxLength, windowEnd - windowStart + 1);
  });

  return maxLength;
};

const find_permutation = (str, pattern) => {
  const frequencyMap = {};
  let windowStart = 0,
    matched = 0;

  pattern.split("").forEach((ch) => {
    if (!(ch in frequencyMap)) {
      frequencyMap[ch] = 0;
    }
    frequencyMap[ch] += 1;
  });

  const chars = str.split("");

  return chars.reduce((isPerm, rightChar, windowEnd) => {
    if (rightChar in frequencyMap) {
      frequencyMap[rightChar] -= 1;
      if (frequencyMap[rightChar] === 0) {
        matched += 1;
      }
    }

    if (Object.keys(frequencyMap).length === matched) return true;

    if (windowEnd >= pattern.length - 1) {
      const leftChar = chars[windowStart];

      if (leftChar in frequencyMap) {
        if (frequencyMap[leftChar] === 0) {
          matched -= 1;
        }
        frequencyMap[leftChar] += 1;
      }
      windowStart += 1;
    }
    return isPerm;
  }, false);
};

const find_substring = (str, pattern) => {
  const frequencyMap = {};
  let windowStart = 0,
    matched = 0,
    substrStart = 0;
  let minLength = str.length + 1;

  pattern.split("").forEach((ch) => {
    if (!(ch in frequencyMap)) {
      frequencyMap[ch] = 0;
    }
    frequencyMap[ch] += 1;
  });

  const chars = str.split("");

  return chars.reduce((_, rightChar, windowEnd) => {
    if (rightChar in frequencyMap) {
      frequencyMap[rightChar] -= 1;
      if (frequencyMap[rightChar] >= 0) {
        matched += 1;
      }
    }

    while (matched === pattern.length) {
      if (minLength > windowEnd - windowStart + 1) {
        minLength = windowEnd - windowStart + 1;
        substrStart = windowStart;
      }
      const leftChar = chars[windowStart];
      windowStart += 1;

      if (leftChar in frequencyMap) {
        if (frequencyMap[leftChar] === 0) {
          matched -= 1;
        }
        frequencyMap[leftChar] += 1;
      }
    }
    if (minLength > str.length) {
      return "";
    }
    return str.substring(substrStart, substrStart + minLength);
  }, "");
};

console.log(`${find_substring("aabdec", "abc")}`);
console.log(`${find_substring("abdabca", "abc")}`);
console.log(`${find_substring("adcad", "abc")}`);
