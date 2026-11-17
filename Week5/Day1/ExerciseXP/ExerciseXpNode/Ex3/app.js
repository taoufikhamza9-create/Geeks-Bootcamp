const fileManager = require('./fileManager.js');
const readFile = fileManager.readFile;
const writeFile = fileManager.writeFile;

console.log(readFile('./HelloWorld.txt'));
writeFile('./ByWorld.txt', 'Writing to the file');
console.log(readFile('./ByWorld.txt'));