import os
from ConfigParser import ConfigParser, NoOptionError

def get_config(config_location="~/led-controller.ini"):
    try:
        config = ConfigParser()
        config.read(os.path.expanduser(config_location))

        return config
    except Exception as e:
        print "Could not load config file : " + str(e)
