# A000359

> Coefficients of iterated exponentials.
> — [OEIS A000359](https://oeis.org/A000359)

Offset 1: 1, 5, 40, 440, 6170, 105315, 2120610, 49242470, 1296133195, 38152216495, 1242274374380, …

### Python 3 — 85 bytes

```python
Q=[[t:=1]]*5
while Q:=[[t]+[t:=t+i*x for i,x in enumerate(L)]for L in Q]:print(t);t=0
```

**How it works**

- The e.g.f. is −log(1+log(1+log(1+log(1+log(1−x))))), five nested
  copies of L(y) = −log(1−y), whose coefficients are (n−1)!. Putting L
  inside a series is the unsigned Stirling transform of the first kind:
  B(L(x)) has coefficients Σ_j |s(n, j)|·b(j). So a(n) is five such
  transforms applied to 0, 1, 0, 0, … (the series x).
- This is the program of [A000310](../A000310/) (four copies of L) with
  one more level; see that page for the triangle
  T(i+1, k) = i·T(i, k) + T(i, k+1), whose antidiagonals
  [T(0, n), …, T(n, 0)] the program keeps, one list per level, and for
  why the start lists `[1]` and the shared references are safe.
- The innermost series x has head 1 at the first pass and 0 after it:
  `t:=1` at the start, `t=0` after each print. The head of every other
  level is the newest term of the level below, carried over in `t`.

**Notes**

- Assigning `Q` in the `while` condition, with `print(t);t=0` as the body,
  starts the output at a(1) with no extra print: 3 bytes under
  `t=1;Q=[[1,1]]*5` with `while[print(t)]:t=0;Q=…` (88 bytes).
- Exact integer arithmetic, so the program is right for every n. a(1345)
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
Sequences](https://oeis.org/A000359), CC BY-SA 4.0.
