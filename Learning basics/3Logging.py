import logging
#https://docs.python.org/3/library/logging.html

logger = logging.getLogger(__name__)
logging.info("Work started")
def main():
    logging.error("Some error occured!")

main()