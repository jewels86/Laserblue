# Laserblue Process
This is an example network process to help you get an idea of what Laserblue does.
## Parameters
- $d = \lceil\frac{1}{2}\log N\rceil$
- Reputation Weights
    - $\alpha = 0.7$
    - $\beta = 0.15$
    - $\gamma = 0.1$
    - $\delta = 0.15$
- Beacon Points (in order of reliability): [L4, L5, L1]

Remember that all nodes, even ones who haven't joined yet, know these parameters because Laserblue acts as a single network.
## First Nodes $S_1$, $G_1$, and $B_1$
Where S, G, and B represent satellite, gateway, and beacon respectively. 

Imagine we have a network around the Earth with our first beacon at Lagrange point L4 when considering the Earth and Moon. 

Now lets say node $S_2$ just launched into orbit and wants to join the network. 
First, it'll generate it's own keypair, vrf seed, and GUID:
- Public key = $K_{2pub}$
- Private key = $K_{2priv}$
- VRF seed = $s_2$
- GUID = $G_2$

Then, $S_2$ will send a join request to $B_1$:

```json
{
    "type": "jreq", // "jreq" meaning "join request"
    "pos": [x, y, z] // general xyz position of the satellite relative to the star
}
```
In CBOR format.

$B_1$ will receive this and check for some of the nodes that have good reputation and are close by to $S_2$. Once it finds some, it will pick $d$ nodes randomly with it's VRF and reply to $S_2$ with:

```json
{
    "type": "jres",
    "params": {
        
    }
}
```