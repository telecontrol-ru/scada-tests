from logging import getLogger
from scadapy import Client
from unittest import TestCase
import yaml


class BaseTest(TestCase):

  def setUp(self):
    self.log = getLogger(self.__class__.__name__)
    with open("settings.yml") as f:
        settings = yaml.load(f, Loader=yaml.CLoader)
    self.log.info("Connect to %s as %s", settings["server"], settings["user_name"])
    self.client = Client(**settings)

  def tearDown(self):
    self.log.info("Disconnect")
    self.client.disconnect()
