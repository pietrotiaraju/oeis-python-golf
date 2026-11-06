# A000561

> Number of discordant permutations.
> — [OEIS A000561](https://oeis.org/A000561)

Offset 3: 6, 44, 145, 336, 644, 1096, 1719, 2540, 3586, 4884, …

### Python 3 — 43 bytes

```python
n=3
while 1:print(n*(9*n*(n-5)+58)//2);n+=1
```

**How it works**

- The OEIS formula is P(n)=n(9n²−45n+58)/2. Factoring the middle
  terms as 9n(n−5)+58 saves one multiplication by n in its written form.
- The same polynomial gives P(3)=6 at the initial offset, so a separate
  initial print is unnecessary. Advancing n then prints every later term.
- The numerator is always even: for even n its first factor is even;
  for odd n, n(n−5) is even. Thus integer division is exact.

**Notes**

- All operations are on integers, and every stated division is exact.
- Python 3.11+ can eventually reach its integer-to-string conversion limit.
- The reference file contains 998 terms from the OEIS b-file; the verification
  bar is 998 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 43 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000561), CC BY-SA 4.0.
