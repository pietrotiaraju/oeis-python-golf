# A001492

> Clock chimes with a quarter-hour bell.
> — [OEIS A001492](https://oeis.org/A001492)

Offset 0: 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 3, 1, 1, 1, 4, 1, 1, 1, 5, …

### Python 3 — 39 bytes

```python
n=0
while[print(n%4//3*n//4%12+1)]:n+=1
```

**How it works**

- The clock rings one bell at each quarter hour that is not on the hour, and
  strikes the hour h times on the hour. Following the data (and the PARI
  program in the entry), a(n) is the n-th sound of the clock counted from a
  quarter past twelve: n = 0, 1, 2 are the quarters 12:15, 12:30, 12:45, n = 3
  is one o'clock, n = 7 two o'clock, …, n = 47 twelve o'clock, and then it
  repeats with period 48. So a(n) = 1 unless n ≡ 3 (mod 4), and
  a(4k + 3) = (k mod 12) + 1.
- `n%4//3` is 1 when n ≡ 3 (mod 4) and 0 otherwise. Python evaluates
  `n%4//3*n//4%12` from left to right, so it is ((n%4//3)·n)//4 mod 12: 0 off
  the hour, and ⌊n/4⌋ mod 12 = k mod 12 on the hour. Adding 1 gives the
  term, for every n.
- `print(…)` runs in the loop condition: it returns `None`, `[None]` is a
  non-empty list and so always true, and the body steps n.

**Notes**

- Printing a whole hour per pass, `k=0` +
  `while[print(1,1,1,k%12+1,sep='\n')]:k+=1`, is 44 bytes, and
  `k=1` + `while[print(f'1\n1\n1\n{k}')]:k=k%12+1` 42.
- The b-file has 1001 terms (n = 0 to 1000); the bar is the whole b-file in
  60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-10 | Python 3 | 39 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001492), CC BY-SA 4.0.
