# A002022

> In the pile of coconuts problem, the number of coconuts that remain to be shared equally at the end of the process.
> — [OEIS A002022](https://oeis.org/A002022)

Offset 2: 0, 6, 240, 1020, 78120, 279930, 40353600, 134217720, 31381059600, …

### Python 3 — 35 bytes

```python
m=1
while[print(m**(-~m|1)-m)]:m+=1
```

**How it works**

- The process of [A002021](../A002021/): a share takes a pile x to
  (n − 1)(x − 1)/n, so y = x + n − 1 is multiplied by (n − 1)/n. The
  least starting pile has y = nⁿ for odd n and y = (n − 1)·nⁿ for even n
  (see that page), so after the n shares y = (n − 1)ⁿ or (n − 1)ⁿ⁺¹, and
  the pile left to share is y − (n − 1).
- With m = n − 1 that is m^e − m, where e = n for odd n and e = n + 1 for
  even n: the least odd number ≥ n, n | 1. Here n is `-~m`, so the term is
  `m**(-~m|1)-m`, for m = 1, 2, 3, ….

**Notes**

- Checks: n = 5 gives 4⁵ − 4 = 1020 and n = 6 gives 5⁷ − 5 = 78120, as in
  the OEIS data.
- Exact integer arithmetic, so the program is right for every n; Python's
  4300-digit int-to-str limit stops the output near n = 1370.
- The b-file has 99 terms (n = 2 to 100); the bar is the whole b-file in
  60 s, which takes a few milliseconds.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 35 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002022), CC BY-SA 4.0.
