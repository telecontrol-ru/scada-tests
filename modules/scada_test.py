from scada_stack import Stack
from scadapy import Client
from unittest import TestCase
import logging
import yaml


class BaseTest(TestCase):

  def setUp(self):
    self.log = logging.getLogger(self.__class__.__name__)

    with open("settings.yml") as f:
        settings = yaml.load(f, Loader=yaml.FullLoader)
    self.log.info("Connect to %s as %s", settings["server"], settings["user_name"])
    try:
        self.client = Client(**settings)
    except:
        self.log.exception("Can't connect to SCADA Server. Make sure the server is running and 'test' account exists.")
        raise

    self.stack = Stack(self.client)

  def tearDown(self):
    self.stack.delete()
    
    self.log.info("Disconnect")
    self.client.disconnect()
