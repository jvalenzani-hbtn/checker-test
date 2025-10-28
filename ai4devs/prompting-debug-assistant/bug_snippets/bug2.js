// goal: compute average rating (0..5) from numbers array
function averageRating(ratings) {
  if (!Array.isArray(ratings) || ratings.length === 0) return 0;

  // BUG: reduce without initial value + divides by (length - 1)
  const sum = ratings.reduce((a, b) => a + b);
  return sum / (ratings.length - 1); // off logic: inflates average
}

// Expected average of [4, 5, 3] is 4.0, but this returns 6.0
console.log(averageRating([4, 5, 3]));
