# Defaults overridden by pathman_ini.py
odl_user = 'admin'
odl_password = 'admin'
odl_ip = '192.168.56.4'
odl_port = '8181'
odl_name = 'flow:1'

# URI
test_server_uri = "http://{}:{}/index.html"
auth_uri = 'http://{}:{}/restconf/operational/network-topology:network-topology'

get_topo_uri = 'http://{}:{}/restconf/operational/network-topology:network-topology/topology/%s' %(odl_name)
get_pcep_uri = 'http://%s:%s/restconf/operational/network-topology:network-topology/topology/pcep-topology' %(odl_ip, odl_port)
get_nodes_uri = 'http://%s:%s/restconf/config/opendaylight-inventory:nodes' %(odl_ip, odl_port)
get_node_topo_uri = 'http://%s:%s/restconf/operational/network-topology:network-topology/topology/topology-netconf' %(odl_ip, odl_port)
get_node_config_uri = 'http://%s:%s/restconf/config/network-topology:network-topology/topology/topology-netconf/node/{node}/yang-ext:mount/' %(odl_ip, odl_port)
# flow id
del_flow_table_node_template_uri = 'http://{}:{}/restconf/config/opendaylight-inventory:nodes/node/{}/flow-node-inventory:table/{}/flow/{}'
# table id
del_flow_node_template_uri = 'http://{}:{}/restconf/config/opendaylight-inventory:nodes/node/{}/flow-node-inventory:table/{}'
add_flow_table_node_template_uri = 'http://{}:{}/restconf/config/opendaylight-inventory:nodes/node/{}/flow-node-inventory:table/{}/flow/{}'

add_flow_port_template_json = '''
{
    "flow": [
        {
            "id": "@id@",
            "match": {
                "in-port": "@inport@"
            },
            "instructions": {
                "instruction": [
                    {
                        "order": "0",
                        "apply-actions": {
                            "action": [
                                {
                                    "output-action": {
                                        "output-node-connector": "@outport@"
                                    },
                                    "order": "0"
                                }
                            ]
                        }
                    }
                ]
            },
            "priority": "@priority@",
            "idle-timeout": "0",
            "hard-timeout": "0",
            "table_id": "0"
        }
    ]
}
'''