const {
  Point, 
  findKLargestNumbers,
  findKthSmallestNumber,
  findClosestPoints,
} = require(".");

const testFindKLargestNumbers = () => {
  console.log(
    `Here are the top K numbers: ${findKLargestNumbers(
      [3, 1, 5, 12, 2, 11],
      3
    )}`
  );
  console.log(
    `Here are the top K numbers: ${findKLargestNumbers([5, 12, 11, -1, 12], 3)}`
  );
};

const testFindKthSmallestNumber = () => {
  console.log(
    `Kth smallest number is: ${findKthSmallestNumber([1, 5, 12, 2, 11, 5], 3)}`
  );
  // since there are two 5s in the input array, our 3rd and 4th smallest numbers should be a '5'
  console.log(
    `Kth smallest number is: ${findKthSmallestNumber([1, 5, 12, 2, 11, 5], 4)}`
  );
  console.log(
    `Kth smallest number is: ${findKthSmallestNumber([5, 12, 11, -1, 12], 3)}`
  );
};

const testFindClosestPoints = () => {
  points = findClosestPoints(
    [new Point(1, 3), new Point(3, 4), new Point(2, -1)],
    2
  );
  result = "Here are the k points closest the origin: ";
  for (i = 0; i < points.length; i++) result += points[i].getPoint();
  console.log(result);
};

testFindClosestPoints();
