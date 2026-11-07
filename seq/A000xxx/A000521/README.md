# A000521

> Coefficients of modular function j as power series in q = e^(2 Pi i t). Another name is the elliptic modular invariant J(tau).
> — [OEIS A000521](https://oeis.org/A000521)

Offset -1: 1, 744, 196884, 21493760, 864299970, 20245856256, 333202640600, 4252023300096, 44656994071935, 401490886656000, …

### Python 3 — 116 bytes

```python
A=[1];r=[1]
for n in r:print(A[-1]);A+=sum((504*d*d-240*(n+~k))*d**3*A[-k]for d in r for k in r[d-1::d])//n,;r+=n+1,
```

**How it works**

- j = E₄³/Δ with E₄ = 1 + 240·Σ σ₃(k)q^k, E₆ = 1 − 504·Σ σ₅(k)q^k and
  Δ = q·∏(1 − q^k)²⁴. Write θ = q·d/dq. Ramanujan's identities
  θE₄ = (E₂E₄ − E₆)/3 and θΔ = E₂Δ give
  θj = (3E₄²·θE₄ − E₄³·E₂)/Δ = −E₄²E₆/Δ, that is θj·E₄ = −j·E₆.
- Comparing the coefficients of q^n in θj·E₄ + j·E₆ = 0 gives the
  recurrence in the OEIS entry (Manyama 2017), with a(m) = 0 for m < −1:

  (n+1)·a(n) = Σ_{k=1}^{n+1} (504σ₅(k) − 240(n−k)σ₃(k))·a(n−k).

  The division by n+1 is exact because the a(n) are integers.
- `A[i]` holds a(i−1). In the pass with loop value n the program appends
  A[n] = a(n−1), so the recurrence reads
  n·a(n−1) = Σ_{k=1}^{n} (504σ₅(k) − 240(n−1−k)σ₃(k))·A[n−k]. Before the
  append `A` has n entries, so `A[-k]` is A[n−k], and `n+~k` is n−1−k.
- The divisor sums are unfolded into one sum over pairs d | k:
  σ₅ and σ₃ become d⁵ and d³, so each pair adds (504d² − 240(n−1−k))·d³·A[n−k].
- `r` is both the loop and the range. A `for` loop over a list sees the
  items appended to it, so `for n in r:…;r+=n+1,` runs forever with
  r = [1, …, n] during pass n. Then `for d in r` runs over 1..n and
  `r[d-1::d]` is d, 2d, 3d, … ≤ n: the multiples of d, with no
  divisibility test.
- The print comes first in the pass, so pass n prints A[n−1]; the first
  line is A[0] = 1 = a(−1).

**Notes**

- Pairs with a divisibility test, `for k in r for d in r if k%d<1`:
  117 bytes and O(n²) work per term instead of O(n log n). The
  `while[print(A[n])]:n+=1;r+=n,;…` frame with `A=[1];n=0;r=[]`: also
  117 bytes. The first entry carried an unused `from math import*`
  (156 bytes).
- Exact integer arithmetic, so the program is right for every n.
- About 3500 terms in 60 s here.
- a(n) has about 5.46·√n digits (a(n) ~ e^(4π√n)/(√2·n^(3/4))), so the
  4300-digit int-to-str limit would only stop the printing near
  n = 620000.
- The b-file has 10002 terms (up to a(10000)); the bar is 150 terms in
  60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 156 | first entry |
| 2026-11-07 | Python 3 | 116 | one sum over divisor pairs, growing list as loop and range |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000521), CC BY-SA 4.0.
