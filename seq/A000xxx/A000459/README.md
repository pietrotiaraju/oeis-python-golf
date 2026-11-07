# A000459

> Number of multiset permutations of {1, 1, 2, 2, ..., n, n} with no fixed points.
> — [OEIS A000459](https://oeis.org/A000459)

Offset 0: 1, 0, 1, 10, 297, 13756, 925705, 85394646, 10351036465, 1596005408152, …

Deal the multiset 1, 1, 2, 2, …, n, n into positions 1, 1, 2, 2, …, n, n
(two of each); a(n) counts the arrangements in which no value lands in a
position with its own label (the card-matching problem with two cards of
each kind).

### Python 3 — 55 bytes

```python
a=b=k=1
while[print(b)]:a,b=b,-~k*(k*(a+b)-a)//2-k;k+=2
```

**How it works**

- **The integral.** Label the 2n cards apart; the forbidden board is n
  disjoint 2×2 blocks, each with rook polynomial x² − 4x + 2 in the
  signed form, so the rook-theory (inclusion–exclusion) count of
  labelled deals is ∫₀^∞ e^(−x)·(x² − 4x + 2)ⁿ dx, and dividing by 2ⁿ for
  the identical copies gives a(n) = ∫₀^∞ e^(−x)·p(x)ⁿ dx with
  p = x²/2 − 2x + 1 (Bala's formula on the entry).
- **The recurrence.** Write I_n for that integral and
  J_n = ∫₀^∞ e^(−x)(x−2)·pⁿ dx. Since p′ = x − 2 and (x−2)² = 2(p+1),
  integration by parts gives I_n = 1 + n·J_{n−1} and
  J_n = −2 + (2n+1)·I_n + 2n·I_{n−1}. Eliminating J gives the recurrence
  on the entry, a(n) = n(2n−1)·a(n−1) + 2n(n−1)·a(n−2) − (2n−1), for
  n ≥ 2 (and for n = 1 with any a(−1)). The program uses it with
  k = 2n − 1: then n = (k+1)/2 and 2(n−1) = k − 1, and
  (2n−1)·a(n−1) + 2(n−1)·a(n−2) = k·(a(n−1) + a(n−2)) − a(n−2), so

  a(n) = (k+1)·(k·(a(n−1) + a(n−2)) − a(n−2))/2 − k.

  k is odd, so k + 1 is even and the `//2` is exact.
- `a, b` hold a(n−2), a(n−1); `-~k` is k + 1. The tuple assignment reads
  both old values before it overwrites them.
- The first pass prints a(0) = 1 and then computes a(1) with k = 1:
  2·(1·(a+b) − a)/2 − 1 = b − 1 = 0. The value standing in for a(−1)
  cancels, so `a=b=k=1` can share one assignment.

**Notes**

- Other versions that print the same terms: the recurrence written in n,
  `a=b=1;n=0` / `while[print(b)]:n+=1;a,b=b,n*((2*n-1)*b+2*(n-1)*a)-2*n+1`:
  66 bytes.
- Exact integer arithmetic, so the program is right for every n.
- The b-file's 101 terms print in 0.08 s here. The b-file has 101 terms
  (up to a(100)); the bar is the whole b-file in 60 s.
- a(818) is the first term with more than 4300 digits, so printing stops
  there (after about 0.3 s).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 66 | first entry |
| 2026-11-07 | Python 3 | 55 | recurrence in k = 2n − 1 |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000459), CC BY-SA 4.0.
