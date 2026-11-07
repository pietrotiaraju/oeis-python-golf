# A000466

> a(n) = 4*n^2 - 1.
> — [OEIS A000466](https://oeis.org/A000466)

Offset 0: -1, 3, 15, 35, 63, 99, 143, 195, 255, 323, …

### Python 3 — 28 bytes

```python
m=0
while[print(m*m-1)]:m+=2
```

**How it works**

- m runs through 0, 2, 4, … = 2n, and 4n² − 1 = (2n)² − 1 = m² − 1, so the
  factor 4 disappears into the step `m+=2`.
- `print` sits in the loop condition: it returns `None`, and `[None]` is a
  non-empty list, so the loop never ends (the [A000007](../A000007/) loop).

**Notes**

- Other versions that print the same terms: `n=0` /
  `while[print(4*n*n-1)]:n+=1`: 31 bytes; the original
  `while 1:print(4*n*n-1);n+=1`: 32 bytes.
- Exact integer arithmetic, so the program is right for every n.
- The b-file's 901 terms print in 0.07 s here. The b-file has 901 terms (up
  to a(900)); the bar is the whole b-file in 60 s.
- [A000447](../A000447/) is Σ (2k−1)² = n(4n² − 1)/3.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 31 | first entry |
| 2026-11-07 | Python 3 | 28 | m = 2n, so the term is m² − 1 |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000466), CC BY-SA 4.0.
