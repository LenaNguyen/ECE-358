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

The resulting reponses should look like the screenshots in Task 1 for the report. There should be three reponses for GET requests and three responses for the HEAD requests. If there is not, please rerun the above commands. 
