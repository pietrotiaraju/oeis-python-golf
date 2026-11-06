# A000310

> Coefficients of iterated exponentials.
> — [OEIS A000310](https://oeis.org/A000310)

Offset 1: 1, 4, 26, 234, 2696, 37919, 630521, 12111114, 264051201, 6445170229, 174183891471, 5164718385337, …

### Python 3 — 85 bytes

```python
Q=[[t:=1]]*4
while Q:=[[t]+[t:=t+i*x for i,x in enumerate(L)]for L in Q]:print(t);t=0
```

**How it works**

- The e.g.f. is −log(1+log(1+log(1+log(1−x)))) = L(L(L(L(x)))) with
  L(y) = −log(1−y), whose coefficients are (n−1)!. Putting L inside a
  series is the unsigned Stirling transform of the first kind: if b has
  e.g.f. B(y), then B(L(x)) has coefficients Σ_j |s(n, j)|·b(j). So a(n)
  is four such transforms applied to 0, 1, 0, 0, … (the series x).
- One triangle does the transform without Stirling numbers:
  T(i, k) = Σ_j |s(i, j)|·c(j + k) has T(0, k) = c(k) and
  T(i+1, k) = i·T(i, k) + T(i, k+1), from |s(i+1, j)| = i·|s(i, j)| +
  |s(i, j−1)|, and the transform is T(n, 0). Here the weight is the row i,
  not the column as for the second kind in [A000258](../A000258/).
- The program keeps one antidiagonal per level, L = [T(0, n), T(1, n−1),
  …, T(n, 0)]. The next one starts with the head T(0, n+1) = c(n+1), and
  each entry is the one before it plus i·L[i], which
  `t:=t+i*x for i,x in enumerate(L)` computes; it ends with T(n+1, 0),
  the next term of that level. That term is the head the next level
  needs, so `t` carries over, and the fourth level ends with a(n+1).
- The innermost series x has head c(1) = 1 at the first pass and 0 after
  it: `t:=1` at the start, `t=0` after each print.
- L[0] = T(0, n) is only ever multiplied by i = 0, so its value does not
  matter. That is why the start lists can be `[1]` (standing for
  T(0, 0) = 0) and why one walrus `[[t:=1]]*4` sets both `t` and the
  four lists. The four references to one list are safe: the lists are
  only read, and each pass builds new ones.

**Notes**

- Assigning `Q` in the `while` condition, with `print(t);t=0` as the body,
  starts the output at a(1) with no extra print: 3 bytes under
  `t=1;Q=[[1,1]]*4` with `while[print(t)]:t=0;Q=…` (88 bytes).
- The number of levels is the number in `[[t:=1]]*4`: `*5` prints
  [A000359](https://oeis.org/A000359) at the same length.
- Exact integer arithmetic, so the program is right for every n. a(1374)
  is the first term with more than 4300 digits, so Python 3.11+ stops
  there with a `ValueError` from the int-to-str limit, which is not counted
  as a failure.
- The b-file has 100 terms (n = 1 to 100); they print in well under a
  second. The bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 85 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000310), CC BY-SA 4.0.
