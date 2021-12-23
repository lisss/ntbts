const sumZero = arr => {
    let [start, end] = [0, arr.length - 1];

    while (start < end) {
        let sum = arr[start] + arr[end];

        if (sum === 0) {
            return [arr[start], arr[end]];
        }
        if (sum > 0) {
            end--;
        } else {
            start++;
        }
    }
};

function countUniqueValues(arr) {
    if (!arr.length) {
        return 0;
    }
    let start = 0;

    for (let end = 1; end < arr.length; end++) {
        if (arr[start] !== arr[end]) {
            start++;
            arr[start] = arr[end];
        }
    }

    return start + 1;
}

function averagePair(arr, target) {
    if (!arr.length) {
        return false;
    }

    let [start, end] = [0, arr.length - 1];

    while (start < end) {
        const avg = (arr[start] + arr[end]) / 2;
        if (avg === target) {
            return true;
        }
        if (avg < target) {
            start++;
        } else {
            end--;
        }
    }
    return false;
}

function isSubsequence(s1, s2) {
    if (s1.length > s2.length) {
        return false;
    }

    let [i, j] = [0, 0];
    while (i < s1.length && j < s2.length) {
        if (s1[i] === s2[j]) {
            i++;
        }
        j++;
        if (i === s1.length) {
            return true;
        }
    }
    return false;
}
console.log(isSubsequence('sr', 'str'));
console.log(isSubsequence('abc', 'acb'));
