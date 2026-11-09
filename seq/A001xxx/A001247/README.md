# A001247

> Squares of Bell numbers.
> — [OEIS A001247](https://oeis.org/A001247)

Offset 0: 1, 1, 4, 25, 225, 2704, 41209, 769129, 17139600, 447195609, …

### Python 3 — 50 bytes

```python
t,*r=1,
while[print(t*t)]:r=[t:=t+x for x in[0]+r]
```

**How it works**

- The Bell-triangle loop of [A000110](../../A000xxx/A000110/), printing
  `t*t`. In the Bell triangle (Aitken's array) each row starts with the
  last entry of the row above, and every next entry is its left neighbour
  plus the entry above that neighbour; row n starts with B(n) and ends
  with B(n + 1).

  ```
  1
  1  2
  2  3  5
  5  7 10 15
  ```

- `t` runs along the new row as a walrus sum. It starts as the last entry
  of the old row, which is also the first entry of the new one, so the
  `0` in `[0]+r` writes that entry unchanged, and each `x` of the old row
  then adds the entry above. When the comprehension ends, `t` is the next
  Bell number.
- `t,*r=1,` sets `t = 1` and `r = []`: the empty row before the first one,
  whose last entry is B(0) = 1. `while[print(…)]` loops forever because
  `[None]` is a non-empty list.

**Notes**

- Exact integer arithmetic, so the program is right for every n. a(1097)
  is the first term with more than 4300 digits, so Python 3.11+ stops
  there with a `ValueError` from the int-to-str limit, which is not counted
  as a failure.
- The b-file has 101 terms (n = 0 to 100); the bar is the whole b-file in
  60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 50 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001247), CC BY-SA 4.0.
