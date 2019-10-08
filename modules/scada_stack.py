from scadapy import NodeId
import logging
import yaml


def NodeIdFromString(str):
  return getattr(NodeId, str)

class Stack:
  def __init__(self, client):
    self.log = logging.getLogger(self.__class__.__name__)
    self.client = client
    self.node_ids = {}

  def node_id(self, name):
    return self.node_ids[name]

  def node(self, name):
    return self.client.node(self.node_id(name))

  def add_from_file(self, path):
    self.log.info(f"Add nodes from {path}")
    with open(path) as f:
        stack_template = yaml.load(f, Loader=yaml.CLoader)
    self.add_from_template(stack_template)

  def add_from_template(self, stack_template):
    for name, node_template in stack_template.items():
        self.add_node_from_template(name, node_template)

  def add_node_from_template(self, name, node_template):
    self.log.info(f"Add node {name}")
    node_id = self.client.add_node(
        parent_id=NodeIdFromString(node_template["ParentId"]),
        type_definition_id=NodeIdFromString(node_template["TypeDefinitionId"]),
        browse_name=node_template.get("BrowseName", ""),
        display_name=node_template.get("DisplayName", "")
    )
    self.node_ids[name] = node_id
    properties = node_template.get("Properties", {})
    if len(properties) != 0:
      node = self.client.node(node_id)
      for name, value in properties.items():
        node[name].value = value

  def delete(self):
    for name, node_id in self.node_ids.items():
        self.log.info(f"Delete node {name}")
        self.client.delete_node(node_id)
