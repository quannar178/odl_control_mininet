from utils import *
from constants import get_topo_uri, add_flow_template_json
import NodeClass
# _, my_topology = get_url(get_topo_uri)
# print(node_structure(my_topology))
node = NodeClass.NodeClass("openflow:1", [])
node.delete_table(0)