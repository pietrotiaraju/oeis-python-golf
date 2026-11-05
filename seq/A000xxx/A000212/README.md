# A000212

> a(n) = floor(n^2/3).
> — [OEIS A000212](https://oeis.org/A000212)

Offset 0: 0, 0, 1, 3, 5, 8, 12, 16, 21, 27, …

### Python 3 — 29 bytes

```python
n=0
while[print(n*n//3)]:n+=1
```

**How it works**

- The definition, with Python's floor division: `n*n//3` is ⌊n²/3⌋ for
  every n ≥ 0 (and `n*n` is one byte under `n**2`).
- `while[print(…)]:` runs the print in the loop test: the list `[None]` is
  non-empty, hence true, and the body only steps `n`. One byte under
  `while 1:print(n*n//3);n+=1`.

**Notes**

- Integer arithmetic only, so it is correct for every n. It prints the
  whole b-file (5001 terms) at once; the bar is the whole b-file in 60 s.
- The running-sum form a(n) = Σ_{i≤n} ⌊2i/3⌋ (Hurt), `a=n=0` /
  `while[print(a:=a+n//3)]:n+=2`, is 35 bytes; keeping n² in its own
  variable (it grows by 2n + 1) is longer still.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 29 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000212), CC BY-SA 4.0.
