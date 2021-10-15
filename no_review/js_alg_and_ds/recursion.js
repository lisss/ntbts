// recursive generators
function aa(list) {
  function* flatten(list) {
      if (!Array.isArray(list)) {
        console.log('>>> 1', list)
          yield list
      } else {
        console.log('>>> 2', list)
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