from utils import *
from constants import get_topo_uri, add_flow_template_json
import NodeClass
if(is_server_open()):
    # _, my_topology = get_url(get_topo_uri)
    # print(node_structure(my_topology))
    # node.delete_flow(0)
    # node1.delete_table()
    node1 = NodeClass.NodeClass("openflow:1", [])
    node1.add_flow(0, 1, 2, 1)
    node1.add_flow(1, 2, 1, 2)
    node2 = NodeClass.NodeClass("openflow:2", [])
    node2.add_flow(0, 1, 2, 1)
    node2.add_flow(1, 2, 1, 2)