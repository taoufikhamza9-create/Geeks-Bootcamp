const fs = require('fs');

function readFile(filePath) {
  return fs.readFileSync(filePath, 'utf8');
}

function writeFile(filePath, content) {
  fs.writeFileSync(filePath, content, 'utf8');
}

module.exports = { readFile, writeFile };

/* 
//async CommonJs way 
const fs = require('fs');

const readFile = (filePath) => fs.promises.readFile(filePath, 'utf8');
const writeFile = (filePath, content) =>
  fs.promises.writeFile(filePath, content, 'utf8');

module.exports = { readFile, writeFile };
 */



/*
// Version ES6
import fs from 'node:fs';

export function readFile(filePath) {
  return fs.readFileSync(filePath, 'utf8');
}

export function writeFile(filePath, content) {
  fs.writeFileSync(filePath, content, 'utf8');
}
*/
