# Laserblue Structure
## Overview
**Laserblue** operates as a decentralized network, meaning there are no central nodes (satellites).
There are three types of nodes in the Laserblue network: gateway nodes, beacon nodes, and satellite nodes.
### Gateways
**Gateway nodes** in Laserblue are satellites that have a maser on them. 
These nodes facilitate long-range communication when there is no other path to a target node. 
Although masers do have a lower data rate and higher latency than lasers, they are much more reliable than lasers other long distances. 

### Beacons
Laserblue **beacons** are nodes that stay semi-stationary using Lagrange points. 
Any other node can always contact one to enter the network, or to establish a connection with any other node.

### Satellites
**Satellites** are the main components of the Laserblue network.
Satellites are always connected to node degree $d$ other satellites via laser. 
They use beacon nodes to establish these connections.