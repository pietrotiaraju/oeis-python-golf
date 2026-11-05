# A000182

> Tangent (or "Zag") numbers: e.g.f. tan(x), also (up to signs) e.g.f. tanh(x).
> — [OEIS A000182](https://oeis.org/A000182)

Offset 1: 1, 2, 16, 272, 7936, 353792, 22368256, 1903757312, 209865342976, …

### Python 3 — 66 bytes

```python
r=[t:=1]
while[r<[t%2]or print(t)]:r=[t:=t+x for x in[-t]+r[::-1]]
```

**How it works**

- The tangent numbers are the odd-indexed Euler zigzag numbers,
  a(n) = [A000111](../A000111/)(2n − 1), so the body is the same
  Seidel–Entringer step as there: each row is the running sums of `[0]`
  followed by the row above reversed, and row m ends with A000111(m). `t`
  runs along the row as a walrus sum, and the `-t` in front brings it back
  to 0 for the leading entry.
- Only every other row should be printed. Instead of tracking the parity of
  the row, the test looks at the parity of the term: the secant numbers
  A000111(2k) are all odd, and the tangent numbers a(n) are even for n ≥ 2.
  - Secant: sec(x)·cos(x) = 1 gives E(2k) = Σ_{j≥1} ±C(2k, 2j)·E(2k − 2j),
    so by induction E(2k) ≡ Σ_{j=1..k} C(2k, 2j) = 2^(2k−1) − 1 (mod 2).
  - Tangent: tan′ = 1 + tan² gives
    a(n+1) = Σ_{i=1..n} C(2n, 2i−1)·a(i)·a(n+1−i). The terms i and n+1−i
    have the same binomial and pair up, and the middle one (n odd) carries
    C(2n, n), which is even.
- The odd values left over are A000111(0) = A000111(1) = A000111(2) = 1,
  and exactly one of them must be printed, as a(1). `r<[t%2]` does that:
  rows 1, 2, … all start with 0, so for odd `t` they are below `[1]` and
  nothing is printed, while row 0 is `[1]` itself and gets through. For
  even `t` no list starting with 0 is below `[0]`, so the term is printed.
  That is 1 byte under `len(r)%2` and 3 under running the step twice per
  pass with `exec("…;"*2)`, which also needs row 1 as the start.
- `while[…]` loops forever because the list holds one element whatever the
  `or` returns.

**Notes**

- Exact integer arithmetic, correct for every n. The whole b-file
  (243 terms) prints in well under a second; the program stops after
  a(830), when the next term passes the 4300-digit int-to-str limit of
  Python 3.11+. The bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 66 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000182), CC BY-SA 4.0.
