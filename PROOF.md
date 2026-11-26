# Geometric readout sequences for pretty good state transfer

**Byline:** Chain.Ren · Independent research

**Version:** [proof-v1.0.1](https://github.com/Asakitan/pgst-geometric-readout/releases/tag/proof-v1.0.1) · version date: 2026-11-26 (Australia/Sydney); see the release for the actual publication timestamp.

OpenAI Codex provided substantive assistance with the proof and reproducibility materials. This work has no institutional endorsement and has not been peer reviewed.

**Scope.** Coutinho and Guo's [Open Problem 2.4](https://doi.org/10.1515/spma-2024-0025) has two requests: decide pretty good state transfer (PGST) in polynomial time, and compute successive readout times witnessing it. The result below addresses the **readout** request, for every finite simple undirected graph and every pair with PGST for the adjacency Hamiltonian. It gives a single geometric progression of times after exact arithmetic preprocessing. It makes no polynomial-time decision or preprocessing claim, and the times may be physically very long. In particular it is not a resolution of both parts of Problem 2.4.

## Theorem

Let $A$ be the adjacency matrix of a finite simple undirected graph, $U(t)=\exp(itA)$, and $a\ne b$ vertices. Suppose the pair has PGST, equivalently $\sup_{t>0}|U(t)_{ba}|=1$. Then exact preprocessing of $A,a,b$ produces real algebraic numbers $y>0,\rho>1$, a rational number $q$, a sign $s$, and constants $C\ge0,0\le c<1$ such that
$
 t_n=\pi y\rho^n,\qquad
 \|U(t_n)e_a-s e^{i\pi q}e_b\|_2\le \pi Cc^n\quad(n\ge1).
$
In particular $1-|U(t_n)_{ba}|^2\le(\pi Cc^n)^2$, by orthogonal projection onto $e_b^\perp$. All steps below are effective for finite simple undirected graphs. No search over evolution times or numerical tolerances is part of the output rule. The same argument also applies to rational real symmetric matrices: their spectra still generate a totally real field, and the integer $H$ below clears denominators.

### 1. What the spectrum requires

Write $A=\sum_j\theta_jE_j$, keeping the distinct eigenvalues with $E_je_a\ne0$. By PGST and compactness there are times along which $U(t)e_a$ tends to $\gamma e_b$ for a fixed unit complex number $\gamma$. Applying the orthogonal projections $E_j$ shows that $a,b$ have identical spectral supports, and their real projection vectors have equal lengths and differ only by a sign $s_j$: $E_je_b=s_j E_je_a$. Indeed the corresponding complex scalar along the sequence must approach a value sending one nonzero real vector to another of equal length, which is $+1$ or $-1$. Along that sequence $e^{it\theta_j}\to\gamma s_j$.

Fix a supported eigenvalue $\theta_0$; put $\delta_j=\theta_j-\theta_0$ and choose $b_j\in\{0,1\}$ with $(-1)^{b_j}=s_j/s_0$. Every integral relation $\sum_j m_j\delta_j=0$ gives $\sum_jm_jb_j=0\bmod 2$, by taking the limit of the product of the relative phases to powers $m_j$. Consequently $\delta_j\mapsto b_j\bmod2$ induces a well-defined homomorphism on the additive lattice $L=\sum_j\mathbb Z\delta_j$. This lattice is finitely generated and torsion-free, hence free. On an integer basis lift each value of that homomorphism to 0 or 1, obtaining an integer-valued $\ell:L\to\mathbb Z$ with $\ell(\delta_j)\equiv b_j\pmod2$.

### 2. Packaging all phases into a single algebraic coefficient

Take $K$ to be the splitting field of the characteristic polynomial of $A$, with its given embedding into $\mathbb R$. It is totally real: each image of a generating root is another eigenvalue of the real symmetric matrix. Extend $\ell$ first to the rational span of $L$ and then to a rational-linear functional on $K$. The integer basis of $L$ is also rationally independent, so this extension is consistent. The trace pairing is nondegenerate (in this totally real case $\operatorname{Tr}(z^2)>0$ for nonzero $z$), hence there is a unique $x\in K$ representing the chosen extension:
$
 \ell(z)=\operatorname{Tr}_{K/\mathbb Q}(xz).
$
Both signs $s_j$ occur, because otherwise $e_a=\pm e_b$. Thus $x\ne0$. Replace $x$ by $-x$ if needed so its distinguished real value $y=x$ is positive. This preserves all parities. Put $q_j=\operatorname{Tr}(x\theta_j)$; these rational numbers satisfy $q_j-q_0\equiv b_j\bmod2$, where this congruence means their difference from $b_j$ is an even integer. Choose a positive integer $H$ with $Hx\theta_j$ an algebraic integer for every $j$.

### 3. Choosing the geometric ratio

If $K=\mathbb Q$, use $\rho=1+2H$, and set $C=c=0$. Suppose $[K:\mathbb Q]=d>1$. We need an algebraic integer $\rho$ satisfying
$
 \rho>1,\qquad |\sigma(\rho)|<1\quad(\sigma\ne\mathrm{id}),\qquad
 \rho\equiv1\pmod{2H\mathcal O_K}.
$
For completeness, Dirichlet's unit theorem says that the logarithms of the absolute values of the $d$ real embeddings of units form a full lattice in the hyperplane of coordinate sum zero. This lattice meets the open cone whose distinguished coordinate is positive and all others negative: take a large multiple of $(d-1,-1,\ldots,-1)$ and subtract a bounded error from a fundamental parallelepiped. Square the resulting unit to make its distinguished embedding positive. Its residue belongs to the finite group of units modulo $2H\mathcal O_K$, so some positive power is 1 modulo $2H\mathcal O_K$. That power is an admissible $\rho$.

No effective form of the unit theorem is necessary. Enumerate integer coefficient vectors in an integral basis of $\mathcal O_K$, in increasing sup norm, and test $\rho=1+2H\sum_i z_i\omega_i$ for the strict inequalities above by exact real algebraic comparisons. Existence guarantees termination. The first admissible element need not be a unit; only the three displayed properties are used.

### 4. Exact congruence, exponentially decreasing error

For any $n\ge1$, $\rho^n-1\in 2H\mathcal O_K$. Therefore
$
 \operatorname{Tr}(x\theta_j\rho^n)-q_j\in 2\mathbb Z.
$
Here the trace of an algebraic integer is an integer, and $Hx\theta_j$ is integral by construction. Set $c=\max_{\sigma\ne\mathrm{id}}|\sigma(\rho)|<1$, $C=\max_j\sum_{\sigma\ne\mathrm{id}}|\sigma(x\theta_j)|$, with empty maxima/sums for the other embeddings interpreted as zero in degree 1. The distinguished term of the trace satisfies
$
 \left|x\theta_j\rho^n-\operatorname{Tr}(x\theta_j\rho^n)\right|\le Cc^n.
$
Using $|e^{iu}-e^{iv}|\le|u-v|$, each phase $e^{it_n\theta_j}$ differs from $e^{i\pi q_0}s_j/s_0$ by at most $\pi Cc^n$. The vectors $E_je_a$ are pairwise orthogonal with total squared norm 1. Recombining the spectral components proves the claimed norm estimate with $q=q_0,\ s=s_0$.

**Algorithmic detail.** Algebraic real roots and spectral projections can be encoded exactly (use the polynomial interpolation formula for $E_j$); construct the splitting field by successive adjunctions of roots. In a rational basis of the field, columns for $\delta_j$ have rational entries. After clearing a common denominator, integer normal form computes a basis for their column lattice and the corresponding integer combinations, hence also each basis element's prescribed parity. Complete the resulting basis to a rational basis of $K$ and solve the nonsingular trace system by rational linear algebra. Integrality, an integral basis, and algebraic signs are computable. The splitting field can be large. The proof also explains why a naive positive-time approximation algorithm exists under the PGST promise: one could enumerate rational times and certify a strict fidelity target. The stronger assertion here is **one geometric progression for all accuracies**, with a proved rate and no repeated fidelity search.

## A short example: the four-site spin chain

Let $\varphi=(1+\sqrt5)/2$. The eigenvalues of $P_4$ in descending order are $\varphi,\varphi-1,1-\varphi,-\varphi$. Their field traces are alternately $1,-1,1,-1$, and the endpoint projections have the same sign pattern, by $\sin(4k\pi/5)=(-1)^{k+1}\sin(k\pi/5)$. Since $\varphi^6=8\varphi+5\equiv1\bmod4$ and $|\varphi'|=1/\varphi<1$, the explicit times
$
 t_n=(\pi/2)\varphi^{6n}
$
obey $U(t_n)e_1\to i e_4$. The trace of $\theta_k\varphi^{6n}$ differs from the trace of $\theta_k$ by a multiple of 4, while the omitted conjugate has absolute value at most $\varphi^{1-6n}$. The transfer-state norm error is at most $(\pi/2)\varphi^{1-6n}$. This example illustrates the construction.

As a direct numerical check, at 105 decimal digits, summing the standard path expression
$
 U(t)_{4,1}=\frac25\sum_{k=1}^4 \sin(k\pi/5)\sin(4k\pi/5)\exp[2it\cos(k\pi/5)]
$
gave the following **infidelities**, not a numerical proof:

| $n$ | $1-|U(t_n)_{4,1}|^2$ |
|---:|---:|
| 1 | 0.015242639162912 |
| 2 | 0.000047594751421336 |
| 4 | $4.5905319842097\times10^{-10}$ |

## Prior art and limits

- [Coutinho–Guo, Problem 2.4](https://doi.org/10.1515/spma-2024-0025) is the open-problem record. [Banchi et al.](https://arxiv.org/abs/1608.04722) develop spectral/arithmetic PGST criteria.
- [Jonckheere, Langbein and Schirmer](https://arxiv.org/abs/1408.3765) already use simultaneous Diophantine approximation and LLL variants to estimate readout times. [Kirkland–van Bommel](https://arxiv.org/abs/2406.15289) give explicit times for concrete tree families.
- On 2026-11-26 the targeted search covered terms including “pretty good state transfer sequence of times algorithm”, “Pisot units pretty good state transfer”, “algebraic conjugates quantum spin network readout times”, and “simultaneous Diophantine approximation transfer fidelity parity”. No primary source found in that search stated the **all-finite-undirected-graphs geometric readout theorem** above. The Pisot trace mechanism is classical algebraic number theory. No claim of efficient or time-optimal physical transfer, experimental validation, or independent peer review.
