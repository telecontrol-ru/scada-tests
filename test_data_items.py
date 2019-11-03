from scada_test import BaseTest
from scadapy import NodeId
import unittest


class DataItemsTest(BaseTest):
  def test_property_categories(self):
    self.stack.add_from_file("test_data_items_stack.yml")
    analog_item = self.stack.node("AnalogItem")
    assert analog_item["Input1"].target(NodeId.HasPropertyCategory) == NodeId.ChannelsPropertyCategory


if __name__ == '__main__':
  unittest.main()