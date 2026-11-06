# A000533

> a(0)=1; a(n) = 10^n + 1, n >= 1.
> — [OEIS A000533](https://oeis.org/A000533)

Offset 0: 1, 11, 101, 1001, 10001, 100001, 1000001, 10000001, 100000001, 1000000001, …

### Python 3 — 33 bytes

```python
n=0
while[print(n+1)]:n=n*10or 10
```

**How it works**

- The accumulator takes the values 0, 10, 100, 1000, … . Adding 1 gives
  the exceptional a(0)=1 followed by a(n)=10^n+1.
- On the first iteration `n*10` is zero, so `or 10` supplies the first
  power of ten. Every later product is positive and keeps multiplying
  by ten.
- Printing in the always-true list condition saves a separate statement.

**Notes**

- All operations are on integers, and every stated division is exact.
- Python 3.11+ can eventually reach its integer-to-string conversion limit.
- The reference file contains 101 terms from the OEIS b-file; the verification
  bar is 101 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 33 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000533), CC BY-SA 4.0.
