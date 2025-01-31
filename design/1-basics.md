# Laserblue Basics
## Overview
**Laserblue** is a concept for a network that interconnects satellites. 
It uses laser and maser transmission systems to maintain data integrity while perserving speed.

The network prioritizes data speed, security, and integrity while ensuring minimal latency.
The system is designed to be scalable, allowing for easy expansion as the demand for data transmission grows. Additionally, it incorporates advanced encryption techniques to safeguard against unauthorized access and ensure that all communications remain confidential.

## Network Parameters
### Node Degree $d$
The node degree, represented as $d$, is the number of other satellites one satellite should be connected to at once. 
The node degree scales with the number of nodes in the network.
### Byzantine Tolerance $f$
Byzantine tolerance, denoted as $f$, refers to the maximum number of faulty or malicious nodes that the network can tolerate while still functioning correctly. 
The value of $f$ is determined based on the total number of nodes in the network and the specific consensus algorithm being used.
### VRF Seed Entropy $H$
The VRF seed entropy $H$ is a measure of the randomness and unpredictability of the seed used in the Verifiable Random Function (VRF). 
High entropy ensures that the seed is difficult to guess or reproduce, which is crucial for maintaining the security and integrity of the VRF. 
### Reputation Weights $\alpha$, $\beta$, $\gamma$, $\delta$
Reputation weights, denoted as $\alpha$, $\beta$, $\gamma$, and $\delta$, are parameters used to quantify the importance of different aspects of a node's behavior in the network. These weights are used to calculate the overall reputation score of a node, which influences its trustworthiness and reliability within the network.

- $\alpha$: This weight represents the importance of a node's uptime. A higher $\alpha$ value indicates that consistent availability is highly valued in the network.
- $\beta$: This weight signifies the importance of accuracy in the data provided by the node. A higher $\beta$ value means that nodes providing accurate and reliable data are more trusted.
- $\gamma$: This weight measures the importance of low latency in the node's performance. A higher $\gamma$ value indicates that nodes with faster response times are preferred.
- $\delta$: This weight accounts for penalties assigned to nodes for misbehavior or malicious activities. A higher $\delta$ value means that nodes with a history of misbehavior are more heavily penalized in their reputation score.

By adjusting these weights, the network can prioritize different aspects of node performance and behavior, ensuring that the most reliable and trustworthy nodes are given higher reputation scores.
### Epoch Length $T_{epoch}$
Epoch length, denoted as $T_{epoch}$, is the duration of a single epoch in the network. It defines the time interval during which specific operations or events are executed. The length of an epoch can vary depending on the network's requirements and the nature of the tasks being performed. 

A well-defined epoch length is crucial for maintaining synchronization and coordination among the nodes in the network. It ensures that all nodes perform their operations within the same timeframe, which helps in achieving consensus and maintaining the overall integrity of the network.

Factors influencing the choice of epoch length include the network's latency, the complexity of the operations, and the desired level of security. By carefully selecting an appropriate epoch length, the network can optimize its performance and ensure efficient and reliable operation.

## Key Concepts
### Epoches
**Epoches** represent periods of time in decentralized networks. 
In these networks, an epoch is a predefined interval during which certain operations or events occur. 
Epoches help in organizing and synchronizing activities across the network. 
They ensure that all nodes in the network are aligned in terms of the operations they perform and the data they process. 
This alignment is crucial for maintaining the integrity and consistency of the network.

### Hashing
**Hashing** is the one-way transformation of data.
Hashing is used to convert data into a fixed-size string of characters, which is typically a hash code. 
This process is deterministic, meaning the same input will always produce the same output.

### SHA-256
**SHA-256** (Secure Hash Algorithm 256-bit) is a member of the SHA-2 cryptographic hash functions designed by the NSA. 
It generates an almost-unique, fixed-size 256-bit (32-byte) hash.

### Verifiable Random Functions (VRFs)
**VRF**s are cryptographic primitives that provide proof that a value was generated in a truly random manner, ensuring both unpredictability and verifiability.

### Elliptic Curve Verifiable Random Functions (ECVRFs)
**ECVRFs** are a type of Verifiable Random Function that use elliptic curve cryptography to generate random values. 
They provide the same benefits as traditional VRFs, such as unpredictability and verifiability, but with the added advantages of elliptic curve cryptography, including smaller key sizes and faster computations. 

### Practical Byzantine Fault Tolerance
**Practical Byzantine Fault Tolerance (PBFT)** is an algorithm designed to provide high fault tolerance in distributed systems. 
PBFT ensures that a system can continue to operate correctly even if some of its components fail or act maliciously. 
It achieves consensus among distributed nodes, allowing them to agree on the state of the system despite the presence of faulty or malicious nodes. The algorithm works efficiently in asynchronous networks and can tolerate up to one-third of faulty nodes.

### Reputation Based Trust
**Reputation Based Trust** is a mechanism used to evaluate and manage the reliability of nodes within a network. 
This system assigns a reputation score to each node based on various performance metrics, including uptime, accuracy, latency, and penalties for misbehavior.

### Gossip-Based Protocols
**Gossip-Based Protocols** are a class of communication protocols used for message propagation in decentralized networks. 
These protocols mimic the way information spreads in social networks, where nodes randomly select a subset of their peers to share information with. 
Over time, the information propagates through the entire network, ensuring that all nodes receive the message.