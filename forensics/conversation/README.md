### Description
I was listening on my network and accidentally snooped on a conversation. Did they say anything of note?

### Flag
CTF{N3TC4TS_R_US}

### Writeup
The easy way to do this is to right click on one of the packets in Wireshark and Follow > TCP Stream.

With this, you can simply click through the streams in the bottom right and find the plaintext conversations.

The flag is in one of the TCP streams, and is base64 encoded. If you decode it, you will get the flag!
