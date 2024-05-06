### Description
Apparently this program has something to do with a murder mystery. What secrets does it hold?

### Build instructions
docker run -dit -p 1337:1337 img-name-here

### Flag
CTF{Wang's fingerprints are covered in oil and salt}

### Writeup
The program trusts user input ... bad mistake! instead of inputting a file number, you can input the file name :)
Read file.txt to see the flag :)
