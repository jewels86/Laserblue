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