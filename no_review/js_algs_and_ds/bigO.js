const addUpTo = n => {
    let res = 0;

    for (let i = 1; i <= n; i++) {
        res += i;
    }

    return res;
};

const addUpToFast = n => (n * (n + 1)) / 2;
console.time('slow');
console.log(addUpTo(100));
console.timeEnd('slow');
console.time('fast');
console.log(addUpToFast(100));
console.timeEnd('fast');
