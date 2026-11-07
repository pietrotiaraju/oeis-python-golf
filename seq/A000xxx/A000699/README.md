# A000699

> Number of irreducible chord diagrams with 2n nodes.
> — [OEIS A000699](https://oeis.org/A000699)

Offset 0: 1, 1, 1, 4, 27, 248, 2830, 38232, 593859, 10401712, …

### Python 3 — 75 bytes

```python
R=[1,1]
while[print(R[1])]:R=[~-len(R)*sum(map(int.__mul__,R,R[-2::-1]))]+R
```

**How it works**

- The OEIS recurrence: a(0) = a(1) = 1 and
  a(n+1) = n·Σ_{k=1..n} a(k)·a(n+1−k) for n ≥ 1.
- `R` is `[a(n), …, a(1), a(0)]`, newest first, and each new term goes in
  at the front. `map(int.__mul__,R,R[-2::-1])` pairs a(n), …, a(1) with
  a(1), …, a(n); `map` stops at the shorter list, so a(0) is left out.
  `~-len(R)` is the factor n.
- `print(R[1])` prints one step behind the newest term, so the start
  `R=[1,1]` prints a(0) and then a(1) without a separate `print(1)`.
  Keeping the list newest first costs 2 bytes in the update but saves 3 in
  the slices and the print, against 76 bytes for the oldest-first list.

**Notes**

- Correctness rests on the recurrence in the OEIS entry, equivalent to
  Hanna's g.f. relation A = 1 + x + x²·(d/dx)((A−1)²/x) for the irreducible
  (connected) chord diagrams.
- Each term is one O(n) convolution of big integers: about 1000 terms in
  10 s, still short of Python's 4300-digit int-to-str limit.
- The b-file has 405 terms; the bar is all 405 in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 75 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000699), CC BY-SA 4.0.
