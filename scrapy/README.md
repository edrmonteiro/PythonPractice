# Basic commands

## install

sudo apt-get install python3 python3-dev python3-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev

inside a virtualenv:
pip install scrapy
## start project

scrapy startproject projectName
scrapy startproject quotes_spider

## scrapy url

cd quotes_spider
scrapy genspider name websiteToScrapy
scrapy genspider quotes quotes.toscrape.com
## show scrapys on the project

scrapy list 

## to explore in terminal
### enter into scrapy shell

scrapy shell
### open a site with scrapy

inside the shell
fetch("quotes.toscrape.com/")

### to inspect the site

response
response.css('h1')
response.css('h1::text')
response.xpath('//h1')
response.xpath('//h1/a')
response.xpath('//h1/a/text()')
response.xpath('//h1/a/text()').extract()
response.xpath('//h1/a/text()').extract_first()
response.xpath('//h1/a/text()').extract()[0]

response.xpath('//*')
response.xpath('//*[@class="tag"]')
response.xpath('//*[@class="tag-item"]')
response.xpath('//*[@class="tag-item"]').extract()
response.xpath('//*[@class="tag-item"]/a/text()').extract()

## to run python code

outside shell from quotes_spider directory
scrapy crawl quotes 

if the website does not have robots.txt file, go to settings.py and change ROBOTSTXT_OBEY to false