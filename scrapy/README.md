# Basic commands

## install

sudo apt-get install python3 python3-dev python3-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev

inside a virtualenv:
pip install scrapy

# 1_first_project
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

# 3_advanced

## scrapy process

scrapy startproject quotes_spider
cd quotes_spider
scrapy genspider quotes quotes.toscrape.com
scrapy shell 'http://quotes.toscrape.com/'
quotes = response.xpath('//*[@class="quote"]')
quote = quotes[0]
quote.extract()
quote.xpath('//a')
quote.xpath('.')
quote.xpath('//*[@class="text"]/text()').extract()
quote.xpath('//*[@class="text"]/text()').extract_first()
quote.xpath('//*[@itemprop="author"]/text()').extract_first()
quote.xpath('.//*[@itemprop="keywords"]/@content').extract_first()
quote.xpath('.//*[@class="tag"]//text()').extract()


next_page_url = response.xpath('//*[@class="next"]/a/@href').extract_first()
response.urljoin(next_page_url)

## save project result into file

scrapy crawl quotes -o items.csv
scrapy crawl quotes -o items.json
scrapy crawl quotes -o items.xml