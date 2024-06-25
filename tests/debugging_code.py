import logging


def func(*args, **kwargs):
    print(vars())
    
func(1,2,3)
func(['a', 'b', 'argh'])



logging.debug('Looks like rain')
logging.info('And hail')
logging.warn('Did I hear thunder?')
logging.error('Was that lightning?')
logging.critical('Stop fencing and get inside!')

logging.basicConfig(level=logging.DEBUG)
logging.debug("It's raining again")
logging.info('With hail the size of hailstones')

logging.basicConfig(level='DEBUG')
logger = logging.getLogger('bunyan')
logger.debug('Timber!')

logging.basicConfig(level='DEBUG', filename='blue_ox.log')
logger = logging.getLogger('bunyan')
logger.debug("Where's my axe?")
logger.warning('I need my axe')

fmt = '%(asctime)s %(levelname)s %(lineno)s %(message)s'
logging.basicConfig(level='DEBUG', format=fmt)
logger = logging.getLogger('bunyan')
logger.error("Where's my other plaid shirt?")