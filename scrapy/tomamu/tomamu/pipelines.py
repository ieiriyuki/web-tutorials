# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

from itemadapter import ItemAdapter


class TomamuPipeline:
    def open_spider(self, spider):
        self.file = open("quotes.jsonl", "w")

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(ItemAdapter(item).asdict()) + "\n"
        self.file.write(line)
        return item
