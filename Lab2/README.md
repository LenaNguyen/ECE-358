## Task 1

To start the webserver run

> python3 lab2/webserver.py

Using a web browser, try making the following requests:
* File exists: http://127.0.0.1:10101/helloWorld.html
* File is nested and exists: http://127.0.0.1:10101/htdocs/nestedhelloWorld.html
* File does not exist: http://127.0.0.1:10101/Hello.html

The resulting webpages should look like the screenshots in Task 1 of the report.


Using a terminal, try running the following commands:

To execute GET requests
> python3 lab2/webclient.py -get

To execute HEAD requests
> python3 lab2/webclient.py -head

The resulting responses should look like the screenshots in Task 1 for the report. There should be three reponses for GET requests and three responses for the HEAD requests. If there is not, please rerun the above commands. 


## Task 2

To start the server run
> python3 lab2/server.py

To start the client run
> python3 lab2/client.py

In the client when prompted, the following domain names can be queried to determine their IP addresses
* google.com
* wikipedia.org
* youtube.com
* uwaterloo.ca
* amazon.ca
* end (this is used to terminate the client)

If at any point a typo is entered, the client and the server will need to be restarted

The random, re, and socket libraries are required to run the two files