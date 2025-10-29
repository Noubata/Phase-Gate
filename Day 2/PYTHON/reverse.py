the_string = "e"

def my_string(string):
	to_reverse = "";
	for word in string:
		to_reverse = word + to_reverse;	
	return to_reverse;	

myWord = "beny";
to_reverse = my_string(myWord);

print(to_reverse)


def my_string2(the_string):
	the_string = "";
	return the_string;
	
output = to_reverse + the_string;
print(output);