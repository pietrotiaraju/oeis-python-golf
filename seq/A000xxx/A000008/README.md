# A000008

> Number of ways of making change for n cents using coins of 1, 2, 5, 10 cents.
> — [OEIS A000008](https://oeis.org/A000008)

Offset 0: 1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 11, 12, 15, 16, 19, 22, 25, 28, …

### Python 3 — 67 bytes

```python
m=12
while[print(sum((m-j)//10*(j//2)for j in range(m,1,-5)))]:m+=1
```

**How it works**

- Group the 5- and 10-cent coins into t "units of 5": c nickels and d dimes
  with c + 2d = t. There are ⌊t/2⌋ + 1 such pairs.
- The remaining k = n − 5t cents are paid with 1s and 2s in ⌊k/2⌋ + 1 ways.
- With m = n + 12 and j = k + 2 = n + 2 − 5t, the first factor is
  (m − j)/10 = 1 + t/2 rounded down and the second is ⌊j/2⌋, so a(n) is the
  sum of `(m-j)//10*(j//2)` over j = m, m − 5, m − 10, … down to 2.
- Starting the loop at m instead of n + 2 costs nothing: the first two
  values j = m and j = m − 5 have weight 0. The stop value 1 is safe too:
  j = 0 and j = 1 give ⌊j/2⌋ = 0. Counting with m = n + 12 directly saves
  the `+2`s and the `5*` of the old form `(m+2)//2*((n-5*m+2)//2)`
  (73 bytes), and the range needs no `n//5+1`. The same substitution is
  used for [A000064](../A000064/).
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
| 2026-11-05 | Python 3 | 67 | count down from j = n + 12 in steps of 5 (-6) |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000008), CC BY-SA 4.0.
