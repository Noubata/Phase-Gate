testList = [4, 3, 25, 100,101, -100, 3, 126, 626]
function perfectSquare(testList){

	let newBox = testList
	for (let number =0; number < testList.length; number++){
		let newNumber = testList[number]**0.5 * testList[number]**0.5
		if (newNumber == testList[number]){
			newBox[number]= true
		}else{
			newBox[number]= false
		}
	
	}
	return newBox
}
console.log(perfectSquare(testList))		