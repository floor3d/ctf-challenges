### Description
We have intercepted a packet capture of a rival hacker. It is possible that this hacker has
some of the same targets that we do! Our intel has warned us that he may have gotten access to a 
database which contains information on one of our top targets, Montgomery.
Do some digging and see if you can find anything that he hacked! If you can find his password,
that would be great...

### Questions
1. This traffic is encrypted! That's no good -- cryptography is scary. Decrypt this traffic using
your special abilities ... or, by chance, the keylog file given to you. When decrypted, what protocol
would be most interesting for us to examine? (seeing as they got access to some online database)

2. Seems as if this attacker did more than just attack a database. Beware of easter eggs. What packet
number is the 'interesting' one -- the one that was used to send a special malicious payload?

3. Great! We have the payload ... but no response? Huh... seems like NEUCTF -- I mean some malicious
entity -- has removed the packet from the capture! Try to run that attack yourself. What is the flag?

**NOTE -- The challenge for this is no longer up. There is no way to get this flag anymore!**


### Question answers
1. HTTP
2. 11831
3. Welp ... no way to do this one! But if you got this far, I bet you could get access by copying the SQL injection payload :)
