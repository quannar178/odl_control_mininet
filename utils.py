import os, re, time, sys
import requests
import json
import logging
import logging.config
from constants import test_server_uri

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

def get_url(url , odl_ip, odl_port, odl_user,odl_password):
    '''request url'''
    headers = {'Content-type': 'application/json'}
    try:
        url = url.format(odl_ip, odl_port)
        logging.info("Url %s" %url)
        response =  requests.get(url, headers = headers, auth = (odl_user,odl_password), verify=False)
        logging.info("Url get Status: %s" % response.status_code)

        if response.status_code in [200]:
            return True, response.json()
        else:
            logging.info(str(response.text))
            return False, {}
    except requests.exceptions.ConnectionError as e:
        logging.error('Connection Error: %s' % e.message)
        return False, {}

def putUrl(url, data):
    # print response.text
    # data type json.
    try:
        response = requests.put(url, json=data, auth=(odl_user, odl_password), headers={'Content-Type': 'application/json'})
        logging.info("Url put Status: %s" % response.status_code)

        if response.status_code in [200]:
            return True
        else:
            logging.info(str(response.text))
            return False
    except requests.exceptions.ConnectionError as e:
        logging.error('Url put Error: %s' % e.message)
        return False

def delUrl(url):
    """ delete url """
    headers = {'Content-type': 'application/json'}
    try:
        response = requests.delete(url, auth=(odl_user, odl_password), headers={'Content-Type': 'application/json'})
        logging.info("Url delete Status: %s" % response.status_code)

        if response.status_code in [200]:
            return True
        else:
            logging.info(str(response.text))
            return False
    except requests.exceptions.ConnectionError as e:
        logging.error('Url delete Error: %s' % e.message)
        return False

def node_structure(my_topology):
    """ learn (print out) the topology structure """

    node_list = []
    try:
        node_dictlist = my_topology['topology'][0]['node']
    except:
        logging.info("We don't have any node.")
        return []
    node_list = node_dictlist
    # for nodes in my_topology['topology'][0]['node']:
    #     #try:
    #     node_ports = []
    #     if 'termination-point' in nodes.keys():
    #         for link in nodes['termination-point']:
    #             logging.debug("port: %s " % link['tp-id'])
    #             if 'tp-id' in link.keys():
    #                 port_dict = link['tp-id']
    #                 if 'ipv4' in port_dict.keys():
    #                     node_ports.append(port_dict['ipv4'])
    #     else:
    #         logging.error("Node {0} is missing 'termination-point' ".format(nodes['node-id']))
    #     # node = Node(name,node_dict['router'],router_id,node_ports,pcc, pcep_type, prefix_array, sid)
    #     logging.info("New node: %s" % str(nodes))
    #     node_list.append(nodes)
    logging.info(node_list)
    return node_list

def is_server_open(odl_ip, odl_port):
    headers = {'Content-type': 'application/json'}
    try:
        url = test_server_uri.format(odl_ip, odl_port)
        logging.info("url %s" %url)
        response =  requests.get(url)
        logging.info("Url get Status: %s" % response.status_code)

        if response.status_code in [200]:
            logging.info("SERVER IS OPENNING")
            return True
        else:
            logging.info("SERVER IS CLOSING")
            return False
    except Exception as e:
        logging.info("SERVER IS CLOSING")
        return False

def is_auth(url , odl_ip, odl_port, odl_user,odl_password):
    '''request url'''
    headers = {'Content-type': 'application/json'}
    try:
        url = url.format(odl_ip, odl_port)
        logging.info("Url %s" %url)
        response =  requests.get(url, headers = headers, auth = (odl_user,odl_password), verify=False)
        logging.info("Url get Status: %s" % response.status_code)

        if response.status_code in [200]:
            return True
        else:
            logging.info(str(response.text))
            return False
    except Exception as e:
        logging.error('Connection Error: %s' % e.message)
        return False