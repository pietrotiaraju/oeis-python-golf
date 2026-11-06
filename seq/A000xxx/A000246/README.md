# A000246

> Number of permutations in the symmetric group S_n that have odd order.
> — [OEIS A000246](https://oeis.org/A000246)

Offset 0: 1, 1, 1, 3, 9, 45, 225, 1575, 11025, 99225, 893025, …

### Python 3 — 35 bytes

```python
a=1;n=0
while[print(a)]:a*=n|1;n+=1
```

**How it works**

- A permutation has odd order exactly when all its cycles have odd length,
  so the e.g.f. is exp(x + x³/3 + x⁵/5 + …) = exp(atanh x) =
  √((1+x)/(1−x)). Its logarithmic derivative is 1/(1−x²), so
  (1−x²)A′ = A, which reads a(n+1) = a(n) + n(n−1)·a(n−1).
- That recurrence collapses to one factor per step: a(n+1) = (n|1)·a(n),
  i.e. multiply by 1, 1, 3, 3, 5, 5, 7, 7, … By induction from
  a(0) = a(1) = 1: if n is even, a(n) = (n−1)·a(n−1), so
  a(n+1) = a(n) + n·a(n) = (n+1)·a(n); if n is odd, a(n) = n·a(n−1), so
  a(n+1) = a(n) + (n−1)·a(n) = n·a(n). Both are (n|1)·a(n). This gives
  the closed forms a(2k) = ((2k−1)!!)² and a(2k+1) = (2k+1)·((2k−1)!!)².
- `n|1` sets the low bit, turning 0, 1, 2, 3, 4, … into 1, 1, 3, 3, 5, …
  with no parity test.
- Starting from n = 1 instead (`a=n=1`) saves 2 bytes in the setup but the
  factor becomes `~-n|1`: also 35. Printing two terms per round with the odd
  factor applied twice (`print(a),print(a:=a*n)` … `n+=2`) is 40, and the
  two-term recurrence above needs a second state and is longer still.

**Notes**

- Exact integer arithmetic, correct for every n. The whole b-file
  (451 terms) prints at once; the program stops after a(1558), when the
  next term passes the 4300-digit int-to-str limit of Python 3.11+. The bar
  is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 35 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000246), CC BY-SA 4.0.
