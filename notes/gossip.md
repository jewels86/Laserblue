# Gossip Broadcasting Notes
*Read [Cryptography & Security](cryptography.md) first.*
- Gossip-based message propagation mimics the way information spreads in social networks.
- Nodes connect to a limited number of peers, with a maximum of the network node degree $d$.
- When a message needs to be broadcasted, a node sends it to a random subset of its connected peers.
- Each receiving node forwards the message to its own peers, repeating the process until the entire network is reached.
- Messages are assigned a TTL (Time-To-Live) to prevent infinite loops.
- Nodes track seen messages using their cryptographic hash to avoid redundant processing.
- Messages are cryptographically signed to prevent forgery.
- Nodes accept all messages unless the sender’s reputation drops below a threshold.
- If a sender’s reputation deteriorates further, nodes will temporarily stop accepting their messages for a set duration.
- Spamming or forgery damages a node's reputation.