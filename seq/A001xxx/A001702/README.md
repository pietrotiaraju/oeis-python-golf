# A001702

> Generalized Stirling numbers, [n+3,n]_2.
> — [OEIS A001702](https://oeis.org/A001702)

Offset 1: 1, 24, 154, 580, 1665, 4025, 8624, 16884, 30810, 53130, 87450, 138424, 211939, 315315, 457520, …

### Python 3 — 58 bytes

```python
n=1
while[print((n**3-n)*(n+4)*(n*n+7*n+14)//48or 1)]:n+=1
```

**How it works**

- The generalized Stirling number [N, K]ᵣ (Mitrinović's numbers with a = −r, b = −1, as in the entry; the r-Stirling numbers of the first kind) is the coefficient of x^K in xʳ(x+r)(x+r+1)⋯(x+N−1). With N = n + 3 and K = n that is the coefficient of xⁿ⁻² in the n + 1
  factors (x+2)(x+3)⋯(x+n+2), i.e. e₃(2, 3, …, n+2): the sum of i·j·k over all
  triples 2 ≤ i < j < k ≤ n + 2.
- That triple sum is a polynomial of degree 6 in n for every n ≥ 1 (nested
  Faulhaber sums; empty sums are 0), and so is
  (n−1)n(n+1)(n+4)(n²+7n+14)/48, the entry's formula. Two polynomials of
  degree 6 that agree at the seven points n = 1, …, 7 (0, 24, 154, 580, 1665,
  4025, 8624) are equal, so the program's value is e₃ for every n.
  `n**3-n` is (n−1)n(n+1).
- For n = 1 the set {2, 3} has no triple and the formula gives 0, but the
  entry lists a(1) = 1, as in [A001701](../A001701/) (its closed form is stated
  for n > 1). `or 1` patches exactly that term: the formula is positive for
  n ≥ 2. `48or` lexes as `48` then `or` (Python 3.12 only warns).

**Notes**

- Exact integer arithmetic, correct for every n (the values are polynomial in
  n). The whole b-file (1000 terms) prints at once; the bar is the whole
  b-file in 60 s.
- Accumulating e₁, e₂, e₃ as in A001701,
  `a=b=0;s=2;c=3` / `while[print((a:=a+c*b)or 1)]:b+=c*s;s+=c;c+=1`, is
  59 bytes.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-14 | Python 3 | 58 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001702), CC BY-SA 4.0.
