from scada_stack import Stack
from scadapy import Client
from unittest import TestCase
import logging
import yaml


class BaseTest(TestCase):

  def setUp(self):
    self.log = logging.getLogger(self.__class__.__name__)

    with open("settings.yml") as f:
        settings = yaml.load(f, Loader=yaml.CLoader)
    self.log.info("Connect to %s as %s", settings["server"], settings["user_name"])
    self.client = Client(**settings)

    self.stack = Stack(self.client)

  def tearDown(self):
    self.stack.delete()
    
    self.log.info("Disconnect")
    self.client.disconnect()
