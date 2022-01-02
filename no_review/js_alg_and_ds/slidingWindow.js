const maxSubarraySum = (arr, num) => {
    if (num > arr.length) {
        return null;
    }

    let maxSum = 0;

    for (let i = 0; i < num; i++) {
        maxSum += arr[i];
    }

    let temp = maxSum;
    for (let i = num; i < arr.length; i++) {
        temp = temp - arr[i - num] + arr[i];
        maxSum = Math.max(temp, maxSum);
    }

    return maxSum;
};

const minSubarrayLen = (arr, sum) => {
    let start = 0;
    let minSum = 0;
    let minLen = Infinity;

    for (let i = 0; i < arr.length; i++) {
        minSum += arr[i];
        while (minSum >= sum) {
            minLen = Math.min(minLen, i - start + 1);
            minSum -= arr[start];
            start++;
        }
    }

    return minLen === Infinity ? 0 : minLen;
};

function findLongestSubstring(s) {
    if (!s.length) return 0;
    let start = 0;
    let len = 0;
    const seen = {};

    for (let i = 0; i < s.length; i++) {
        const nextCh = s[i];
        if (nextCh in seen) {
            start = Math.max(start, seen[nextCh] + 1);
        }

        seen[nextCh] = i;
        len = Math.max(len, i - start + 1);
    }

    return len;
}

console.log(findLongestSubstring('abcc'));
console.log(findLongestSubstring('bbbb'));
