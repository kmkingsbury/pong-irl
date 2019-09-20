import logging
import yaml

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')


logging.debug("Reading Config file...")
with open("config.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

print(str(cfg))
