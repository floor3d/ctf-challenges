### Description
So many web pages, so little time. Which page has the flag?

### Build instructions
docker build -t web_server_image .
docker run -p 80:80 web_server_image

### Flag
CTF{crawl_lawl}

### Answer
Create a script to crawl all pages and return the one with CTF in it
