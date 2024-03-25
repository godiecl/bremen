import logging
import libs

# the logger
log = logging.getLogger(__name__)


def main():
    log.info('Starting the main thread ..')
    # code here!
    log.info('Done.')


# The main thread
if __name__ == '__main__':
    main()
