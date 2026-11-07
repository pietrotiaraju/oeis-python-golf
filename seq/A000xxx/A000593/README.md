# A000593

> Sum of odd divisors of n.
> — [OEIS A000593](https://oeis.org/A000593)

Offset 1: 1, 1, 4, 1, 6, 4, 8, 1, 13, 6, …

### Python 3 — 60 bytes

```python
n=1
while[print(sum(d>>n%d*n for d in range(1,n+1,2)))]:n+=1
```

**How it works**

- `range(1,n+1,2)` runs over the odd d ≤ n, and `d>>n%d*n` is d when d
  divides n and 0 otherwise: `%` and `*` bind tighter than `>>`, so the
  shift is (n mod d)·n, which is 0 for a divisor and at least n otherwise;
  a shift by n or more clears d, since d ≤ n < 2ⁿ.
- `print` sits in the loop condition: it returns `None`, and `[None]` is a
  non-empty list, so the loop never ends (the [A000007](../A000007/) loop).

**Notes**

- Other versions that print the same terms: `d*(n%d<1)` in place of the
  shift: 61 bytes; the first version of this page,
  `while 1:n+=1;print(sum(d for d in range(1,n+1,2)if n%d<1))`: 62 bytes.
- Exact integer arithmetic, so the program is right for every n.
- Each term costs n/2 steps: about 23700 terms in 60 s here. The b-file has
  10000 terms (up to a(10000)), which take about 13 s; the bar is the whole
  b-file in 60 s.
- a(n) ≤ n², so the 4300-digit int-to-str limit is out of reach.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 62 | first entry |
| 2026-11-07 | Python 3 | 60 | `d>>n%d*n` as the divisor filter, print in the loop condition |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000593), CC BY-SA 4.0.
