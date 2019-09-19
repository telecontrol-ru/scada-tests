from scadapy import NodeId
from scada_test import BaseTest


class PingTest(BaseTest):
  def test_ping(self):
    data_items = self.client.node(NodeId.DataItems)
    assert data_items == NodeId.DataItems
    assert data_items.browse_name == "DataItems"

  def test_creates(self):
    data_items = self.client.node(NodeId.DataItems)
    data_items_creates = data_items.targets(NodeId.Creates)
    assert NodeId.DataGroupType in data_items_creates
    assert NodeId.DataItemType in data_items_creates
