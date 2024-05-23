### Description
I’ve made a peculiar program. I input my flag and it spat out a string, but then I forgot what the flag was! I guess you’ll have to reverse engineer my binary … can’t you sea?
	FLAG OUTPUT: 59gdCTF{ibf}f83b

### Flag
CTF{f83b59gdibf}

### Solution
You will have to reverse the binary with something like Ghidra.

The binary splits the string into four, and then prints the third quarter, first quarter, fourth quarter, and second quarter.
