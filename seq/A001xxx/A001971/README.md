# A001971

> Nearest integer to n^2/8.
> — [OEIS A001971](https://oeis.org/A001971)

Offset 0: 0, 0, 1, 1, 2, 3, 5, 6, 8, 10, 13, 15, 18, 21, 25, 28, 32, 36, 41, 45, 50, 55, …

### Python 3 — 31 bytes

```python
n=0
while[print(n*n+4>>3)]:n+=1
```

**How it works**

- **Ties.** n²/8 is halfway between two integers when n ≡ 2 (mod 4)
  (then n² ≡ 4 (mod 8)); the data rounds those up (a(2) = 1, a(6) = 5), so
  a(n) = ⌊(n² + 4)/8⌋ (Paul Weisenhorn's formula in the entry).
- **Program.** `n*n+4>>3` is that floor: `+` binds tighter than `>>`, and a
  right shift by 3 floors the division by 8.
- Exact integer arithmetic, so the program is right for every n.

**Notes**

- The b-file has 10001 terms (n = 0 to 10000); the bar is the whole b-file
  in 60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 31 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001971), CC BY-SA 4.0.
