import logging
import pyrax
import sys

# import pyconru  # @UnusedImport

logger = logging.getLogger(__name__)



if __name__ == '__main__':
    # check authentication
    logger.debug('authenticated: %s' % pyrax.identity.authenticated)

    cs = pyrax.cloudservers
    server_name = "pyconru-%s" % pyrax.utils.random_ascii(8)
    
    ubu_image = [img for img in cs.images.list()
            if "14.04" in img.name
            and "PVHVM" in img.name][0]
    print("Ubuntu Image:", ubu_image)
    flavor_1GB = [flavor for flavor in cs.flavors.list()
            if flavor.ram == 1024][0]
    print("1024 Flavor:", flavor_1GB)
    server = cs.servers.create(server_name, ubu_image.id, flavor_1GB.id)
    print("Name:", server.name)
    print("ID:", server.id)
    print("Status:", server.status)
    print("Admin Password:", server.adminPass)
    print("Networks:", server.networks)
