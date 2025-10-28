// goal: copy numbers > 0 into a new array
function positives(arr) {
  const out = [];
  // BUG: i <= arr.length causes one extra iteration with arr[i] === undefined
  for (let i = 0; i <= arr.length; i++) {
    if (arr[i] > 0) {      // undefined > 0 => false, but may mask other bugs
      out.push(arr[i]);
    }
  }
  return out;
}

console.log(positives([1, -2, 3])); // expected [1,3], but loop logic is wrong
