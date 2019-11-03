from scada_test import BaseTest
import unittest


class Iec61850Test(BaseTest):
  def setUp(self):
    super().setUp()
    self.stack.add_from_file("test_iec61850_stack.yml")

  def test_basic(self):
    self.log.info("Wait for client device connection")
    self.stack.node("ClientDevice")["Online"].wait_for_value(True)
    client_device = self.stack.node("ServerDevice")
    self.log.info("Wait for server device connection")
    self.stack.node("ServerDevice")["Online"].wait_for_value(True)


if __name__ == '__main__':
  unittest.main()