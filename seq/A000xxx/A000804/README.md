# A000804

> Permanent of a certain cyclic n X n (0,1) matrix.
> — [OEIS A000804](https://oeis.org/A000804)

Offset 0: 1, 1, 2, 6, 24, 120, 265, 579, 1265, 2783, 6208, 13909, 31337, 70985, 161545, 369024, 845825, 1944295, 4480285, 10345391, …

### Python 3 — 142 bytes

```python
P=[1,*[0]*33]*16
f=n=1
while[print(min(f,sum(P[::34])))]:f*=n;n+=1;P=[sum(P[x+x%32-d]for d in(2,4,8,16,32)if d&2*x>x&16)for x in range(1,513)]
```

**The formula**

The matrix is the n×n circulant with ones in the 5 cyclic positions
j = i, i+1, …, i+4 of row i (the OEIS comment and
[A008305](https://oeis.org/A008305)), so a(n) counts the permutations σ of
ℤ_n with σ(i) − i ∈ {0, …, 4} (mod n). For n < 5 that is every
permutation, n!.

For n ≥ 5 each displacement has one representative d_i ∈ {0, …, 4},
and σ is a permutation exactly when the periodic map i ↦ i + d_(i mod n) is
a bijection of ℤ. Scan ℤ from left to right; the state at i is the set c of
offsets j ∈ {0, …, 3} whose target i + j is already taken by a source
before i. Source i takes a free offset t ∉ c; target i must be taken by then
(nothing later can reach it), so b = c ∪ {t} contains 0, and the next state
is b shifted down by one. The state only depends on the last 4
displacements, so the bijective period-n maps are exactly the closed walks
of length n in this 16-state graph:

a(n) = tr(Tⁿ)  (n ≥ 5).

For n < 5 every permutation still has such a lift, so tr(Tⁿ) ≥ n! there,
and a(n) = min(n!, tr(Tⁿ)) for every n. (tr(Tⁿ) is also the number of
juggling sequences of period n with throws 0 … 4.)

**How it works**

- `P` holds Tⁿ: the number of walks from s to e sits at `P[32*s+2*e]`; the
  odd places are leftovers that are never read. Row s starts as the unit
  vector, `[1,*[0]*33]*16`, and the trace is `sum(P[::34])`.
- The step pulls from predecessors. With b = 2e + 1, the predecessors of e
  are b minus one of its bits, as long as that stays below 16. `x` runs
  over 1 … 512, so x = 32s + 2e + 1 and `x%32` is b; the predecessor
  b − 2ʲ sits at x + b − 2ʲ⁺¹, which is `x+x%32-d` for d = 2ʲ⁺¹.
- `d&2*x` is d when bit j of b is set and 0 otherwise. If b ≥ 16 (bit
  4 set) only j = 4 keeps the predecessor below 16, and then d is
  the largest power: so the test is `d&2*x>x&16`.
- `f` is n!, for the min.

**Notes**

- Integer additions only, exact for every n.
- A term costs 512 entries × 5 bit tests; the b-file's 1001 terms print in
  about 1 s on this PC (the program stops later at Python's 4300-digit
  int-to-str limit). The bar is the whole b-file.
- [A000805](../A000805/) is the same program for six ones.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 142 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000804), CC BY-SA 4.0.
