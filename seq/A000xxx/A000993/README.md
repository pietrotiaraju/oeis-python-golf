# A000993

> Number of distinct quadratic residues mod 10^n; also number of distinct n-digit endings of base-10 squares.
> — [OEIS A000993](https://oeis.org/A000993)

Offset 0: 1, 6, 22, 159, 1044, 9121, 78132, 748719, 7161484, 70800861, 699869892, 6978353179, 69580078524, 695292156201, 6947835288052, 69465637212039, 694529215501164, 6944974263529141, 69446563720728612, 694457689921141299, …

### Python 3 — 49 bytes

```python
n=0
while[print((~2**n-4)//6*(-5**-~n//12))]:n+=1
```

**How it works**

- By the Chinese remainder theorem the squares mod 10ⁿ are the pairs
  (square mod 2ⁿ, square mod 5ⁿ), so a(n) = s₂(n)·s₅(n), where s_q(n)
  counts the squares mod qⁿ.
- A nonzero square mod qⁿ is q²ᵏ·u with 2k < n and u a unit square mod
  qⁿ⁻²ᵏ. Mod 5ᵐ there are 2·5ᵐ⁻¹ unit squares; mod 2ᵐ there is 1 for
  m ≤ 3 and 2ᵐ⁻³ after that. Summing the geometric series:
  s₅(n) = ⌈5ⁿ⁺¹/12⌉ and s₂(n) = ⌈(2ⁿ + 5)/6⌉ (that is (2ⁿ+10)/6 for odd n,
  (2ⁿ+8)/6 for even n ≥ 2, and 1 for n = 0).
- Both ceilings come from floor division of negatives:
  `~2**n-4` is −2ⁿ−5, so `(~2**n-4)//6` = −s₂(n); `-5**-~n` is −5ⁿ⁺¹
  (`**` binds tighter than the unary minus, and `-~n` is n+1), so
  `-5**-~n//12` = −s₅(n). The product of the two negatives is a(n), with
  no extra parentheses for the signs.

**Notes**

- Exact integers; the formula is the closed form of the count, so it is
  right for every n. The OEIS entry gives the same value as one floor of
  a longer expression.
- Python's 4300-digit limit on `print` stops the program after a(4301);
  the b-file has the 1001 terms n = 0, …, 1000 and the bar is all of them
  in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 49 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000993), CC BY-SA 4.0.
