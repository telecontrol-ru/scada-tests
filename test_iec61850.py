from scada_test import BaseTest

class Iec61850Test(BaseTest):
  def test_basic(self):
    self.stack.add_from_file("test_iec61850_stack.yml")
    device = self.stack.node("ClientDevice")
    self.log.info("Wait for device connection")
    device["Online"].wait_for_value(True)
