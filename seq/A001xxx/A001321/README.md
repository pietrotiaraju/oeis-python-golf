# A001321

> Number of equivalence classes of 3-valued Post functions of n variables under action of symmetric group S_n.
> — [OEIS A001321](https://oeis.org/A001321)

Offset 1: 27, 10206, 1271126683458, 18476103676807778218052102700370958034, …

A 3-valued Post function of n variables is any map {0,1,2}ⁿ → {0,1,2}; Sₙ
permutes the variables, and the classes are the orbits.

### Python 3 — 169 bytes

```python
from math import*
f=lambda r,*L:r and sum(f(r+~k,*L,~k)for k in range(r))//r or 3**(sum(3**sum(map(gcd,L,[t]*n))for t in range(N))//N)
n=N=1
while[print(f(n))]:n+=1;N*=n
```

**What is counted**

- Burnside's lemma: there are Σ_σ 3^c(σ) / n! classes, where c(σ) is the
  number of cycles of σ on the 3ⁿ points of {0,1,2}ⁿ.
- If σ has cycle lengths L, σᵗ splits a cycle of length l into gcd(t,l)
  cycles and fixes the 3^Σgcd(t,l) points that are constant on them.
  Burnside's lemma for ⟨σ⟩ gives c(σ) = (1/N) Σ_{t<N} 3^Σgcd(t,l) for any
  multiple N of the order of σ; N = n! is one for every σ in Sₙ.

**How it works**

- `f(r,*L)` is the recursion of [A000612](../../A000xxx/A000612/): it
  averages over the permutations of r further points by the length of the
  cycle through one of them (each length 1…r has probability 1/r), so
  f(r,L) = Σ_k f(r−k, L+[k]) / r. The lengths are stored as `~k` for
  k in `range(r)`, that is −1…−r; `gcd` ignores the sign.
- At r = 0 the leaf is 3^c(σ): `map(gcd,L,[t]*n)` pairs t with every
  cycle (there are at most n), and the loop keeps N = n!.
- The floors are exact: by de Bruijn's lemma each level is the number of
  Sᵣ-orbits that the permutation already chosen maps to themselves, an
  integer, and the leaf is an integer cycle count.

**Notes**

- `lcm(*L)` in place of N, which the loop then need not keep, is 175
  bytes.
- The recursion has 2ⁿ⁻¹ leaves of n! terms each: the 5 b-file terms print
  at once and a(8) takes about 7 s. a(9) has more than 4300 digits
  (3^(3⁹) has 9392), so printing it would stop the program with Python's
  int-to-str limit.
- The b-file is synthesized from the 5 terms of the entry; the bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 169 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001321), CC BY-SA 4.0.
