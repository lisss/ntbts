const factorial = num => {
    if (num === 0 || num === 1) return 1;
    return num * factorial(num - 1);
};

function power(num, pow) {
    if (pow === 0) return 1;
    if (pow === 1) return num;
    if (num === 1) return 1;

    return num * power(num, pow - 1);
}

const productOfArray = arr => {
    if (!arr.length) return 0;

    const _do = a => {
        if (!a.length) return 1;
        let n = a[a.length - 1];
        a.pop();
        return n * _do(a);
    };

    return _do(arr);
};

function recursiveRange(num) {
    if (num === 0) return 0;
    return num + recursiveRange(num - 1);
}

function fib(num) {
    if (num <= 2) return 1;
    return fib(num - 1) + fib(num - 2);
}

function reverse(s) {
    if (s.length <= 1) return s;
    if (s.length === 2) return s[1] + s[0];

    return s[s.length - 1] + reverse(s.slice(0, -1));
}

function isPalindrome(s) {
    if (s.length === 1) return true;
    if (s.length === 2) return s[0] === s[1];
    if (s[0] === s.slice(-1)) return isPalindrome(s.slice(1, -1));
    return false;
}

// arbitrary callback

const isOdd = val => val % 2 !== 0;

function someRecursive(arr, cb) {
    if (arr.length === 1) return cb(arr[0]);
    return cb(arr[arr.length - 1]) || someRecursive(arr.slice(0, 1), cb);
}

function flatten(arr) {
    let newArr = [];
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] instanceof Array) {
            newArr = newArr.concat(flatten(arr[i]));
        } else {
            newArr.push(arr[i]);
        }
    }

    return newArr;
}

function capitalizeFirst(array) {
    if (array.length === 1) {
        return [array[0][0].toUpperCase() + array[0].substr(1)];
    }
    const res = capitalizeFirst(array.slice(0, -1));
    const string =
        array.slice(array.length - 1)[0][0].toUpperCase() +
        array.slice(array.length - 1)[0].substr(1);
    res.push(string);
    return res;
}
console.log(capitalizeFirst(['abc', 'yzd']));
