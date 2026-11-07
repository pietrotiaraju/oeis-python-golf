# A000514

> Eulerian numbers (Euler's triangle: column k=6 of A008292, column k=5 of A173018).
> — [OEIS A000514](https://oeis.org/A000514)

Offset 6: 1, 120, 4293, 88234, 1310354, 15724248, 162512286, 1505621508, 12843262863, 102776998928, …

a(n) is the number of permutations of 1, …, n with exactly 5 descents
(positions i with π(i) > π(i+1)), that is, with 6 ascending runs.

### Python 3 — 91 bytes

```python
import math
n=6
while[print(sum((-1)**j*math.comb(n+1,j)*(6-j)**n for j in range(6)))]:n+=1
```

**How it works**

- The number of permutations of n elements with m ascents (equally, by
  reversal, m descents) is A(n, m) = Σ_{j=0}^{m+1} (−1)^j·C(n+1, j)·(m+1−j)^n
  (Graham, Knuth and Patashnik, *Concrete Mathematics*, eq. 6.38). It
  inverts Worpitzky's identity x^n = Σ_m A(n, m)·C(x+m, n): sort the
  positions of each map f: {1, …, n} → {1, …, x} by value, ties by
  position; a permutation with m ascents arises from the C(x+m, n) maps
  whose values must strictly increase at its n−1−m descents.
- With m = 5 the last term (j = 6) is C(n+1, 6)·0^n = 0 for n ≥ 1, so
  `range(6)` is enough: a(n) = 6^n − (n+1)·5^n + C(n+1, 2)·4^n −
  C(n+1, 3)·3^n + C(n+1, 4)·2^n − C(n+1, 5).
- The loop starts at the offset n = 6, where the formula gives 1 (the
  decreasing permutation); below it the true value 0 would be printed.
- `while[print(…)]:n+=1` is a byte under `while 1:print(…);n+=1`: the
  list holding `None` is truthy. `import math` with `math.comb` used once
  is a byte under `from math import*` with `comb`.

**Notes**

- `from math import*` / `while 1:print(…);n+=1` with the same sum:
  93 bytes. The triangle recurrence A(n, k) = k·A(n−1, k) +
  (n−k+1)·A(n−1, k−1) as a cached lambda over two arguments is about
  115 bytes.
- Exact integer arithmetic, so the program is right for every n.
- The whole b-file prints in about 0.1 s here. The program stops after
  a(5525): a(n) has about 0.778·n digits, and a(5526) is the first with
  more than 4300, the int-to-str limit of Python 3.11+.
- The b-file has 995 terms (up to a(1000)); the bar is the whole b-file
  in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 93 | first entry |
| 2026-11-07 | Python 3 | 91 | `while[print(…)]` loop, `import math` |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000514), CC BY-SA 4.0.
