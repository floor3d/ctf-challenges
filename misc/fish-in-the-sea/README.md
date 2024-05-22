### Description
They say that there are always more fish in the sea. However, I bet there’s more hashes than there are fish …
I’m thinking of a number between 0 and 999. The number has one decimal point; so, for example, 324.7 can be my 
number, but 324 can’t! The hash for my number is c7284578c298d2578f040b0660056b5711c98e28fc7520927d7c03d371da4504. 
What is my special number?

FLAG FORMAT: CTF{specialnumber}

### Flag
CTF{424.2}

### Solution
Make a script (python, bash, etc) to get the sha256sum of every number with 1 decimal point from 0 to 999 :D
You'll of course have to check if the hash matches mine!
