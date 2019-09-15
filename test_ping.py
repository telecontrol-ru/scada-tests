from scadapy import NodeId
from scada_test import BaseTest


class PingTest(BaseTest):

  def test_ping(self):
    root_folder = self.client.node(NodeId.DataItems)
    assert root_folder.browse_name == "DataItems"
