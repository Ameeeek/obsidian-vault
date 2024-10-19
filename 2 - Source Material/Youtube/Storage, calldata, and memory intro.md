---
Source: https://updraft.cyfrin.io/courses/solidity/simple-storage/solidity-memory-storage-calldata?lesson_format=video
tags:
  - web3
---
# Storage, calldata, and memory intro


![[Pasted image 20240806134112.png]]

  

 okay so basically, there are 3 major type of places that EVM (Ethereum virtual machine) can write into

 which is memory, call data and storage.

  
 to simplify things

 calldata : temporary storage that can not be changed

 this code below will NOT be able to compile, because you cannot change data that is lcoated in the calldata

```solidity
function addPerson(string calldata _name, uint256 favNumber) public{
	_name = "cat";
	 listOfPeople.push(Person(favNumber, _name ));
}
```

  

 memory : temporary storage that can be changed

 this code below will be able to compile

```
 function addPerson(string memory _name, uint256 favNumber) public{

 _name = "cat";

 listOfPeople.push(Person(favNumber, _name ));

 }
```
  

 storage : permanent storage that can be changed. for your information, every variable under the contract scope and outside any function or struct will be stored in storage, which will make it to be permanent

  

 for context, temporary means that the data will only be stored upon the function call. so once the code is recompiled, the data goes bye bye

  

 okay now there's another question raised,

 why do we state the memory in _name, and not in uint256, because when you try to state the uint256, it will lure the error to come,

 because memory or calldata is only specified for special type like array and temporary data/variable, meanwhile uint on the other side is a permanent type

 and _name is a temporary data and IS a an array of character since it's a string

  

 well then can i use storage on _name? well basically no, because storage is used for permanent data and _name is temporary

  

so, struct, array and mappings, needs to be given temporary keyword like memory or call data.
### References