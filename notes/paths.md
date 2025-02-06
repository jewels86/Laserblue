# Path-Based Messaging Notes
- Nodes use path-based messaging when communicating directly with other nodes.

## Orbital Summaries & Commitments
- Each satellite maintains an onboard model of its future orbit. Instead of sharing exact coordinates, it computes an abstract summary of its predicted trajectory over a specific time window.
- An **orbit summary** is created with a list of spherical coordinates (latitude, longitude, altitude) and the time differences between each provided waypoint.
- The satellite concatenates the orbit summary with a nonce and hashes the resulting string using SimHash, creating an **orbit commitment**. This commitment preserves similarity between trajectories while concealing precise details.
- Whenever a satellite is changing trajectories, it broadcasts its updated orbit commitment to its neighbors.
- Neighbors use these orbit commitments to build a local table of commitments, which represents the predicted paths of nearby nodes.

## Message Routing
- Suppose Satellite A wants to send a message intended for Satellite C.
- When Satellite B receives the message from Satellite A, it examines the attached orbit commitment.
- Satellite B compares the sender’s commitment with the commitments in its local table by computing the Hamming distance between the SimHash outputs.
- The neighbor whose commitment best matches (i.e., has the smallest Hamming distance) is selected as the next hop for the message.
- If no neighbor’s commitment closely aligns with the sender’s commitment (i.e., if the Hamming distances are all above a certain threshold), Satellite B will default to broadcasting the message to all its neighbors, ensuring the message is still propagated through the network.