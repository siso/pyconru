import json
import logging
import pyrax

# import pyconru  # @UnusedImport

logger = logging.getLogger(__name__)



if __name__ == '__main__':
    # check authentication
    logger.debug('authenticated: %s' % pyrax.identity.authenticated)

    cs = pyrax.cloudservers

    # list available flavours
    print '** Cloud Servers Flavours **'
    for s in cs.list_flavors():
        print "%s - %s" % (s.id, s.name)

    # list available images
    print '** Cloud Servers Images **'
    for i in cs.list_images():
        print "%s - %s" % (i.id, i.name)
