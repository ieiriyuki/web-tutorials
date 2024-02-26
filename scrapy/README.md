# Try Scrapy

https://docs.scrapy.org/en/latest/intro/tutorial.html

## to learn how to extract data with Scrapy

``python
scrapy shell 'url'

>>> response.css("title")
[<Selector query='descendant-or-self::title' data='<title>Quotes to Scrape</title>'>]

```

## Run scrapy

```bash
cd tomamu

scrapy cralw quotes
```
