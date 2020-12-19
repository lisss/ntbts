const {
  Point,
  KthLargestNumberInStream,
  FrequencyStack,
  findKLargestNumbers,
  findKthSmallestNumber,
  findClosestPoints,
  minimumCostToConnectRopes,
  findKFrequentNumbers,
  sortCharacterByFrequency,
  findClosestElements,
  findClosestElements2,
  findMaximumDistinctElements,
  findSumOfElements,
  rearrangeString,
  reorganizeString,
  scheduleTasks,
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

const testMinimumCostToConnectRopes = () => {
  console.log(
    `Minimum cost to connect ropes: ${minimumCostToConnectRopes([1, 3, 11, 5])}`
  );
  console.log(
    `Minimum cost to connect ropes: ${minimumCostToConnectRopes([3, 4, 5, 6])}`
  );
  console.log(
    `Minimum cost to connect ropes: ${minimumCostToConnectRopes([
      1,
      3,
      11,
      5,
      2,
    ])}`
  );
};

const testFindKFrequentNumbers = () => {
  console.log(
    `Here are the K frequent numbers: ${findKFrequentNumbers(
      [1, 3, 5, 12, 11, 12, 11],
      2
    )}`
  );
  console.log(
    `Here are the K frequent numbers: ${findKFrequentNumbers(
      [5, 12, 11, 3, 11],
      2
    )}`
  );
};

const testSortCharacterByFrequency = () => {
  console.log(
    `String after sorting characters by frequency: ${sortCharacterByFrequency(
      "Programming"
    )}`
  );
  console.log(
    `String after sorting characters by frequency: ${sortCharacterByFrequency(
      "abcbab"
    )}`
  );
};

const testKthLargestNumberInStream = () => {
  kthLargestNumber = new KthLargestNumberInStream([3, 1, 5, 12, 2, 11], 4);
  console.log(`4th largest number is: ${kthLargestNumber.add(6)}`);
  console.log(`4th largest number is: ${kthLargestNumber.add(13)}`);
  console.log(`4th largest number is: ${kthLargestNumber.add(4)}`);
};

const testFindClosestElements = () => {
  console.log(
    `'K' closest numbers to 'X' are: ${findClosestElements(
      [5, 6, 7, 8, 9],
      3,
      7
    )}`
  );
  console.log(
    `'K' closest numbers to 'X' are: ${findClosestElements(
      [2, 4, 5, 6, 9],
      3,
      6
    )}`
  );
  console.log(
    `'K' closest numbers to 'X' are: ${findClosestElements(
      [2, 4, 5, 6, 9],
      3,
      10
    )}`
  );
  console.log("--- another approach ---");
  console.log(
    `'K' closest numbers to 'X' are: ${findClosestElements2(
      [5, 6, 7, 8, 9],
      3,
      7
    )}`
  );
  console.log(
    `'K' closest numbers to 'X' are: ${findClosestElements2(
      [2, 4, 5, 6, 9],
      3,
      6
    )}`
  );
  console.log(
    `'K' closest numbers to 'X' are: ${findClosestElements2(
      [2, 4, 5, 6, 9],
      3,
      10
    )}`
  );
};

const testFindMaximumDistinctElements = () => {
  console.log(
    `Maximum distinct numbers after removing K numbers: ${findMaximumDistinctElements(
      [7, 3, 5, 8, 5, 3, 3],
      2
    )}`
  );
  console.log(
    `Maximum distinct numbers after removing K numbers: ${findMaximumDistinctElements(
      [3, 5, 12, 11, 12],
      3
    )}`
  );
  console.log(
    `Maximum distinct numbers after removing K numbers: ${findMaximumDistinctElements(
      [1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5],
      2
    )}`
  );
};

const testFindSumOfElements = () => {
  console.log(
    `Sum of all numbers between k1 and k2 smallest numbers: ${findSumOfElements(
      [1, 3, 12, 5, 15, 11],
      3,
      6
    )}`
  );
  console.log(
    `Sum of all numbers between k1 and k2 smallest numbers: ${findSumOfElements(
      [3, 5, 8, 7],
      1,
      4
    )}`
  );
};

const testRearrangeString = () => {
  console.log(`Rearranged string: ${rearrangeString("aappp")}`);
  console.log(`Rearranged string: ${rearrangeString("Programming")}`);
  console.log(`Rearranged string: ${rearrangeString("aapa")}`);
};

const testReorganizeString = () => {
  console.log(`Reorganized string: ${reorganizeString("Programming", 3)}`);
  console.log(`Reorganized string: ${reorganizeString("mmpp", 2)}`);
  console.log(`Reorganized string: ${reorganizeString("aabc", 3)}`);
  console.log(`Reorganized string: ${reorganizeString("aab", 2)}`);
  console.log(`Reorganized string: ${reorganizeString("aapa", 3)}`);
};

const testScheduleTasks = () => {
  console.log(
    `Minimum intervals needed to execute all tasks: ${scheduleTasks(
      ["a", "a", "a", "b", "c", "c"],
      2
    )}`
  );
  console.log(
    `Minimum intervals needed to execute all tasks: ${scheduleTasks(
      ["a", "b", "a"],
      3
    )}`
  );
  console.log(
    `Minimum intervals needed to execute all tasks: ${scheduleTasks(
      ["A", "A", "A", "B", "B", "B"],
      2
    )}`
  );
};

const testFrequencyStack = () => {
  const frequencyStack = new FrequencyStack();
  frequencyStack.push(1);
  frequencyStack.push(2);
  frequencyStack.push(3);
  frequencyStack.push(2);
  frequencyStack.push(1);
  frequencyStack.push(2);
  frequencyStack.push(5);
  console.log(frequencyStack.pop());
  console.log(frequencyStack.pop());
  console.log(frequencyStack.pop());
};

testFrequencyStack();
