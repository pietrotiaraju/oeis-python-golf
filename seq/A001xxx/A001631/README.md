# A001631

> Tetranacci numbers: a(n) = a(n-1) + a(n-2) + a(n-3) + a(n-4), with initial conditions a(0..3) = (0, 0, 1, 0).
> — [OEIS A001631](https://oeis.org/A001631)

Offset 0: 0, 0, 1, 0, 1, 2, 4, 7, 14, 27, 52, 100, 193, 372, 717, 1382, 2664, …

### Python 3 — 41 bytes

```python
l=0,0,1,0
while 1:a,*l=*l,sum(l);print(a)
```

**How it works**

- `l` holds 4 consecutive terms, a(n) to a(n+3), starting from the
  data's a(0) to a(3) = 0, 0, 1, 0.
- `*l,sum(l)` builds the 5 terms a(n) to a(n+4): the old 4 and
  `sum(l)` = a(n) + a(n+1) + a(n+2) + a(n+3), which is a(n+4) by the tetranacci recurrence.
- `a,*l=` splits that tuple: `a` takes the oldest term a(n), and `l`
  becomes a list of the newest 4, a(n+1) to a(n+4), so the window has
  moved one step. `print(a)` then prints a(n), so the terms come out in
  order from a(0).
- Integers are exact, so every term is right, for every n.

**Notes**

- This is the program of [A000078](../../A000xxx/A000078/) with the
  seeds 0, 0, 1, 0. By linearity a(n) = A000078(n+1) − A000078(n), but
  printing that costs bytes: `print(l[0]-a)` on the A000078 window is 46.
- Four named variables cost more, and no chain of in-place statements can
  win: four variables need four statements, at least 45 bytes with the
  shortest start.
- Python's 4300-digit limit on int-to-str conversion stops the program
  after a(15091), the last term with at most 4300 digits; the limit
  is not counted as a failure.
- The b-file has 1001 terms (a(0) to a(1000)); they print in
  well under a second. The bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 41 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001631), CC BY-SA 4.0.
