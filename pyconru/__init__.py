import logging.config
import os
import pyrax
import sys

from pyconru.colouredconsolehandler import ColouredConsoleHandler  # @UnresolvedImport

PYRAX_DEFAULT_REGION = 'LON'

class AuthenticationError(Exception):
    def __init__(self, message='authentication error', Errors=None):

        # Call the base class constructor with the parameters it needs
        Exception.__init__(self, message)

        # Now for your custom code...
        self.Errors = Errors

# LOGGING
logging.handlers.ColouredConsoleHandler = ColouredConsoleHandler
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)

# AUTH ENV VARS
if os.getenv('OS_AUTH_USER'):
    logger.debug("OS_AUTH_USER: %s" % os.getenv('OS_AUTH_USER'))
else:
    logger.error('OS_AUTH_USER undefined')
    sys.exit(1)

if os.getenv('OS_AUTH_APIKEY'):
    logger.debug('OS_AUTH_APIKEY: ****')
else:
    logger.error('OS_AUTH_APIKEY undefined')
    sys.exit(1)

region = PYRAX_DEFAULT_REGION
if os.getenv('OS_AUTH_REGION'):
    logger.debug("OS_AUTH_REGION: %s" % os.getenv('OS_AUTH_USER'))
else:
    logger.warning("OS_AUTH_REGION undefined, using default '%s'" % region)

# authenticate
pyrax.set_setting('identity_type', 'rackspace')
pyrax.set_credentials(os.getenv('OS_AUTH_USER'),
                      os.getenv('OS_AUTH_APIKEY'),
                      region=region)
