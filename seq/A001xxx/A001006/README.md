# A001006

> Motzkin numbers: number of ways of drawing any number of nonintersecting chords joining n (labeled) points on a circle.
> — [OEIS A001006](https://oeis.org/A001006)

Offset 0: 1, 1, 2, 4, 9, 21, 51, 127, 323, 835, 2188, 5798, 15511, 41835, 113634, 310572, …

### Python 3 — 51 bytes

```python
s=b=m=1
while 1:m+=1;s=3*b+(b:=b+s-3*s//m);print(b)
```

**How it works**

- The Motzkin numbers satisfy (n+2)M(n) = (2n+1)M(n−1) + 3(n−1)M(n−2),
  the D-finite recurrence of the algebraic g.f. M = 1 + xM + x²M² (it is
  in the entry).
- With m = n + 2 the right side is m(2M(n−1) + 3M(n−2)) − 3(M(n−1) +
  3M(n−2)), so with s = M(n−1) + 3M(n−2):

  **M(n) = M(n−1) + s − 3s/m**,

  and 3s/m is an integer because everything else is.
- The state is `b` = M(n−1) and `s`. The new s is 3·M(n−1) + M(n), which
  `s=3*b+(b:=…)` gets in one statement: `3*b` is read before the walrus
  overwrites `b`.
- Phantom start: with b = s = 1 the first pass (m = 2) gives
  1 + 1 − ⌊3/2⌋ = 1 = M(0), and the second (m = 3) gives b + s − s = b
  for any s, so every variable starts at 1 and the print comes after the
  update (1 byte under `while[print(b)]:` with `s=b=1;m=2`).

**Notes**

- Exact integer arithmetic; correct for every n by the recurrence.
- Thousands of terms per second; the bar is the whole b-file (2107 terms)
  in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 51 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001006), CC BY-SA 4.0.
