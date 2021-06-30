import logging
from typing import List
from constants import del_flow_table_node_template_uri, add_flow_template_json, add_flow_table_node_template_uri, del_flow_node_template_uri
from utils import delUrl, putUrl
import json

class NodeClass:
    def __init__(self, node_id : str, terminate_id: List) -> None:
        self.node_id = node_id
        self.terminate_id = terminate_id
        self.table = 0
        self.flow = []
    
    def delete_flow(self, id_flow):
        url = del_flow_table_node_template_uri.format(self.node_id,self.table,id_flow)
        logging.info("Delete flow URL: %s" % str(url))
        delUrl(url)

    def delete_table(self):
        url = del_flow_node_template_uri.format(self.node_id,self.table)
        logging.info("Delete table URL: %s" % str(url))
        delUrl(url)


    def add_flow(self, id_flow, inport, outport, priority):
        # need check inport and outport in terminate_id
        self.flow.append(id_flow)
        tempate = add_flow_template_json
        tempate = tempate.replace("@id@", str(id_flow))
        tempate = tempate.replace("@inport@", str(inport))
        tempate = tempate.replace("@outport@", str(outport))
        tempate = tempate.replace("@priority@", str(priority))
        data_json = json.loads(tempate)
        url = add_flow_table_node_template_uri.format(self.node_id,self.table,id_flow)
        logging.info("Prepare data: %s" % str(data_json))
        logging.info("Add flow url: %s" % str(url))
        putUrl(url, data_json)
    