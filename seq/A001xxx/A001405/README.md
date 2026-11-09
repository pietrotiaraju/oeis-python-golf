# A001405

> a(n) = binomial(n, floor(n/2)).
> — [OEIS A001405](https://oeis.org/A001405)

Offset 0: 1, 1, 2, 3, 6, 10, 20, 35, 70, 126, 252, 462, 924, 1716, 3432, 6435, 12870, …

### Python 3 — 42 bytes

```python
a=n=1
while[print(a)]:a=a*n//(n+1>>1);n+=1
```

**How it works**

- C(n, ⌊n/2⌋)/C(n−1, ⌊(n−1)/2⌋) = n/⌈n/2⌉: for n = 2k it is
  C(2k, k)/C(2k−1, k−1) = 2k/k, for n = 2k + 1 it is
  C(2k+1, k)/C(2k, k) = (2k+1)/(k+1).
- So the loop keeps a = a(n−1) and n, prints a, and steps with
  `a=a*n//(n+1>>1)`: ⌈n/2⌉ = (n+1) >> 1, and the product a·n is divisible
  by ⌈n/2⌉ because the quotient is the integer a(n). Starting with
  `a=n=1` prints a(0) = 1 and then gives a(1) = 1·1/1.
- Exact integer arithmetic, so the program is right for every n.

**Notes**

- `math.comb(n,n//2)` with its import is 52 bytes.
- The b-file has 1001 terms (n = 0 to 1000); the bar is the whole b-file in
  60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 42 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001405), CC BY-SA 4.0.
