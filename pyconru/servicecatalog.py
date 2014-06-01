import json
import logging
import pyrax

# import pyconru  # @UnusedImport

logger = logging.getLogger(__name__)

def compute_endpoint():
    '''
    fetch compute endpoint
    '''
    for i in pyrax.identity.service_catalog:
        if i['type'] == 'compute':
            return i
    return None

if __name__ == '__main__':
    # check authentication
    logger.debug('authenticated: %s' % pyrax.identity.authenticated)

    # catalog of service endpoints
    logger.info("\n%s" % json.dumps(pyrax.identity.service_catalog,
                                    sort_keys=True, indent=4))

    # compute endpoint
    logger.info("\ncompute endpoint: %s" %
                json.dumps(compute_endpoint(), sort_keys=True, indent=4))
