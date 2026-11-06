# A000496

> Restricted permutations.
> — [OEIS A000496](https://oeis.org/A000496)

Offset 0: 1, 1, 2, 6, 24, 44, 80, 144, 260, 476, …

**Status:** the program uses the rational generating function marked
conjectural in the OEIS entry. Its integer recurrence is exact for
that series; the interpretation as restricted permutations has the
same unresolved qualification.

### Python 3 — 70 bytes

```python
a=[1,1,2,6,24,44,80,144,260]
while[print(a.pop(0))]:a+=[2*a[-1]-a[-4]]
```

**How it works**

- The rational series recorded by Plouffe describes the tail:

  Σₘ≥₀ a(m+4)xᵐ=
  (24−4x−8x²−16x³−4x⁴)/(1−2x+x⁴).

- Multiplying by the denominator gives the first five tail
  coefficients 24,44,80,144,260. Beyond its numerator's
  degree four, the coefficient equation is
  **a(n)=2a(n−1)−a(n−4), for n≥9**.
- The list starts with a(0) through a(8), including the prefix
  1,1,2,6 before the rational tail. Applying the homogeneous
  recurrence too early would fail: at n=8 it would give
  2·144−24=264 instead of the required 260.
- `a.pop(0)` prints and removes the oldest queued term. After
  that removal, `a[-1]` and `a[-4]` are the entries needed
  to append the next term, starting with a(9)=2·260−44=476.
- Each iteration removes one entry and appends one, so the queue
  stays nine entries long. `[print(...)]` is a nonempty list
  and keeps the loop running independently of the printed value.

**Notes**

- **Conjectural status.** The OEIS explicitly labels Plouffe's
  generating function as conjectured. The program computes its
  coefficients exactly and matches the b-file; identifying those
  coefficients with the restricted-permutation count at every later
  index remains conditional on that generating function.
- The nine constants supply the finite prefix and the initial
  conditions forced by the rational numerator. They do not embed
  the reference file, and the recurrence produces every later value.
- A fixed-size queue and two arithmetic operations extend each
  term. The growing integer output eventually reaches Python 3.11+'s
  default 4300-digit conversion limit, an interpreter limit separate
  from the conjectural mathematical interpretation.
- The b-file has 1001 terms (indices 0 through 1000). The bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 70 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000496), CC BY-SA 4.0.
