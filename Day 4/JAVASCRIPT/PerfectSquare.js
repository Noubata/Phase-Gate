testList = [4, 9, 25, 49]

function perfectSquare(testList){

	let newBox = []
	let number1 =0
	for(let number = 0; number <=testList.length; number++){
		if (number == number**0.5 * number**0.5){
			newBox[number] = true
			return newBox 
		}else{
			newBox[number] = false
			return newBox 	
		}
	}
}
console.log(perfectSquare(testList))





