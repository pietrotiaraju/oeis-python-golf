# A000110

> Bell or exponential numbers: number of ways to partition a set of n labeled elements.
> — [OEIS A000110](https://oeis.org/A000110)

Offset 0: 1, 1, 2, 5, 15, 52, 203, 877, 4140, 21147, 115975, 678570, 4213597, 27644437, 190899322, 1382958545, …

### Python 3 — 48 bytes

```python
t,*r=1,
while[print(t)]:r=[t:=t+x for x in[0]+r]
```

**How it works**

- The Bell triangle (Aitken's array): each row starts with the last entry
  of the row above, and every next entry is its left neighbour plus the
  entry above that neighbour.

  ```
  1
  1  2
  2  3  5
  5  7 10 15
  ```

  Row n starts with B(n) and ends with B(n + 1).
- `t` runs along the new row as a walrus sum. It starts as the last entry
  of the old row, which is also the first entry of the new one, so the
  extra `0` in `[0]+r` writes that first entry unchanged, and each `x` of
  the old row then adds the entry above. When the comprehension ends,
  `t` is the last entry, B(n + 1), ready to be printed.
- `t,*r=1,` sets `t = 1` and `r = []` in 7 bytes: the empty "row" before
  the first one, whose last entry is B(0) = 1. Its next row is `[1]`, so
  the program prints 1, 1, 2, 5, … `while[print(t)]` prints and loops
  forever because `[None]` is a non-empty list.

**Notes**

- `r=[];t=1` is 1 byte longer than `t,*r=1,`, and `r=[t]+[t:=t+x for x
  in r]` is 1 byte longer than prepending the `0`. Keeping the `0` in the
  list, `r[1:]=[t:=t+x for x in r]` with `t=1;r=[0]`, costs 3 bytes more.
  The binomial recurrence B(n + 1) = Σ C(n, k)·B(k) needs `math.comb`
  and is longer still.
- Exact integer arithmetic, so the program is right for every n.
  a(1981) is the first term with more than 4300 digits, so Python 3.11+
  stops there with a `ValueError` from the int-to-str limit, which is not
  counted as a failure.
- The b-file has 501 terms (n = 0 to 500); they print in well under a
  second. The bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 48 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000110), CC BY-SA 4.0.
