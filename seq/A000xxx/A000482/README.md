# A000482

> Unsigned Stirling numbers of first kind s(n,5).
> — [OEIS A000482](https://oeis.org/A000482)

Offset 5: 1, 15, 175, 1960, 22449, 269325, 3416930, 45995730, 657206836, 9957703756, …

### Python 3 — 79 bytes

```python
a=0;b=1;c=e=6;d=11;n=4
while[print(a:=a*n+b)]:b=b*n+c;c=c*n+d;d=d*n+e;e*=n;n+=1
```

**How it works**

- Let c(n,k)=|s(n,k)| count permutations of n elements with k cycles.
  When inserting the new element, either put it after one of the n
  old elements in a cycle, or make it a singleton cycle. Therefore
  **c(n+1,k)=n·c(n,k)+c(n,k−1)**.
- At the start of an iteration, `a, b, c, d, e` hold columns
  k=5, 4, …, 1 of row n. The initial row n=4 is
  (0, 1, 6, 11, 6), including the zero for more cycles than elements.
- `a:=a*n+b` computes column 5 of row n+1 and prints it immediately.
  The body updates the lower columns in descending k, so each update
  still reads the old value of the column below it. The last column
  c(n,1)=(n−1)! needs only multiplication by n.
- Increment n last. The first pass thus prints c(5,5)=1,
  without storing and printing an extra leading zero. On the next
  pass it prints c(6,5)=C(6,2)=15.

**Notes**

- The program keeps only 5 columns, rather than the whole Stirling
  triangle, and uses exact integer additions and multiplications.
  The recurrence proves correctness at every index.
- This extends the three-column loop of [A000399](../A000399/).
  Updating in ascending column order would incorrectly use values
  from row n+1, rather than row n.
- `[print(...)]` stays true even though `print` returns `None`.
  Putting the first update inside that print handles the output
  offset without a separate initialization for row 5.
- Counts grow at factorial scale; Python 3.11+ eventually reaches its
  default 4300-digit integer-to-string limit, an interpreter limit
  rather than a failure of the recurrence.
- The b-file has 96 terms (indices 5 through 100). The bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 79 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000482), CC BY-SA 4.0.
