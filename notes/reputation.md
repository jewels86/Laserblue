# Reputation Notes
*Read [Proof of Performance](proof-of-performance) and [Tasks](tasks.md) first.*
- When a task is completed, the requester broadcasts a reputation update based on:
    - Data Quality: Whether the data meets expected standards.
    - Data Accuracy: If the result can be independently verified.
    - Timeliness: How quickly the result was submitted.
- The network adjusts reputation based on the credibility of the broadcaster. Higher-reputation nodes have more influence.
- Reputation is tracked with a **Directed Acyclic Graph** (**DAG**).
- Each DAG node contains:
    - ID: The hash of the payload.
    - Timestamp: When the node was created.
    - Payload: The reputation update, including the public key of the updated node, the public key of the node updating it, and the actual increase.
    - Signature: The signature from the node updating the reputation.
    - References: Links to previous nodes, validating them.
- New nodes reference other not-yet validated nodes.
- Referencing nodes confirms them as valid, increasing trust.
- The more references a node has, the more trusted it becomes.
- High-reputation nodes carry more weight in validation.
- Conflicts are resolved by selecting the branch with the most validation weight.
- When any node evaluates another's reputation, it applies a decay function:  
    $$R(t) = R_{prev} \cdot e^{-\lambda(R_{prev})(t-t_{prev})}$$  
    $$\lambda(R_{prev}) = \lambda_{min} + (\lambda_{max} - \lambda_{min}) * e^{-kR_{prev}}$$  
    Where $\lambda(R_{prev})$ is the decay rate, which depends on past reputation $R_{prev}$ from time $t_{prev}$, $k$ is a scaling factor for smooth transitions (e.g 0.05), $\lambda_{min}$ is the minimum decay rate (e.g 0.001), and $\lambda_{max}$ is the maximum decay rate (e.g 0.1).

