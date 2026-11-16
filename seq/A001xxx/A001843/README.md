# A001843

> The coding-theoretic function A(n,4,4).
> — [OEIS A001843](https://oeis.org/A001843)

Offset 4: 1, 1, 3, 7, 14, 18, 30, 35, 51, 65, 91, 105, 140, 157, 198, 228, …

### Python 3 — 53 bytes

```python
n=4
while[print((~-n*(n-2>>1)//3-(n%6<1))*n//4)]:n+=1
```

**How it works**

- A(n,4,4) is the largest number of 4-subsets of an n-set any two of which
  meet in at most 2 points (weight-4 words at distance at least 4): the
  packing number of quadruples, where every triple lies in at most one block.
- **Johnson bound.** J(n,4,4) = ⌊n/4·⌊(n−1)/3·⌊(n−2)/2⌋⌋⌋, with
  ⌊(n−1)/3·⌊(n−2)/2⌋⌋ lowered by 1 before the last step when n ≡ 0 (mod 6).
- **Theorem 4.9** of Bao and Ji, *Des. Codes Cryptogr.* 77 (2015) 217–229
  (arXiv:1401.2022): A(n,4,4) = J(n,4,4) for every n. It completes Hanani
  (1960; Steiner quadruple systems, n ≡ 2, 4 (mod 6), and by deleting a
  point n ≡ 1, 3), Brouwer (1978; n ≡ 0) and Ji (2006; n ≡ 5 apart from 21
  values, which Bao and Ji settle).
- **Golf.** `~-n*(n-2>>1)//3` is ⌊(n−1)·⌊(n−2)/2⌋/3⌋, the inner floor
  (`~-n` is n − 1, and `>>` binds looser than `-`); `-(n%6<1)` is the
  correction for 6 | n, and `*n//4` the outer floor. Andrei Zabolotskii's
  formula on the OEIS page, `((n-2)//2*(n-1)//3-(n%6<1))*n//4`, is the same
  computation in 2 more bytes.

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- The b-file has 1000 terms (n = 4 to 1003); the bar is the whole b-file in
  60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 53 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001843), CC BY-SA 4.0.
