# A000111

> Euler or up/down numbers: e.g.f. sec(x) + tan(x). Also for n >= 2, half the number of alternating permutations on n letters (A001250).
> — [OEIS A000111](https://oeis.org/A000111)

Offset 0: 1, 1, 1, 2, 5, 16, 61, 272, 1385, 7936, 50521, 353792, 2702765, 22368256, 199360981, …

### Python 3 — 56 bytes

```python
r=[t:=1]
while[print(t)]:r=[t:=t+x for x in[-t]+r[::-1]]
```

**How it works**

- The Seidel–Entringer triangle: each row starts with 0, and every next
  entry is its left neighbour plus an entry of the row above, read from
  right to left. Row n ends with a(n).

  ```
  1
  0  1
  0  1  1
  0  1  2  2
  0  2  4  5  5
  0  5 10 14 16 16
  ```

  So a row is the running sums of `[0]` followed by the row above
  reversed, and its last entry, the sum of the row above, is the next
  term. The reversal is what makes the counts alternate between up and
  down steps.
- `t` runs along the new row as a walrus sum. At the start of a pass it
  still holds the last entry of the old row, which is a(n), so the extra
  `-t` in front of `r[::-1]` brings the sum to 0 for the leading entry
  without a separate `t=0`. When the comprehension ends, `t` is the last
  entry, a(n + 1), ready to be printed.
- `r=[t:=1]` starts from row 0, `[1]`, with `t = 1`. `while[print(t)]`
  prints and loops forever because `[None]` is a non-empty list.

**Notes**

- Resetting the sum with `[t:=0]+[t:=t+x for x in r[::-1]]` is 2 bytes
  longer than the `-t`. `r=t,=1,` (a tuple) is 1 byte shorter than
  `r=[t:=1]`, but a tuple cannot be added to `[-t]`, and
  `[-t,*r[::-1]]` gives the byte back. Reversing the result instead
  (`[t:=t+x for x in[-t]+r][::-1]`) costs the same. A search over the
  other ways to write this loop (`x-t` or `t-x` sums, putting the 0 or
  `t` at either end, printing `r[-1]` or `sum(r)`) found nothing shorter.
- Exact integer arithmetic, so the program is right for every n; the
  values were checked against 2·a(n + 1) = Σ C(n, k)·a(k)·a(n − k) for
  every term it prints. a(1660) is the first term with more than 4300
  digits, so Python 3.11+ stops there with a `ValueError` from the
  int-to-str limit, which is not counted as a failure; the 1660 terms
  before it print in about a second.
- The b-file has 486 terms (n = 0 to 485, up to 999 digits); they print
  in well under a second. The bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 56 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000111), CC BY-SA 4.0.
