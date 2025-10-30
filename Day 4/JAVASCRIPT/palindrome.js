testList = ["madam", "racecar", "hello", "noon"]

function palindrome (testList){

	for(let word = 0; word < testList.length; word++){

	let myString = testList[word];
	let newString = ""
	
	for(let theString = 0; theString < myString.length ; theString--){

	newString += testList[theString]
	}
	testList[theString]= myString == newString
	}
	return testList
}
console.log(testList)