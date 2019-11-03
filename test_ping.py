from scadapy import NodeId
from scada_test import BaseTest


class PingTest(BaseTest):
  def test_ping(self):
    data_items = self.client.node(NodeId.DataItems)
    assert data_items == NodeId.DataItems
    assert data_items.browse_name == "DataItems"

  def test_data_items(self):
    data_items = self.client.node(NodeId.DataItems)
    creates = data_items.targets(NodeId.Creates)
    assert NodeId.DataGroupType in creates
    assert NodeId.DataItemType in creates

  def test_data_group_type(self):
    data_group_type = self.client.node(NodeId.DataGroupType)
    assert data_group_type.node_id == NodeId.DataGroupType
    assert data_group_type.browse_name == "DataGroupType"
    creates = data_group_type.targets(NodeId.Creates)
    assert NodeId.DataGroupType in creates
    assert NodeId.DataItemType in creates