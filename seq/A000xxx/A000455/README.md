# A000455

> Digits of powers of 2.
> — [OEIS A000455](https://oeis.org/A000455)

Offset 0: 1, 2, 4, 8, 1, 6, 3, 2, 6, 4, …

### Python 3 — 39 bytes

```python
n=1
while[print(d)for d in str(n)]:n*=2
```

**How it works**

- n holds 1,2,4,8,16,…, the powers 2ᵏ starting at k=0.
  `str(n)` gives their digits in the required left-to-right order.
- The comprehension calls `print(d)` once for every character d,
  so a power with several digits contributes several consecutive
  sequence terms, one per line. In particular 16 contributes 1,6,
  followed by 3,2 from 32.
- Each call returns `None`, and the comprehension makes a list of
  these results. Every decimal representation has at least one digit,
  so that list is nonempty and the `while` condition stays true.
- Only after all the current power's digits have printed does the
  body multiply n by 2. No separator or marker is inserted between
  the powers.

**Notes**

- Exact integer multiplication and decimal conversion. Printing the
  digit characters is equivalent to printing the integers 0 through 9,
  including any zero occurring inside a power.
- The offset counts emitted digits, not exponents. The first four
  powers each contribute one term, while 2⁴ contributes two.
- Each round holds the power, its decimal text and a temporary list
  proportional to its number of digits; there is no accumulated
  string containing all previous powers.
- Python 3.11+'s default conversion limit first rejects 2^14285,
  which has 4301 decimal digits. This is an interpreter limit rather
  than a wrong digit in the sequence.
- The b-file has 10000 terms (indices 0 through 9999). The bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 39 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000455), CC BY-SA 4.0.
