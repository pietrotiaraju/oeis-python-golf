# A000454

> Unsigned Stirling numbers of first kind s(n,4).
> — [OEIS A000454](https://oeis.org/A000454)

Offset 4: 1, 10, 85, 735, 6769, 67284, 723680, 8409500, 105258076, 1414014888, …

### Python 3 — 68 bytes

```python
a=0;b=1;c=3;d=2;n=3
while[print(a:=a*n+b)]:b=b*n+c;c=c*n+d;d*=n;n+=1
```

**How it works**

- Let c(n,k)=|s(n,k)| count permutations of n elements with k cycles.
  When inserting the new element, either put it after one of the n
  old elements in a cycle, or make it a singleton cycle. Therefore
  **c(n+1,k)=n·c(n,k)+c(n,k−1)**.
- At the start of an iteration, `a, b, c, d` hold columns
  k=4, 3, …, 1 of row n. The initial row n=3 is
  (0, 1, 3, 2), including the zero for more cycles than elements.
- `a:=a*n+b` computes column 4 of row n+1 and prints it immediately.
  The body updates the lower columns in descending k, so each update
  still reads the old value of the column below it. The last column
  c(n,1)=(n−1)! needs only multiplication by n.
- Increment n last. The first pass thus prints c(4,4)=1,
  without storing and printing an extra leading zero. On the next
  pass it prints c(5,4)=C(5,2)=10.

**Notes**

- The program keeps only 4 columns, rather than the whole Stirling
  triangle, and uses exact integer additions and multiplications.
  The recurrence proves correctness at every index.
- This extends the three-column loop of [A000399](../A000399/).
  Updating in ascending column order would incorrectly use values
  from row n+1, rather than row n.
- `[print(...)]` stays true even though `print` returns `None`.
  Putting the first update inside that print handles the output
  offset without a separate initialization for row 4.
- Counts grow at factorial scale; Python 3.11+ eventually reaches its
  default 4300-digit integer-to-string limit, an interpreter limit
  rather than a failure of the recurrence.
- The b-file has 97 terms (indices 4 through 100). The bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 68 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000454), CC BY-SA 4.0.
