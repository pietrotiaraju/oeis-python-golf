# A001476

> Numbers that are not the sum of distinct positive cubes.
> — [OEIS A001476](https://oeis.org/A001476)

Offset 1: 2, 3, 4, 5, 6, 7, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, …

### Python 3 — 61 bytes

```python
s=1
for n in range(12759):s|=s<<n**3*(n<24);s>>n&1or print(n)
```

**How it works**

- **Subset sums as bits**, as in [A001422](../A001422/) for squares. Bit j
  of `s` is set when j is a sum of distinct cubes among those added so far
  (the empty sum gives bit 0). `s|=s<<n**3` adds n³ as an optional new
  part. A representation of n only uses cubes ≤ n, and those are all in
  once the pass for n has added n³ (n³ ≥ n), so bit n is final there and
  the program prints n when it is clear. 0 (the empty sum) and 1 = 1³ are
  not printed, as in the entry.
- **Only the cubes up to 23³.** For n ≥ 24 the shift is `n**3*0` = 0, so
  `s` stops growing: 24³ = 13824 is larger than every n the loop looks at,
  and keeping the shifts would make `s` astronomically long.
- **Why it can stop at 12758 (Dressler and Parker, 1974: 12758 is the
  largest such number).** Self-contained argument: every integer from
  12759 to 26582 = 12758 + 24³ is a sum of distinct cubes among 1³, …, 23³
  (the same bit computation shows it). Induction on k ≥ 23: if every
  integer in [12759, X] is a sum of distinct cubes ≤ k³ and
  X ≥ 12758 + (k + 1)³, then for n in (X, X + (k + 1)³], n − (k + 1)³ lies in
  [12759, X], so n is that sum plus (k + 1)³, a new distinct cube. The new
  end X + (k + 1)³ ≥ 12758 + 2(k + 1)³ is again ≥ 12758 + (k + 2)³, since
  2(k + 1)³ ≥ (k + 2)³ for k ≥ 3. So every n ≥ 12759 is a sum of distinct
  cubes, and the 2788 numbers printed for n ≤ 12758 are the whole sequence;
  the program ends after the last one.
- Exact integer arithmetic; `s` has about 76000 bits.

**Notes**

- The sequence is finite (keyword `fini`, `full`); the bar is all 2788
  terms, which print in a fraction of a second.
- `s|=n<24and s<<n**3` is one byte longer; two loops (cubes, then the
  scan) are 12 bytes longer.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-10 | Python 3 | 61 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001476), CC BY-SA 4.0.
