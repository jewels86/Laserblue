# Proof Of Performance Notes
- In a **Proof of Performance** (**PoP**) system, nodes earn credibility by completing verifiable tasks that contribute to the network's operation.
## Tasks
- In PoP systems, the network maintains a list of tasks that need to be completed. 
These tasks are created by nodes and are assigned via zero-knowledge calculations.
- Tasks are weighted by priority and age.
## Validation & Accuracy
- All task results are cryptographically signed to prove authenticity and prevent tampering.
- Multiple nodes return results for a task, and their outputs are compared to ensure accuracy.
- In some cases, the final result may be the weighted average of the individual results based on reputation. In others, all results or the result from the node with highest accuracy may be accepted.
## Reputation
- Nodes gain reputation based on performance, accuracy, and reliability.
- Incorrect or delayed results can negatively affect a node's reputation.
- Every node holds a DAG representing the reputations of other nodes.
