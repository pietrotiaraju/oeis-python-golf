# A000629

> Number of necklaces of partitions of n+1 labeled beads.
> — [OEIS A000629](https://oeis.org/A000629)

Offset 0: 1, 2, 6, 26, 150, 1082, 9366, 94586, 1091670, 14174522, 204495126, 3245265146, 56183135190, …

### Python 3 — 56 bytes

```python
r=[t:=1]
while[print(t)]:r=[t:=t+x for x in[sum(r)-t]+r]
```

**How it works**

- a(n) = 2·A000670(n) − 0ⁿ (Somos). The program runs the array of
  [A000670](../A000670/): each row is the running sums of s(n) = the sum
  of the row above, followed by the row above, so the first entries s(n)
  are the Fubini numbers and the last entry of row n is
  s(n) + Σ_{j<n} C(n,j)·s(j) = 2·s(n) for n ≥ 1, and 1 for n = 0.

  ```
   1
   1  2
   3  4  6
  13 16 20 26
  75 88 104 124 150
  ```
- `t` runs along the new row as a walrus sum. At the start of a pass it
  holds the last entry of the old row, so the first element `sum(r)-t`
  brings it to s(n); then it adds the old row in order, and ends on the
  last entry, which the `while` header prints.

**Notes**

- The values were checked against a(n) = 1 + Σ_{j<n} C(n,j)·a(j) for
  every printed term.
- Exact integer arithmetic, so the program is right for every n. Python's
  4300-digit limit for printing ints stops it at a(1484); the 1484 terms
  before it print in about a second.
- The b-file has 425 terms; the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 56 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000629), CC BY-SA 4.0.
