# A000698

> A problem of configurations: a(0) = 1; for n>0, a(n) = (2n-1)!! - Sum_{k=1..n-1} (2k-1)!! a(n-k). Also the number of shellings of an n-cube, divided by 2^n n!.
> — [OEIS A000698](https://oeis.org/A000698)

Offset 0: 1, 1, 2, 10, 74, 706, 8162, 110410, 1708394, 29752066, …

### Python 3 — 78 bytes

```python
L=[1,1]
while[print(L[-2])]:L+=sum(map(int.__mul__,L,L[-1:]+L[::-1])),;L[0]+=2
```

**How it works**

- Bala's recurrence in the OEIS entry: a(1) = 1 and, for n ≥ 1,
  a(n+1) = (2n−1)·a(n) + Σ_{k=1..n} a(k)·a(n+1−k).
- `L` is `[c, a(1), …, a(n)]`, where the slot `L[0]` holds c = 2n−1.
  Pairing `L` with `L[-1:]+L[::-1]` = [a(n), a(n), a(n−1), …, a(1), c]
  gives c·a(n) + Σ a(k)a(n+1−k); `map` stops at the shorter list, so the
  trailing c is never used. `L[0]+=2` then moves c on to the next 2n−1.
- The start `L=[1,1]` is c = 1 for n = 1 and a(1) = 1, and since
  a(0) = 1 too, `print(L[-2])` prints the sequence one step behind the
  newest term: a(0) (the slot, before it changes), then a(1), a(2), ….

**Notes**

- Correctness rests on Bala's recurrence (2011, in the OEIS entry), which
  follows from the g.f. 2 − 1/Σ(2n−1)!!xⁿ of the name and the differential
  equation 2x²D′ + (x−1)D + 1 = 0 of D = Σ(2n−1)!!xⁿ.
- Each term is one O(n) convolution of big integers: about 1000 terms in
  10 s, still short of Python's 4300-digit int-to-str limit.
- The b-file has 201 terms; the bar is all 201 in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 78 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000698), CC BY-SA 4.0.
