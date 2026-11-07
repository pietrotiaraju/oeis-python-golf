# A000511

> Number of n-step spiral self-avoiding walks on hexagonal lattice, where at each step one may continue in same direction or make turn of 2*Pi/3 counterclockwise.
> — [OEIS A000511](https://oeis.org/A000511)

Offset 0: 1, 1, 2, 3, 5, 8, 11, 17, 25, 33, …

The walks live on the triangular lattice (6 neighbours per point) and are
counted with the first step fixed, so a(1) = 1.

### Python 3 — 125 bytes

```python
f=lambda z,d,t,S:n<len(S)or sum(f(w,a,b,S|{w})for a,b in((d,t),(t,-d-t))if{w:=z+a}-S)
n=0
while[print(+f(1,1,1j,{0,1}))]:n+=1
```

**How it works**

- Lattice points x + yω are stored as the complex numbers x + yi, so the
  three step directions 120° apart are 1, i and −1 − i (= ω²), and the six
  neighbours of a point are ±1, ±i, ±(1 + i) away. Only additions of
  small integers happen, so the arithmetic is exact.
- A walk heading in direction d may go on in d or turn to the next
  direction t. The three directions sum to 0, so after the turn the next
  one is −d − t: the state (d, t) becomes (d, t) going straight and
  (t, −d − t) after a turn, `for a,b in((d,t),(t,-d-t))`.
- `f(z,d,t,S)` counts the ways to finish a walk that stands at z with state
  (d, t) and has visited the set S. A walk of n steps has n + 1 points, so
  `n<len(S)or` returns `True` (counted as 1) once it is complete; n is the
  global loop counter.
- `{w:=z+a}-S` is non-empty exactly when the next point w is new, and the
  walrus (allowed bare in a set display since Python 3.10) hands w to the
  call, which is evaluated after the test.
- The count starts after the fixed first step from 0 to 1, with state
  (1, i). For n = 0 and 1 the set {0, 1} already has more than n points, so
  f returns `True` and `+` prints it as 1.

**Notes**

- Passing n down as a parameter (`n<1or`, `f(n-1,…)`) is 130 bytes, and
  counting both first steps from 0 and halving
  (`print(-~f(0,1,1j,{0})>>1)`, by the 120° symmetry) is 127. The previous
  version with coordinate pairs and an explicit set update was 249 bytes.
- The search visits every spiral walk of length ≤ n, so it is correct for
  every n; complex numbers with integer parts stay exact while coordinates
  are below 2⁵³, far beyond reach.
- The time grows with a(n): 51 terms (up to a(50)) in 60 s here. The
  recursion is about 2n frames deep, so Python's default limit of 1000
  would only matter near n = 500.
- The b-file has 96 terms (up to a(95)); the bar is 20 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 249 | first entry |
| 2026-11-07 | Python 3 | 125 | state (d, t) → (t, −d−t), Gaussian-integer points, length test on the set |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000511), CC BY-SA 4.0.
