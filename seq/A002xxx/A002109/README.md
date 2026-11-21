# A002109

> Hyperfactorials: Product_{k = 1..n} k^k.
> — [OEIS A002109](https://oeis.org/A002109)

Offset 0: 1, 1, 4, 108, 27648, 86400000, 4031078400000, 3319766398771200000, …

### Python 3 — 34 bytes

```python
p=n=1
while[print(p)]:p*=n**n;n+=1
```

**How it works**

- p is the running product 1¹·2²·…·(n−1)^(n−1): it is printed, then
  multiplied by n^n. From p = n = 1, the first two lines are a(0) = 1 (the
  empty product) and a(1) = 1.

**Notes**

- `p*=(n:=n+1)**n` with `n=0` is longer.
- Exact integer arithmetic, right for every n. The b-file has 37 terms
  (n = 0 to 36); the bar is the whole b-file in 60 s, a few milliseconds.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-20 | Python 3 | 34 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002109), CC BY-SA 4.0.
