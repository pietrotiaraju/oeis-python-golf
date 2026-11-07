# A000406

> Coefficients of iterated exponentials.
> — [OEIS A000406](https://oeis.org/A000406)

Offset 1: 1, 6, 57, 741, 12244, 245755, 5809875, 158198200, 4877852505, 168055077875, …

### Python 3 — 85 bytes

```python
Q=[[t:=1]]*6
while Q:=[[t]+[t:=t+i*x for i,x in enumerate(L)]for L in Q]:print(t);t=0
```

The e.g.f. in the entry is −log(1+log(1+log(1+log(1+log(1+log(1−x)))))),
that is, six nested copies of H(y) = −log(1−y).

**How it works**

- Substituting H into an e.g.f. with coefficients c(k) gives the unsigned
  Stirling transform of the first kind, b(n) = Σ_k |s(n, k)|·c(k). So a(n)
  is six such transforms applied to the series x: c = 0, 1, 0, 0, … .
- One transform runs on T(i, k) = Σ_j |s(i, j)|·c(j + k), which satisfies
  T(0, k) = c(k) and T(i+1, k) = i·T(i, k) + T(i, k+1) (from
  |s(i+1, j)| = i·|s(i, j)| + |s(i, j−1)|); the left edge T(n, 0) is b(n).
- Each list `L` holds an antidiagonal T(0, n), T(1, n−1), …, T(n, 0). The
  next one starts with the new input T(0, n+1) = `t`, and its entry i + 1
  is the entry before it plus i·T(i, n−i): that is `t:=t+i*x` over
  `enumerate(L)`. Its last value T(n+1, 0) is the level's new output.
- `t` carries that output into the next list as its input, so the six
  lists chain the six transforms. For the innermost series x the input is
  1 at the first pass (`t:=1`) and 0 afterwards (`t=0` after each print).
- `Q=[[t:=1]]*6` is six references to one list, which is safe because the
  lists are only read and then replaced. Their stand-in first entry 1
  (really c(0) = 0) is only ever multiplied by i = 0.
- The new `Q` is assigned in the `while` condition, and a non-empty list
  is true, so each pass computes a row and then prints it, starting at
  a(1).

**Notes**

- Same program as [A000310](../A000310/) (four levels) and
  [A000359](../A000359/) (five); [A000405](../A000405/) is the
  second-kind (exponential) analogue, whose weights run downwards.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 100 terms (up to a(100)) and prints in about 0.1 s; the
  bar is the whole b-file in 60 s.
- a(1321) is the first term with more than 4300 digits, so printing stops
  there, after about 10 s here.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 85 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000406), CC BY-SA 4.0.
