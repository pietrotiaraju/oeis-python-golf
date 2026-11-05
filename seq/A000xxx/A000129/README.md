# A000129

> Pell numbers: a(0) = 0, a(1) = 1; for n > 1, a(n) = 2*a(n-1) + a(n-2).
> — [OEIS A000129](https://oeis.org/A000129)

Offset 0: 0, 1, 2, 5, 12, 29, 70, 169, 408, 985, 2378, 5741, 13860, …

### Python 3 — 35 bytes

```python
a,b=0,1
while[print(a)]:a,b=b,a+2*b
```

**How it works**

- `a` and `b` hold two consecutive Pell numbers, a(n) and a(n+1), starting
  from a(0) = 0 and a(1) = 1.
- `print(a)` runs in the loop condition, as in [A000045](../A000045/): it
  returns `None`, and `[None]` is a non-empty list, so the loop never ends.
- `a,b=b,a+2*b` moves one step along the recurrence: the new pair is
  a(n+1), a(n) + 2·a(n+1) = a(n+2). Integers are exact, so every term is
  right.

**Notes**

- This is the [Fibonacci](../A000045/) program with `a+b` turned into
  `a+2*b`; `a+b+b` and `a+b*2` are the same length.
- Starting one step earlier, from a(−1) = 1 and a(0) = 0, and printing `b`
  is also 35 bytes.
- `a=b=1` saves 2 bytes on the start by running the companion sequence
  1, 1, 3, 7, 17, 41, … ([A001333](https://oeis.org/A001333)) with the same
  recurrence, but recovering a(n) as `b-a>>1` costs 5, so it is 38 bytes.
- Python's 4300-digit limit on int-to-str conversion stops the program at
  a(11235), the first Pell number with 4301 digits, after printing a(0) to
  a(11234). The limit is not counted as a failure.
- The b-file has 1001 terms (n = 0 to 1000, the last one has 383 digits) and
  the whole of it prints instantly; the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 35 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000129), CC BY-SA 4.0.
