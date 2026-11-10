# A001511

> The ruler function: exponent of the highest power of 2 dividing 2n. Equivalently, the 2-adic valuation of 2n.
> — [OEIS A001511](https://oeis.org/A001511)

Offset 1: 1, 2, 1, 3, 1, 2, 1, 4, 1, 2, 1, 3, 1, 2, 1, 5, 1, 2, 1, 3, 1, 2, 1, …

### Python 3 — 34 bytes

```python
l=[1]
for x in l:print(x);l+=x+1,1
```

**How it works**

- v₂(2n) = 1 + v₂(n), so a(2k) = v₂(4k) = a(k) + 1, and a(2k + 1) = 1
  because 2(2k + 1) has a single factor 2.
- `l` is the sequence itself, a(1), a(2), …. The `for` loop walks the list
  while it grows (a list iterator sees items appended during the loop): on
  reading a(k) it prints it and appends a(2k) = a(k) + 1 and
  a(2k + 1) = 1. When a(k) is read the list already holds a(1) to
  a(2k − 1), so the new terms land exactly in place and the reader never
  catches up: the loop runs forever.

**Notes**

- The direct formula is longer: `n=1` / `while[print(len(bin(n&-n))-2)]:n+=1`
  (`n&-n` keeps the lowest set bit of n) is 39 bytes.
- The list holds about twice as many entries as have been printed, 8 bytes
  each (the small ints themselves are shared), a few hundred kB for the
  b-file.
- The b-file has 10000 terms; the bar is the whole b-file in 60 s, which
  takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-10 | Python 3 | 34 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001511), CC BY-SA 4.0.
