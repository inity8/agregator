pip install -r requirements.txt
scrapy runspider script.py -- output=data.json -L WARNING
scrapy runspider script.py -o ./output.json -L WARNING