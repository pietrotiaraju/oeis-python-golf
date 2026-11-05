# A000217

> Triangular numbers: a(n) = binomial(n+1,2) = n*(n+1)/2 = 0 + 1 + 2 + ... + n.
> — [OEIS A000217](https://oeis.org/A000217)

Offset 0: 0, 1, 3, 6, 10, 15, 21, 28, 36, 45, …

### Python 3 — 29 bytes

```python
m=1
while[print(m*m>>3)]:m+=2
```

**How it works**

- `m` runs over the odd numbers 2n + 1. Since (2n + 1)² = 4n² + 4n + 1 =
  8·a(n) + 1, every odd square is one more than eight times a triangular
  number, so `m*m>>3` (drop the three low bits, which hold just that 1) is
  a(n) exactly.
- Keeping 2n + 1 in place of n turns n(n + 1)/2 into a single square and a
  shift: `m*m>>3` is 2 bytes under `n*n+n>>1`, and the step `m+=2` costs the
  same as `n+=1`.
- `while[print(…)]:` runs the print in the loop test: the list `[None]` is
  non-empty, hence true, and the body only steps `m`. One byte under
  `while 1:print(…);…`.

**Notes**

- Integer arithmetic only, so it is correct for every n. It prints the
  whole b-file (30001 terms) at once; the bar is the whole b-file in 60 s.
- The direct form `n=0` / `while[print(n*n+n>>1)]:n+=1` and the running sum
  `a=n=0` / `while[print(a)]:n+=1;a+=n` are both 31 bytes; `n*-~n>>1` and
  `n*~n//-2` tie with `n*n+n>>1`. `m*m//8` ties with `m*m>>3`.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 29 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000217), CC BY-SA 4.0.
