const fibMemo = (num, mem = [undefined, 1, 1]) => {
  if (mem[num] !== undefined) return mem[num];
  const res = fib(num - 1, mem) + fib(num - 2, mem);
  mem[num] = res;
  return res;
}

const fibTable = (num) => {
  if (num <= 2) return 1;
  const fibNums = [0, 1, 1];

  for (let i = 3; i <= num; i++) {
    fibNums[i] = fibNums[i - 1] + fibNums[i - 2];
  }

  return fibNums[num];
}

module.exports = {
  fibMemo,
  fibTable,
}