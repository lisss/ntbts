// https://leetcode.com/problems/group-shifted-strings/
// @TODO!!!
const groupStrings = (strings) => {
  const _get_key = (s) => {
    res = [];
    for (let i = 0; i < s.length - 1; i++) {
      x = (s.charCodeAt([i + 1]) - s.charCodeAt([i])) % 26;
      res.push(x);
    }
    return res;
  };

  grouped = {};
  strings.forEach((x) => {
    key = _get_key(x);
    if (!(key in grouped)) {
      grouped[key] = [];
    }
    grouped[key].push(x);
  });
  res = [];
  Object.keys(grouped).forEach((k) => {
    res.push[grouped[k]];
  });

  return res;
};

console.log(groupStrings(["az", "ba"]));
