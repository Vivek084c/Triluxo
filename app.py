from pipeline.pipeline_1 import StageTextExtractor
from src.Log import logger

url = "https://brainlox.com/courses/category/technical"
output_file = "website_content.txt"

STAGE_NAME="Text Extractor"
logger.info(f">>>>>> Started Stage {STAGE_NAME} <<<<<<")
p = StageTextExtractor(url, output_file)
p.main()
logger.info(f">>>>>> Compleated : {STAGE_NAME} <<<<<<")