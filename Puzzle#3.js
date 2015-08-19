function reverseArray(array)
{
	if(array.length == 0)
	{
		return "Array is empty";
	}
	if(array.length == 1)
	{
		return array[0];
	}

	var head = array.pop();
	var reverseArr = [head, reverseArray(array)];
	return reverseArr;
}

var array = [0,1,2,3,4];
debug(reverseArray(array));
//console.log(reverseArray(array));