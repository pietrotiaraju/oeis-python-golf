# A000670

> Fubini numbers: number of preferential arrangements of n labeled elements; or number of weak orders on n labeled elements; or number of ordered partitions of [n].
> — [OEIS A000670](https://oeis.org/A000670)

Offset 0: 1, 1, 3, 13, 75, 541, 4683, 47293, 545835, 7087261, 102247563, 1622632573, 28091567595, 526858348381, …

### Python 3 — 59 bytes

```python
r=[t:=1]
while[print(r[0])]:r=[t:=t+x for x in[sum(r)-t]+r]
```

**How it works**

- In the array T(n,0) = s(n), T(n,k) = T(n,k−1) + T(n−1,k−1) (each row is
  the running sums of s(n) followed by the row above, as in Bell's
  triangle), T(n,n) = Σⱼ C(n,j)·s(j), and the sum of row n−1 is
  T(n,n) − T(n,0) = Σ_{j<n} C(n,j)·s(j).
- So starting each row with the sum of the row above gives
  s(n) = Σ_{j<n} C(n,j)·s(j), s(0) = 1: the Fubini recurrence. The program
  prints the first entry of each row.

  ```
   1
   1  2
   3  4  6
  13 16 20 26
  75 88 104 124 150
  ```
- `t` runs along the new row as a walrus sum. At the start of a pass it
  holds the last entry of the old row, so the first element `sum(r)-t`
  brings it to s(n); then it adds the old row in order.

**Notes**

- The last entry of row n is s(n) + Σ_{j<n} C(n,j)·s(j) = 2·s(n) for n ≥ 1,
  which is [A000629](../A000629/): that program prints `t` instead of
  `r[0]`, 3 bytes less. Printing `t+1>>1` here would be 2 bytes longer.
- The values were checked against a(n) = Σₖ k!·S(n,k) for every printed
  term.
- Exact integer arithmetic, so the program is right for every n. Python's
  4300-digit limit for printing ints stops it at a(1485); the 1485 terms
  before it print in about a second.
- The b-file has 425 terms; the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 59 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000670), CC BY-SA 4.0.
