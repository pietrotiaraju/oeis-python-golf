# A000088

> Number of simple graphs on n unlabeled nodes.
> — [OEIS A000088](https://oeis.org/A000088)

Offset 0: 1, 1, 2, 4, 11, 34, 156, 1044, 12346, 274668, 12005168, 1018997864, 165091172592, 50502031367952, 29054155657235488, …

### Python 3 — 172 bytes

```python
import math
f=lambda n,k,L,w,d=1:n>=k and f(n,k+1,L,w)+f(n-k,k,L+[k],w//k//d<<sum(math.gcd(k,j)for j in L)+k//2,d+1)or 0**n*w
n=0;F=1
while[print(f(n,1,[],F)//F)]:n+=1;F*=n
```

**How it works**

- Burnside's lemma: a(n) = (1/n!)·Σ_π 2^e(π) over the permutations π of the
  n nodes, where e(π) is the number of orbits π has on the C(n, 2) possible
  edges. e depends only on the cycle type λ of π:
  **e(λ) = Σ_{i<j} gcd(λᵢ, λⱼ) + Σᵢ ⌊λᵢ/2⌋**. Two cycles of lengths a and b
  move their a·b connecting edges in orbits of length lcm(a, b), so there are
  gcd(a, b) of them; one a-cycle has ⌊a/2⌋ orbits on its own C(a, 2) edges.
  There are n!/z_λ permutations of type λ, with z_λ = Π k^(c_k)·c_k!, so
  **a(n) = Σ_λ 2^e(λ) / z_λ** over the partitions λ of n. This is the formula
  of Andrew Howroyd's PARI program on the OEIS page.
- `f` walks the partitions with parts in nondecreasing order as a binary
  recursion. With `n` still to fill and `k` the smallest part allowed, it
  either moves on to bigger parts, `f(n,k+1,L,w)`, or takes a part k,
  `f(n-k,k,L+[k],…)`. `L` lists the parts taken so far and `d` is one more
  than the number of k's among them; moving on resets it to 1 through the
  default argument.
- `w` is 2^e·n!/z for the parts taken so far and starts at F = n!. A new part
  k adds Σ_{j∈L} gcd(k, j) + ⌊k/2⌋ to e (the shift) and contributes k·d to
  z (the c_k! grows by the factor d). Both divisions are exact: for a partial
  partition μ, z_μ divides |μ|!, which divides n!, so `w//k//d` loses nothing
  and the shift can come after it without parentheses.
- When k > n the walk stops: with n = 0 the partition is complete and its
  weight `w` counts; with 0 < n < k it is a dead end worth 0. `0**n*w` gives
  both. When n ≥ k the two branches always add up to something positive (one
  of them contains the partition that ends with the part n), so `and`/`or`
  is safe.
- The main loop keeps F = n! and prints `f(n,1,[],F)//F`.
- `import math` plus `math.gcd` is a byte shorter than `from math import*`,
  since `gcd` appears once. Counting the k's in `d` instead of with
  `-~L.count(k)` saves 3 more.

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- The work grows with the number of partitions: a(0) … a(39) print in about
  2 s and about 58 terms in 60 s. The b-file goes to n = 87, where
  p(87) = 38 887 673, out of reach of a partition sum in Python; the Python
  program on the OEIS page is about as fast as this one. The bar is 40 terms
  in 60 s.
- The recursion is about n calls deep, and a(n) ~ 2^C(n,2)/n! passes
  Python's 4300-digit int-to-str limit from n = 176; neither is reached in
  practice.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 172 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000088), CC BY-SA 4.0.
