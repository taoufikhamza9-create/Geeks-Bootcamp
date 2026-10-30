                               //Exercise 1

const people = ["Greg", "Mary", "Devon", "James"];
people.shift() // removes the first element ("Greg")
console.log(people)
people.splice(2,1,"Jason") // at index 2, removes 1 element and inserts "Jason" in its place
console.log(people)
people.push("Hamza") // adds "Hamza" at the end of the array
console.log(people)
console.log(people.indexOf("Mary")) // index of "Mary" in the array
let copy = people.slice(1,4) // new array from index 1 to 4 (4 excluded), people is not modified
console.log(copy)
console.log(people.indexOf("Fou")) // output -1 cause it's not in the array
let last = people[people.length - 1] // length of the array = 4 and the last element index is length - 1
console.log(last)

                                //Exercise 2

const colors = ["red" , "blue", "green" , "purple" , "yellow"]

// i starts at 0 so we display i+1 to start counting at 1
 for ( let i=0 ; i < colors.length ; i++ ) {
    console.log(`My #${i+1} choice is ${colors[i]}`)
}

// Bonus : only the special suffixes, every number after 3 uses "th"
const suffixes =[ "st", "nd" , "rd" ]


for ( let i=0 ; i < colors.length ; i++ ) {
    let suffixe
    if (i>=suffixes.length){ // no suffix at this index in the array -> default "th"
        suffixe= "th"
    }
    else{
        suffixe=suffixes[i]
    }
    console.log(`My ${i+1}${suffixe} choice is ${colors[i]}`)
}


                          //Exercise 3
//1
let num = prompt ("Enter a number please :")
console.log(typeof(num)) // prompt() always return a string
console.log(num)
//2
// do...while : asks at least once then keep asking while the number is smaller than 10
do {
    num = Number(prompt ("Enter a number please :")) // converts the string from prompt() into a number

} while (num<10)

                          //Exercise 4

 const building = {
    numberOfFloors: 4,
    numberOfAptByFloor: {
        firstFloor: 3,
        secondFloor: 4,
        thirdFloor: 9,
        fourthFloor: 2,
    },
    nameOfTenants: ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  { // [number of rooms, rent]
        sarah: [3, 990],
        dan:  [4, 1000],
        david: [1, 500],
    },
}
console.log(building["numberOfFloors"]) // number of floors
console.log(building["numberOfAptByFloor"]["firstFloor"]) // apartments on floor 1
console.log(building["numberOfAptByFloor"]["thirdFloor"]) // apartments on floor 3
console.log(building["nameOfTenants"][1]) // second tenant index 1
console.log(building["numberOfRoomsAndRent"]["dan"][0]) // Dan's number of rooms index 0

// index 1 = rent
const sarahRent=building["numberOfRoomsAndRent"]["sarah"][1]
const davidRent=building["numberOfRoomsAndRent"]["david"][1]
const danRent=building["numberOfRoomsAndRent"]["dan"][1]
if (sarahRent+davidRent>danRent){
    // write directly in the object : danRent is only a copy of the value
    building["numberOfRoomsAndRent"]["dan"][1]=1200
}

console.log(building["numberOfRoomsAndRent"]["dan"][1]) // check that the rent changed in the object

                            //Exercise 5

const family = { 
    father : "Mohamed",
    mother : "Meriem",
    child1 : "Moad",
    child2 : "Rachid",  
    child3 : "Malak",

}

// display the keys
for (let memberFamily in family){
    console.log(memberFamily)
}

// display the values (brackets because the key is in a variable)
for (let memberFamily in family){
    console.log(family[memberFamily])
}

                         //Exercise 6

 const details = {
  my: 'name',
  is: 'Rudolf',
  the: 'reindeer'
}

let phrase=""
// add each key and its value to the sentencen phrase
for (let x in details){
    phrase += x + " " + details[x] + " "
}
phrase = phrase.trim() // remove the extra space at the end
console.log(phrase)

                        //Exercise 7 

const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
let secretSoName =""

names.sort() // sort the names first so the first letters are already in order

// add the first letter of each name because a string works like an array of letters
for (let name of names){
    secretSoName += name[0]
}
console.log(secretSoName) 