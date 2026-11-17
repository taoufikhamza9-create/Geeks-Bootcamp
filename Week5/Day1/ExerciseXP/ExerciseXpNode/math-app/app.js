const _ = require("lodash");
const { add, multiply } = require("./math");

const additionResult = add(8, 4);
const multiplicationResult = multiply(6, 7);
const results = [additionResult, multiplicationResult];

console.log("Addition:", additionResult);
console.log("Multiplication:", multiplicationResult);
console.log("Total (Lodash):", _.sum(results));
console.log("Average (Lodash):", _.mean(results));
