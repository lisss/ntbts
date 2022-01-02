const same = (arr1, arr2) => {
    if (arr1.length !== arr2.length) {
        return false;
    }
    const initFreq = {};
    const squaredFreq = {};

    arr1.forEach(x => {
        const sq = x ** 2;
        initFreq[sq] = sq in initFreq ? ++initFreq[sq] : 1;
    });

    arr2.forEach(x => {
        squaredFreq[x] = x in squaredFreq ? ++squaredFreq[x] : 1;
    });

    for (let x in initFreq) {
        if (squaredFreq[x] !== initFreq[x]) {
            return false;
        }
    }

    return true;
};

const validAnagram1 = (s1, s2) => {
    if (s1.length !== s2.length) {
        return false;
    }

    const [freq1, freq2] = [{}, {}];

    for (let x of s1) {
        freq1[x] = (freq1[x] || 0) + 1;
    }

    for (let x of s2) {
        freq2[x] = (freq2[x] || 0) + 1;
    }

    for (let x in freq1) {
        if (freq2[x] !== freq1[x]) {
            return false;
        }
    }

    return true;
};

const validAnagram2 = (s1, s2) => {
    if (s1.length !== s2.length) {
        return false;
    }

    const lookup = {};

    for (let x of s1) {
        lookup[x] = (lookup[x] || 0) + 1;
    }

    for (let x of s2) {
        if (!lookup[x]) {
            return false;
        } else {
            lookup[x] -= 1;
        }
    }

    return true;
};

function sameFrequency(num1, num2) {
    const s1 = num1.toString();
    const s2 = num2.toString();

    if (s1.length !== s2.length) {
        return false;
    }

    const freqMap = {};
    for (let x of s1) {
        freqMap[x] = x in freqMap ? ++freqMap[x] : 1;
    }

    for (let x of s2) {
        if (!freqMap[x]) {
            return false;
        } else {
            freqMap[x]--;
        }
    }

    return true;
}

function areThereDuplicates(...args) {
    const freqMap = {};
    for (let x of args) {
        if (freqMap[x]) {
            return true;
        }
        freqMap[x] = 1;
    }

    return false;
}
