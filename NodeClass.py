import logging
from typing import List
from constants import del_flow_table_node_template_uri, add_flow_port_template_json, add_flow_table_node_template_uri, del_flow_node_template_uri
from utils import delUrl, putUrl
import json

class NodeClass:
    def __init__(self, node_id : str, terminate_id: List) -> None:
        self.node_id = node_id
        self.terminate_id = terminate_id
        self.table = 0
        self.flow = []

    def __str__(self) -> str:
        return "{} : terminate_id: {} : flow: {}".format(self.node_id, self.terminate_id, self.flow)
    
    def get_node_id(self):
        return self.node_id
    def get_flow(self):
        flow = []
        for temp in self.flow:
            flow.append(json.dumps(temp))
        return flow
    def get_terminate_id(self):
        return self.terminate_id
    
    def delete_flow(self, id_flow, odl_ip, odl_port, odl_user, odl_password):
        url = del_flow_table_node_template_uri.format(odl_ip, odl_port, self.node_id,self.table,id_flow)
        # logging.info("Delete flow URL: %s" % str(url))
        if(delUrl(url, odl_user, odl_password)):
            for temp in self.flow:
                if(temp["id"] == id_flow):
                    self.flow.remove(temp)
            logging.info(self)
            return True
        else:
            return False

    def delete_table(self, odl_ip, odl_port, odl_user, odl_password):
        url = del_flow_node_template_uri.format(odl_ip, odl_port,self.node_id,self.table)
        logging.info("Delete table URL: %s" % str(url))
        if(delUrl(url, odl_user, odl_password)):
            self.flow = []
            return True
        return False


    def add_flow(self, odl_ip, odl_port, odl_user, odl_password, id_flow, inport, outport, priority):

        tempate = add_flow_port_template_json
        tempate = tempate.replace("@id@", str(id_flow))
        tempate = tempate.replace("@inport@", str(inport))
        tempate = tempate.replace("@outport@", str(outport))
        tempate = tempate.replace("@priority@", str(priority))
        data_json = json.loads(tempate)
        url = add_flow_table_node_template_uri.format(odl_ip, odl_port, self.node_id,self.table,id_flow)
        # logging.info("Prepare data: %s" % str(data_json))
        # logging.info("Add flow url: %s" % str(url))
        if(putUrl(url, data_json, odl_ip, odl_port, odl_user, odl_password)):
            flow_info = {}
            flow_info["id"] = id_flow
            flow_info["info"]  = "inport: {} to outport: {}".format(inport, outport)
            for temp in self.flow:
                if(temp['id'] == flow_info["id"]):
                    self.flow.remove(temp)
                    logging.info("Duplicate flow id")
            for temp in self.flow:
                if(temp['info'] == flow_info["info"]):
                    self.flow.remove(temp)
                    logging.info("Duplicate flow data")
            self.flow.append(flow_info)
            return True
        return False
    