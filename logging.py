import logging
# to log debug and info, perform the below settings
#logging.basicConfig(level = logging.DEBUG) # must appear at the top before calling any loging method
#to log in a file
logging.basicConfig(filename='app.log', filemode='w', format='%(asctime)-15s - %(name)s - %(levelname)s - %(message)s', level = logging.DEBUG)
# to log ONLY info, perform the below settings
#logging.basicConfig(level = logging.INFO)
logging.error('Error has occured')
logging.warning('Error has occured')
logging.critical('Error has occured')
logging.debug('Error has occured')
logging.info('Error has occured')


logging.warning('write log to a file new')
