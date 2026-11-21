# A002081

> Numbers congruent to {2, 4, 8, 16} (mod 20).
> — [OEIS A002081](https://oeis.org/A002081)

Offset 0: 2, 4, 8, 16, 22, 24, 28, 36, 42, 44, 48, 56, 62, 64, 68, 76, 82, 84, …

### Python 3 — 27 bytes

```python
k=2
while[print(k)]:k+=k%10
```

**How it works**

- Modulo 20 the terms cycle through 2, 4, 8, 16, and in increasing order
  consecutive terms differ by 2, 4, 8 and 6 (16 → 22).
- A number ≡ r (mod 20) ends in the digit r mod 10, which is 2, 4, 8, 6 for
  r = 2, 4, 8, 16: exactly the step to the next term. So from k = 2,
  `k+=k%10` moves from each term to the next one (the residue goes
  2 → 4 → 8 → 16 → 2), and by induction it visits every term, in order,
  and nothing else.

**Notes**

- The closed form a(n) = 20⌊n/4⌋ + (2, 4, 8, 16)[n mod 4] needs a table
  and a counter, and is longer.
- Exact integer arithmetic, right for every n. The b-file has 10001 terms
  (n = 0 to 10000); the bar is the whole b-file in 60 s, a fraction of a
  second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-20 | Python 3 | 27 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002081), CC BY-SA 4.0.
