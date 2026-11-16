# A001882

> a(2n) = a(2n-1) + 2a(2n-2), a(2n+1) = a(2n) + a(2n-1), with a(1) = 2 and a(2) = 3.
> — [OEIS A001882](https://oeis.org/A001882)

Offset 1: 2, 3, 5, 11, 16, 38, 54, 130, 184, 444, 628, 1516, 2144, 5176, 7320, 17672, …

### Python 3 — 44 bytes

```python
a=2;b=3;m=1
while[print(a)]:a,b=b,b+m*a;m^=3
```

**How it works**

- Both rules have the form a(k + 1) = a(k) + m·a(k − 1): m = 1 when k + 1 is odd, m = 2 when it
  is even. `a` and `b` are a(k) and a(k + 1); m starts at 1, since a(3) = a(2) + a(1), and
  `m^=3` swaps it between 1 and 2 (1 ^ 3 = 2, 2 ^ 3 = 1).

**Notes**

- Exact integer arithmetic. The b-file has 500 terms; the bar is the whole b-file in 60 s,
  which takes a fraction of a second.
- Pairing the terms gives (a(2n − 1), a(2n)) → (a(2n − 1) + a(2n), a(2n − 1) + 3a(2n)), but
  printing two terms per pass costs more than the toggle.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 44 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001882), CC BY-SA 4.0.
