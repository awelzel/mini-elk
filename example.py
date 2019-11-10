"""
Simple example using a TCPLogstashHandler
"""
import logging
import random
import time

import logstash


def main():
    logstash_handler = logstash.TCPLogstashHandler(
        host="127.0.0.1", port="5959", version=1
    )
    logging.basicConfig(
        level=logging.DEBUG,
        handlers=[
            logging.StreamHandler(),
            logstash_handler,
        ],
    )

    logging.info("Hello hello")

    while True:
        r = random.random() + 0.1
        time.sleep(r * 2)
        logging.info("Random %.3f also in extra fields...", r,
                     extra={"random": r, "sub": {"random": r}})


if __name__ == "__main__":
    main()
