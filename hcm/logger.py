import logging

LEVEL = logging.DEBUG

logger = logging.getLogger("hybrid-causal-discovery")
logger.setLevel(LEVEL)

ch = logging.StreamHandler()
ch.setLevel(LEVEL)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)

logger.addHandler(ch)
