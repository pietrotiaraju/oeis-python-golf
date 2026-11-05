# A000008

> Number of ways of making change for n cents using coins of 1, 2, 5, 10 cents.
> — [OEIS A000008](https://oeis.org/A000008)

Offset 0: 1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 11, 12, 15, 16, 19, 22, 25, 28, …

### Python 3 — 73 bytes

```python
n=0
while[print(sum((m+2)//2*((n-5*m+2)//2)for m in range(n//5+1)))]:n+=1
```

**How it works**

- Group the 5- and 10-cent coins into m "units of 5": c nickels and d dimes
  with c + 2d = m. There are ⌊m/2⌋ + 1 such pairs.
- The remaining n − 5m cents are paid with 1s and 2s in ⌊(n − 5m)/2⌋ + 1
  ways.
- So a(n) = Σ (⌊m/2⌋ + 1)(⌊(n − 5m)/2⌋ + 1) for m = 0…⌊n/5⌋, written as
  `(m+2)//2*((n-5*m+2)//2)`. Exact integers, n/5 steps per term.
- `while[print(...)]:` prints in the loop condition (`[None]` is true) and
  saves a byte over `while 1:print(...);`.

**Notes**

- The OEIS recurrence a(n) = a(n−2) + a(n−5) − a(n−7) + a(n−10) − a(n−12)
  − a(n−15) + a(n−17) + 1, run on a list padded with 17 zeros, is 81 bytes.
- The closed forms on the OEIS entry (Kirchner 2017, Hoang 2025) come out at
  77 bytes or more.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 73 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000008), CC BY-SA 4.0.
