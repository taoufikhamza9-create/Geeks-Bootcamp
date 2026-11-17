import { persons } from './data.js';
function averageAge() {
  let totalAge = 0;
  for(let persone of persons) {
    totalAge += persone.age;
  } 
  return console.log(totalAge / persons.length);
}
averageAge() // Returns the average age of all persons in the array   (result: 30)
