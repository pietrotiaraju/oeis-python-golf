# A001323

> Number of equivalence classes of 3-valued Post functions of n variables under action of semi-direct product of symmetric group S_n and complementing group C(n,3).
> — [OEIS A001323](https://oeis.org/A001323)

Offset 1: 11, 1230, 47093135946, 228100045393047605442978104423211474, …

A 3-valued Post function of n variables is any map {0,1,2}ⁿ → {0,1,2}. The
complementing group C(n,3) shifts each variable by its own constant,
xᵢ ↦ xᵢ + cᵢ (mod 3), and Sₙ permutes the variables; together they form the
group Sₙ ⋉ Z₃ⁿ of order n!·3ⁿ acting on the 3ⁿ points, and the classes are
the orbits. For n = 1, Burnside's lemma gives (27 + 3 + 3)/3 = 11 as in the
entry (the reflection x ↦ 2 − x would give 18); brute force over the group
gives 11, 1230, 47093135946 and a(4) as well.

### Python 3 — 203 bytes

```python
from math import*
f=lambda r,*L:r and sum(f(r+~v//3,*L,~v)for v in range(3*r))//r//3or 3**(sum(prod((t//(g:=gcd(t,v//3))*v%3<1)*3**g for v in L)for t in range(N))//N)
N=3;n=1
while[print(f(n))]:n+=1;N*=n
```

**What is counted**

- Burnside's lemma: a(n) = Σ_g 3^c(g) / (n!·3ⁿ), where c(g) is the number
  of cycles of g = (σ, c) on the 3ⁿ points.
- Take a cycle of σ of length l whose shifts add up to s (mod 3). gᵗ moves
  the points of that block in gcd(t,l) chains, and going once round a chain
  adds (t/gcd(t,l))·s, so gᵗ fixes 3^gcd(t,l) values of the block when
  (t/gcd(t,l))·s ≡ 0 (mod 3) and none otherwise. The fixed points of gᵗ are
  the product over the blocks.
- The order of g divides 3·lcm(L), hence 3·n!, so Burnside's lemma for ⟨g⟩
  gives c(g) = (1/N) Σ_{t<N} fix(gᵗ) with N = 3·n!.

**How it works**

- `f(r,*L)` averages over the elements of Z₃ ≀ Sᵣ on r further variables,
  as in [A001321](../A001321/): the cycle through one of them has length
  l = 1…r with probability 1/r, and its shift sum s is uniform on Z₃, so
  f(r,L) = Σ_{l,s} f(r−l, L+[(l,s)]) / (3r).
- A cycle is one number v = `~j` for j in `range(3*r)`: v runs over
  −3r…−1, `v//3` = −l takes each value three times, and v ≡ s (mod 3)
  runs over all three sums. In the leaf `gcd(t,v//3)` is gcd(t,l), and
  `t//g*v%3<1` tests (t/g)·s ≡ 0 (mod 3).
- At r = 0 the product over the cycles is fix(gᵗ), and the sum over
  t < N, with N = 3·n! kept by the loop, divided by N is c(g).
- The floors are exact: by de Bruijn's lemma each level is the number of
  orbits of Z₃ ≀ Sᵣ that the element already chosen maps to themselves, an
  integer.

**Notes**

- Since only s = 0 against s ≠ 0 matters mod 3, cycles can also be stored
  signed with weight 2 for s ≠ 0 (the [A000616](../../A000xxx/A000616/)
  style): 214 bytes.
- The 5 b-file terms print in under a second; a(6) takes about 20 s. a(9)
  has more than 4300 digits, so printing it would stop the program with
  Python's int-to-str limit.
- The b-file is synthesized from the 5 terms of the entry; the bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 203 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001323), CC BY-SA 4.0.
