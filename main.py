from utils import *
from constants import get_topo_uri, add_flow_port_template_json
import NodeClass
if(is_server_open("192.168.56.4", "8181")):
    _, my_topology = get_url(get_topo_uri, "192.168.56.4", "8181", "admin", "admin")
    print((my_topology))
    # node.delete_flow(0)
    # node1.delete_table()
    # node1 = NodeClass.NodeClass("openflow:1", [])
    # node1.add_flow(0, 1, 2, 1)
    # node1.add_flow(1, 2, 1, 2)
    # node2 = NodeClass.NodeClass("openflow:2", [])
    # node2.add_flow(0, 1, 2, 1)
    # node2.add_flow(1, 2, 1, 2)