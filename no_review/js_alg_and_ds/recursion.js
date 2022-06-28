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

// recursive generators
function aa(list) {
  function* flatten(list) {
      if (!Array.isArray(list)) {
          yield list
      } else {
          yield list.map(x => flatten(x))
      }
  }

  return flatten(list)
}

// const gen = aa([1,2])
// console.log(gen)
// console.log(gen.next())
// console.log(gen.next())

const fl = (elem, res) => {
  if (!Array.isArray(elem)) {
    res.push(elem)
  } else {
    elem.forEach(x => fl(x, res))
  }
  return res
}

function capitalizeFirst (arr) {
  if (arr.length === 1) {
    return [arr[0][0].toUpperCase() + arr[0].substr(1)]
  }
  const res = capitalizeFirst(arr.slice(0, -1))
  const nextWord = arr.slice(arr.length - 1)[0]
  res.push(nextWord[0].toUpperCase() + nextWord.substr(1))
  return res
}

// return a sum of all even numbers in an object
// that may contain nested objects
function nestedEvenSum (obj) {

  let sum = 0;

  const _do = (obj) => {
    if (typeof obj !== 'object' || !Object.keys(obj).length) {
      return;
    }
    for (let [k, v] of Object.entries(obj)) {
      if (typeof v === 'number' && v % 2 === 0) {
        sum += v;
      } else {
        _do(v);
      }
    }
  };

  _do(obj);
  return sum;
}


// var obj1 = {
//   outer: 2,
//   obj: {
//     inner: 2,
//     otherObj: {
//       superInner: 2,
//       notANumber: true,
//       alsoNotANumber: "yup"
//     }
//   }
// }

// var obj2 = {
//   a: 2,
//   b: {b: 2, bb: {b: 3, bb: {b: 2}}},
//   c: {c: {c: 2}, cc: 'ball', ccc: 5},
//   d: 1,
//   e: {e: {e: 2}, ee: 'car'}
// };

/*****
 * 
 */
function capitalizeWords (arr) {
  if (arr.length === 1) {
    return [arr[0].toUpperCase()]
  }
  const res = capitalizeWords(arr.slice(0, -1))
  res.push(arr.slice(arr.length - 1)[0].toUpperCase())

  return res
}


/**
 * stringify numbers
 */
// let obj = {
//     num: 1,
//     test: [],
//     data: {
//         val: 4,
//         info: {
//             isRight: true,
//             random: 66
//         }
//     }
// }

const stringifyNumbers = (obj) => {
  if (typeof obj !== 'object' || !Object.keys(obj).length) {
    return obj
  }
  const newObj = {}
  for (let [k, v] of Object.entries(obj)) {
    if (typeof v === 'number') {
      newObj[k] = v.toString()
    } else {
      newObj[k] = stringifyNumbers(v);
    }
  }
  return newObj;
}

/*
{
    num: "1",
    test: [],
    data: {
        val: "4",
        info: {
            isRight: true,
            random: "66"
        }
    }
}
*/

/**
 * return array of values typeof string
 */
const collectStrings = (obj) => {
  let res = []
  if (typeof obj !== 'object' || !Object.keys(obj).length) {
    return res
  }

  for (let [k, v] of Object.entries(obj)) {
    if (typeof v === 'string') {
      res.push(v)
    } else {
      res = res.concat(collectStrings(v))
    }
  }

  return res;

};

const obj = {
    stuff: "foo",
    data: {
        val: {
            thing: {
                info: "bar",
                moreInfo: {
                    evenMoreInfo: {
                        weMadeIt: "baz"
                    }
                }
            }
        }
    }
}