from scrapy.selector import Selector
import pathlib

file_name = "foo.html"
path = str(pathlib.Path().resolve()) + "/"
file = open(path + file_name)
html_doc = file.read()
    
sel = Selector(text=html_doc)

sel.extract()

sel.xpath('/html/head/title').extract()
sel.xpath('//title').extract()
sel.xpath('//text()').extract()


