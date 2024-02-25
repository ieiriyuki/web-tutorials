# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

from itemadapter import ItemAdapter
from scrapy.exporters import JsonLinesItemExporter


class TomamuPipeline:
    def open_spider(self, spider):
        self.file = open("quotes.jsonl", "wb")

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        self._exporter_for_items(item)
        return item

    def _exporter_for_items(self, item):
        exporter = JsonLinesItemExporter(self.file)
        exporter.start_exporting()
        exporter.export_item(item)
        exporter.finish_exporting()
