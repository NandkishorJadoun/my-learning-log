// L1: Arrays

// Assignment
export function averageScore(ratings: number[]) {
  if (ratings.length === 0) {
    return 0;
  }

  const sum = ratings.reduce((acc, cur) => acc + cur, 0);
  const length = ratings.length;

  return sum / length;
}

// L2: Types parameters

const ratingsUsingTypeParam: Array<number> = [1, 2, 3];

// L3: Heterogeneous Arrays (Array contains different types)

const HeterogeneousArr = ["hello", "world", 11, 55];

// Assignment
export function interpolateComment(
  id: number,
  comment: string,
  comments: (string | number)[],
) {
  return comments.map((c) => {
    return c === id ? comment : c;
  });
}

// L4: Rest Parameters (denoted by three dots (...) before the parameter name)

//Assignment
export function formatLabels(...labels: string[]) {
  if (labels.length === 0) return "No labels";
  if (labels.length === 1) return `Label: ${labels[0]}`;
  return `Labels: ${labels.join(", ")}`;
}

// L5: Evolving any()

// Creating an empty array infers the type as `any[]`, and pushing items of different types
// will work without errors within that scope.
// However, in the outer scope, the array will be inferred to have the types
// that were pushed or defined in the inner scope.

//Assignment
export function collectSupportData(id: number, resolved: boolean) {
  const supportData = [];
  supportData.push("Support session started", id, resolved);
  return supportData;
}
