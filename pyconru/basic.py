import logging
import pyrax

# import pyconru  # @UnusedImport

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    # check authentication
    logger.debug('authenticated: %s' % pyrax.identity.authenticated)

    # token
    t = pyrax.identity.token
    # display first half of token, for demo purposes
    logger.info('identity token: %s%s' % (''.join(c for c in t[0:-len(t)/2]),
                                          '*' * (len(t)/2)))
