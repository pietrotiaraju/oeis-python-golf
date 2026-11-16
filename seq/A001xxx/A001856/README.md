# A001856

> A self-generating sequence: every positive integer occurs as a(i)-a(j) for a unique pair i,j.
> — [OEIS A001856](https://oeis.org/A001856)

Offset 1: 1, 2, 4, 8, 16, 21, 42, 51, 102, 112, 224, 235, 470, 486, 972, 990, 1980, …

### Python 3 — 98 bytes

```python
l=[1];S={r:=0}
for x in l:
 print(x);S|={x-y for y in l}
 while r in S:r+=1
 l+=x+(x,r)[len(l)%2],
```

**How it works**

- The entry's formula: a(1) = 1, a(2) = 2, a(2n + 1) = 2a(2n), a(2n + 2) = a(2n + 1) + r(n), where
  r(n) is the least positive number that is not a difference a(j) − a(i) of two of the first
  2n + 1 terms. a(2) = 2 is the same rule with r(0) = 1, so after a(1) every even-indexed term is
  the last term plus the least missing difference and every odd-indexed term doubles the last.
- `l` is the list of terms and the loop walks it while it grows: each pass prints x = l[-1],
  adds the differences x − y with every term y to the set `S` (the ones with later or equal y
  are 0 or negative and never matter), moves `r` up to the least positive number not in `S`,
  and appends the next term: `x+(x,r)[len(l)%2]` is x + r when x has an odd index (len(l) is
  odd) and 2x when it has an even one.
- The least missing difference never decreases, because `S` only grows, so `r` keeps climbing
  from where it stopped; on even-index passes it may stop early at a smaller value, which the
  next pass simply continues from.

**Notes**

- Exact integer arithmetic; `S` holds about n²/2 differences, some 500000 big integers for the
  1000-term b-file (a(1000) has 55 digits).
- The bar is the whole b-file in 60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 98 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001856), CC BY-SA 4.0.
