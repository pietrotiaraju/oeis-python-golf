# A000064

> Partial sums of (unordered) ways of making change for n cents using coins of 1, 2, 5, 10 cents.
> — [OEIS A000064](https://oeis.org/A000064)

Offset 0: 1, 2, 4, 6, 9, 13, 18, 24, 31, 39, 50, 62, 77, 93, 112, 134, 159, …

### Python 3 — 69 bytes

```python
m=12
while[print(sum((m-j)//10*(j*j//4)for j in range(m,1,-5)))]:m+=1
```

**How it works**

Summing [A000008](../A000008/) up to n is the same as adding a second kind
of 1-cent coin: a(n) counts the partitions of n into parts 1 (two kinds),
2, 5 and 10, with g.f. 1/((1 − x)²(1 − x²)(1 − x⁵)(1 − x¹⁰)).

- Pay 5t cents with nickels and dimes: ⌊t/2⌋ + 1 ways (0 to ⌊t/2⌋ dimes).
- Pay the other k = n − 5t cents with the two kinds of 1 and the 2s:
  with b twos there are k − 2b + 1 ways to split the rest, and the sum
  over b is ⌊(k + 2)²/4⌋ (it is (a + 1)² for k = 2a and (a + 1)(a + 2)
  for k = 2a + 1).
- With m = n + 12 and j = k + 2 = n + 2 − 5t, the first factor is
  (m − j)/10 = 1 + t/2 rounded down, so a(n) is the sum of
  `(m-j)//10*(j*j//4)` over j = m, m − 5, m − 10, … down to 2.
- Starting the loop at m instead of n + 2 costs nothing: the first two
  values j = m and j = m − 5 have weight 0. Counting with m = n + 12
  directly instead of n saves the `+10` in the weight and the `+2` in the
  range.
- `while[print(...)]:` prints in the loop condition (`[None]` is true).

**Notes**

- Term n takes about n/5 steps, so the whole b-file (n ≤ 1000) prints in
  well under a second.
- Another split gives the same length: the coins 1, 2, 5 alone pay k cents
  in round((k + 4)²/20) ways ([A000115](https://oeis.org/A000115)), the
  other 1-cent coin and the dimes pay s cents in ⌊s/10⌋ + 1 ways, and
  `m=14` with `(m-j)//10*((j*j+9)//20)for j in range(m)` is also 69 bytes.
- Folding the nickels in as well, the coins 1, 1, 2, 5 pay k cents in
  ⌊(j³ − 31j + 200)/480⌋ ways with j = 2k + 9; summing that over the dimes
  (`m=9`, `range(m,0,-20)`, `m+=2`) is 71 bytes.
- The closed form on the OEIS entry (Tani Akinari, 2014) needs a (−1)ⁿ term
  and a period-5 table, both growing with n, and is over 80 bytes.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 69 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000064), CC BY-SA 4.0.
