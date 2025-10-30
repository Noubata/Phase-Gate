testList = ["madam", "racecar", "hello", "noon"]

function palindrome (testList){

	for(let word = 0; word < testList.length; word++){

	let myString = testList[word];

	let newString = ""
	
	for(let theString = myString.length - 1; theString >=0; theString--){

	newString += testList[theString]
	}
	testList[theString]= myString == newString
	}
	return testList
}
console.log(testList)