# A001250

> Number of alternating permutations of order n.
> — [OEIS A001250](https://oeis.org/A001250)

Offset 0: 1, 1, 2, 4, 10, 32, 122, 544, 2770, 15872, 101042, …

For n ≥ 2, a(n) counts the up-down permutations of 1, …, n plus the
down-up ones. Complementing (i ↦ n + 1 − i) swaps the two kinds, so
a(n) = 2·E(n), with E the Euler zigzag numbers of
[A000111](../../A000xxx/A000111/); a(0) = a(1) = 1.

### Python 3 — 66 bytes

```python
r=[t:=1]
while[print(sum(r[-2:]))]:r=[t:=t+x for x in[-t]+r[::-1]]
```

**How it works**

- The Seidel–Entringer loop of [A000111](../../A000xxx/A000111/): each row
  starts with 0, and every next entry is its left neighbour plus an entry
  of the row above, read from right to left. Row n ends with E(n).

  ```
  1
  0  1
  0  1  1
  0  1  2  2
  0  2  4  5  5
  0  5 10 14 16 16
  ```

- The program prints the sum of the last two entries of each row. From
  row 2 on, the last step of the running sum adds the first entry of the
  row above, which is 0, so the last two entries are equal and their sum
  is 2·E(n) = a(n). Row 1, `[0, 1]`, gives 0 + 1 = 1 = a(1), and row 0,
  `[1]`, has only one entry, so `r[-2:]` is `[1]` and the sum is
  1 = a(0). The slice is what lets one expression cover all three cases.
- `t` runs along the new row as a walrus sum. At the start of a pass it
  holds the last entry of the old row, so the `-t` in front of `r[::-1]`
  brings the sum to 0 for the leading entry. `while[print(…)]` loops
  forever because `[None]` is a non-empty list.

**Notes**

- A search over starting rows of length up to 4 (entries −3 to 3), the
  other leading entries (`0`, `-2*t`, `±1`, `t`), with and without the
  reversal, and reads such as `t`, `r[1]`, `r[2]`, `2*r[1]` or `t-r[1]`
  found no other way to get 1, 1, 2, 4, 10, … from this loop; `t+r[-2]`
  fails on row 0. Printing a(0) separately and then `t+r[-2]` after each
  update is 72 bytes.
- Exact integer arithmetic, so the program is right for every n. a(1660)
  is the first term with more than 4300 digits, so Python 3.11+ stops
  there with a `ValueError` from the int-to-str limit, which is not
  counted as a failure.
- The b-file has 501 terms (n = 0 to 500); the bar is the whole b-file in
  60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 66 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001250), CC BY-SA 4.0.
