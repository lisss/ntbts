
class HashMap {
  constructor(size = 53) {
    this.keyMap = (new Array(size));
  }

  _hash (key) {
    let total = 0;
    const MAGIC_PRIME = 31;
    for (let i = 0; i < Math.min(key.length, 100); i++) {
      const ch = key[i]
      const code = ch.charCodeAt(0) - 96;
      total = (total * MAGIC_PRIME + code) % this.keyMap.length;
    }

    return total;
  }

  set(key, val) {
    const hash = this._hash(key);
    if (!this.keyMap[hash]) {
      this.keyMap[hash] = []
    }
    const existingIdx = this.keyMap[hash].map(x => x.indexOf(key))
    if (existingIdx.length) {
      this.keyMap[hash][existingIdx[0]] = [key, val]
    } else {
      this.keyMap[hash].push([key, val])
    }
  }

  get(key) {
    const hash = this._hash(key);
    if (!this.keyMap[hash]) {
      return
    }
    const items = this.keyMap[hash];
    for (let it of items) {
      const [k, v] = it
      if (k === key) {
        return v
      }
    }

    return
  }

  keys() {
    return this.keyMap.flatMap(x => x.map(x => x[0]))
  }

  values() {
    return this.keyMap.flatMap(x => x.map(x => x[1]))
            .filter((val, i, arr) => arr.indexOf(val) === i)
  }
}

module.exports = {
  HashMap,
}