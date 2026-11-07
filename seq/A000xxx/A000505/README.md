# A000505

> Eulerian numbers (Euler's triangle: column k=5 of A008292, column k=4 of A173018).
> — [OEIS A000505](https://oeis.org/A000505)

Offset 5: 1, 57, 1191, 15619, 156190, 1310354, 9738114, 66318474, 423281535, 2571742175, …

a(n) is the number of permutations of 1..n with exactly 4 descents
(5 ascending runs).

### Python 3 — 87 bytes

```python
b=c=d=e=m=0
while[e>0==print(e)]:m+=1;b,c,d,e=2*b+m,3*c+(m-1)*b,4*d+(m-2)*c,5*e+(m-3)*d
```

**How it works**

- Let A(n, k) be the number of permutations of 1..n with k ascending runs
  (k − 1 descents). Put n into one of the n gaps of a permutation of
  1..n−1 with k runs: at the end or inside one of its k − 1 descents the
  number of descents stays the same, and at the front or inside an ascent it
  grows by one. So k gaps keep k runs and the other n − k add one, which is
  the classical Eulerian recurrence

  A(n, k) = k·A(n−1, k) + (n − k + 1)·A(n−1, k−1),

  and a(n) = A(n, 5).
- Column k = 1 is 1 for n ≥ 1, so the program keeps only columns 2 to 5 in
  `b,c,d,e`. All four are 0 at n = 1, and with m = n − 1 the new row is
  b = 2b + m, c = 3c + (m−1)·b, d = 4d + (m−2)·c, e = 5e + (m−3)·d, all
  read from the old row by the tuple assignment.
- `e>0==print(e)` is the chain `e>0 and 0==print(e)`, so it prints only once
  e = A(n, 5) is nonzero, which is exactly from n = 5 on. Its value is
  `False`, but `[False]` is a true list, so the loop never ends.

**Notes**

- The inclusion–exclusion formula A(n, 5) = Σ_{j=0}^{4} (−1)^j·C(n+1, j)·(5−j)ⁿ
  is 91 bytes (`import math` / `n=5` /
  `while[print(sum((-1)**j*math.comb(n+1,j)*(5-j)**n for j in range(5)))]:n+=1`)
  and 93 with `from math import*` and `while 1:`. Other offsets of m (m = n − 2
  from the n = 2 row, m = n − 3) give the same 87 bytes or more.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 996 terms (up to a(1000)); the bar is the whole b-file in
  60 s. Each term costs a few big-integer operations.
- Python's 4300-digit int-to-str limit stops the printing after a(6151)
  (4300 digits; a(6152) has 4301), about a second after the start.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 93 | first entry |
| 2026-11-07 | Python 3 | 87 | Eulerian recurrence on four columns |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000505), CC BY-SA 4.0.
