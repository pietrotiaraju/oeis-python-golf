# A000805

> Permanent of a certain cyclic n X n (0,1) matrix.
> — [OEIS A000805](https://oeis.org/A000805)

Offset 0: 1, 1, 2, 6, 24, 120, 720, 1854, 4738, 12072, 30818, 79118, 204448, 528950, 1370674, 3557408, 9244418, 24043990, 62573616, 162925614, …

### Python 3 — 146 bytes

```python
P=[1,*[0]*65]*32
f=n=1
while[print(min(f,sum(P[::66])))]:f*=n;n+=1;P=[sum(P[x+x%64-d]for d in(2,4,8,16,32,64)if d&2*x>x&32)for x in range(1,2049)]
```

**The formula**

The matrix is the n×n circulant with ones in the 6 cyclic positions
j = i, i+1, …, i+5 of row i (the OEIS comment and
[A008305](https://oeis.org/A008305)), so a(n) counts the permutations σ of
ℤ_n with σ(i) − i ∈ {0, …, 5} (mod n). For n < 6 that is every
permutation, n!.

For n ≥ 6 each displacement has one representative d_i ∈ {0, …, 5},
and σ is a permutation exactly when the periodic map i ↦ i + d_(i mod n) is
a bijection of ℤ. Scan ℤ from left to right; the state at i is the set c of
offsets j ∈ {0, …, 4} whose target i + j is already taken by a source
before i. Source i takes a free offset t ∉ c; target i must be taken by then
(nothing later can reach it), so b = c ∪ {t} contains 0, and the next state
is b shifted down by one. The state only depends on the last 5
displacements, so the bijective period-n maps are exactly the closed walks
of length n in this 32-state graph:

a(n) = tr(Tⁿ)  (n ≥ 6).

For n < 6 every permutation still has such a lift, so tr(Tⁿ) ≥ n! there,
and a(n) = min(n!, tr(Tⁿ)) for every n. (tr(Tⁿ) is also the number of
juggling sequences of period n with throws 0 … 5.)

**How it works**

- `P` holds Tⁿ: the number of walks from s to e sits at `P[64*s+2*e]`; the
  odd places are leftovers that are never read. Row s starts as the unit
  vector, `[1,*[0]*65]*32`, and the trace is `sum(P[::66])`.
- The step pulls from predecessors. With b = 2e + 1, the predecessors of e
  are b minus one of its bits, as long as that stays below 32. `x` runs
  over 1 … 2048, so x = 64s + 2e + 1 and `x%64` is b; the predecessor
  b − 2ʲ sits at x + b − 2ʲ⁺¹, which is `x+x%64-d` for d = 2ʲ⁺¹.
- `d&2*x` is d when bit j of b is set and 0 otherwise. If b ≥ 32 (bit
  5 set) only j = 5 keeps the predecessor below 32, and then d is
  the largest power: so the test is `d&2*x>x&32`.
- `f` is n!, for the min.

**Notes**

- Integer additions only, exact for every n.
- A term costs 2048 entries × 6 bit tests; the b-file's 1002 terms print in
  about 5 s on this PC (the program stops later at Python's 4300-digit
  int-to-str limit). The bar is the whole b-file.
- [A000804](../A000804/) is the same program for five ones.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 146 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000805), CC BY-SA 4.0.
