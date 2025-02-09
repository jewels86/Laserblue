# Cryptography & Security Notes
*Read [Proof of Performance](proof-of-performance.md) first.*
- Satellites use Elliptic Curve Cryptography (ECC) to generate a public/private key pair.
- Satellites can sign data with the private key, and other satellites can verify it with the public key.
- Satellites are identified by their public keys.
## Behavioral Fingerprinting
- The behavior of other nodes is tracked using fingerprints.
- Behavior is represented with a state vector $S$ that contains 4 weighted rolling metrics:
    - **Response Time $T_{res}$**: The average response time, adjusted for expected propagation and distance delay.
    - **Message Frequency $M$**: The average frequency at which the node communicates.
    - **Dropped Messages $D$**: How often messages fail to be delivered.
    - **Uptime $U$**: How often the node is online and reachable.
    - **Flag count $F$**: Set as 1 by default, but switched to 0 if flags are raised (e.g node disconnects randomly, starts to spam, etc).
    
    These metrics are packaged into a vector as\
    $$S = [T_{res}, M, D, U, F]$$
- The state at any time $n$ can be represented with
    $S_n = \alpha \cdot S_{n - 1} + (1 - \alpha) * S_{new}$
    Where $S_{new}$ represents the new state vector and $\alpha$ is a smoothing factor.
- Instead of storing behavior logs, we hash the state vector into a fingerprint:
    $$
    F_n = \text{SimHash}(S_n)
    $$
- SimHash enables compact storage and efficient similarity comparison, as it preserves approximate relationships between state vectors.
- Instead of comparing to fingerprints directly ($F_n = F_m$), we compare their drift:  
    $$
    \text{Drift} = \frac{\text{HammingDistance}(F_n, F_m)}{t_m - t_n}
    $$
    Where the hamming distance is the number of differing bits in the SimHash outputs, and where a small drift represents stable behavior and a large one represents erratic behavior.