from scadapy import Client
from unittest import TestCase
import yaml


class BaseTest(TestCase):

  def setUp(self):
    with open("settings.yml") as f:
        settings = yaml.load(f)
    self.client = Client(**settings)