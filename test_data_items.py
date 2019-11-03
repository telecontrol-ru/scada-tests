from scada_test import BaseTest
from scadapy import NodeId
import unittest


class DataItemsTest(BaseTest):
  def setUp(self):
    super().setUp()
    self.stack.add_from_file("test_data_items_stack.yml")

  def test_property_categories(self):
    data_item_type = self.client.node(NodeId.DataItemType)
    input1_property = data_item_type["Input1"]
    input1_category = input1_property.target(NodeId.HasPropertyCategory)
    assert input1_category.display_name == "Каналы"


if __name__ == '__main__':
  unittest.main()