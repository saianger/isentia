# isentia

Set up info:
1. scrapy package has been installed on local 
2. mongodb instance has been created in compose.io, the db name is isentia with a collection named articles
3. A simple REST API has been created using bottle module, and can be executed in local

Instructions
1. Pull the entire folder to local, run scrapy crawl isentia, it will start the spider and crawl  www.theguardian.com/au for 
   all the articles in it, and then insert each article to compose mongodb. (currently there are 59 articles been inserted)
2. Run python isentia_api.py on local, wait for service to start and open a browser, put the url with the keyword you want to
   search on. For example, if you want to search the article contains keyword "teenager", type in: 
   http://localhost:8080/articles/teenager
   
Limitation:
1. A proper data cleaning hasn't been done, some articles are not been extracted.
2. REST API can only show one document at a time
