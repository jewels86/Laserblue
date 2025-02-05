# Cryptography & Security Notes
*Read [Proof of Performance](proof-of-performance.md) first.*
- Satellites can use Elliptic Curve Cryptography (ECC) to generate a public/private key pair.
- Satellites can sign data with the public key, and other satellites can verify it with the public key.
- Satellites are also identified by their public keys.
## Behavioral Fingerprinting
- The behavior of other nodes is tracked using fingerprints.
- Behavior is represent with a state vector $S$ that contains 4 weighted rolling metrics:
    - **Response Time**: The average amount of time a response takes (discounting distance)
- The state at any time $t$ can be represented with
    $$
    S_n = \alpha \cdot S_{n - 1} + (1 - \alpha) * S_{new}
    $$
    Where $S_{new}$ represents the changes to the state vector.
- Instead of storing behavior logs, we hash the state vector into a fingerprint:
    $$
    F_n = \text{Hash}(S_n)
    $$
- Using hashes means that if someone tries to forge a node's behavior, their fake state vector would produce an entirely different hash.
- Instead of comparing to fingerprints directly ($F_n = F_m$), we compare their drift:  
    $$
    \text{Drift} = |F_n - F_m|
    $$
    Where a small drift represents stable behavior and a large one represents erratic behavior.