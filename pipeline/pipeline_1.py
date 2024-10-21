from stage.stage_01_extract_text import TextExtractor
from src.Log import logger

class StageTextExtractor:
    def __init__(self, url, output_file) :
        self.url = url
        self.output_file = output_file

    def main(self):
        logger.info("---- Creating TextExtractor Object ----")
        p = TextExtractor(self.url, self.output_file)
        logger.info("---- Starting the text Extraction ----")
        p.extract_entire_content()
        logger.info("---- Compleated the text Extraction Stage ----")

        