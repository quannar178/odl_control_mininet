"""
    host - switch - host
"""
from mininet.topo import Topo

class MyTopo( Topo ):
    def build( self ):
        # Add hosts and switches
        leftHost = self.addHost("h1")
        rightHost = self.addHost("h2")
        switch = self.addSwitch("s1",protocols='OpenFlow13')
        # Add links
        self.addLink(leftHost, switch)
        self.addLink(rightHost, switch)

topos = { 'mytopo': ( lambda: MyTopo() ) }
