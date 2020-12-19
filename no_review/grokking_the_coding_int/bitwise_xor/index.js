// Single Number (easy)
const findSingleNumber = (arr) => {
  let num = 0;
  arr.forEach((x) => {
    num ^= x;
  });

  return num;
};

// console.log(findSingleNumber([1, 4, 2, 1, 3, 2, 3]));

const flipAndInvertImage = (matrix) => {
  matrix.forEach((row) => {
    let [start, end] = [0, row.length - 1];

    while (start < end) {
      [row[start], row[end]] = [row[end], row[start]];
      start++;
      end--;
    }

    for (let i = 0; i < row.length; i++) {
      row[i] ^= 1;
    }
  });

  return matrix;
};

// console.log(
//   flipAndInvertImage([
//     [1, 0, 1],
//     [1, 1, 1],
//     [0, 1, 1],
//   ])
// );
// console.log(
//   flipAndInvertImage([
//     [1, 1, 0, 0],
//     [1, 0, 0, 1],
//     [0, 1, 1, 1],
//     [1, 0, 1, 0],
//   ])
// );
