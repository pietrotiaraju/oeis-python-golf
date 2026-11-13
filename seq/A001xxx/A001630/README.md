# A001630

> Tetranacci numbers: a(n) = a(n-1) + a(n-2) + a(n-3) + a(n-4), with a(0)=a(1)=0, a(2)=1, a(3)=2.
> — [OEIS A001630](https://oeis.org/A001630)

Offset 0: 0, 0, 1, 2, 3, 6, 12, 23, 44, 85, 164, 316, 609, 1174, 2263, 4362, …

### Python 3 — 41 bytes

```python
l=0,0,1,2
while 1:a,*l=*l,sum(l);print(a)
```

**How it works**

- `l` holds 4 consecutive terms, a(n) to a(n+3), starting from the
  data's a(0) to a(3) = 0, 0, 1, 2.
- `*l,sum(l)` builds the 5 terms a(n) to a(n+4): the old 4 and
  `sum(l)` = a(n) + a(n+1) + a(n+2) + a(n+3), which is a(n+4) by the tetranacci recurrence.
- `a,*l=` splits that tuple: `a` takes the oldest term a(n), and `l`
  becomes a list of the newest 4, a(n+1) to a(n+4), so the window has
  moved one step. `print(a)` then prints a(n), so the terms come out in
  order from a(0).
- Integers are exact, so every term is right, for every n.

**Notes**

- This is the program of [A000078](../../A000xxx/A000078/) with the
  seeds 0, 0, 1, 2. Since the recurrence is linear, a(n) = A000078(n) +
  A000078(n+1) (the entry's own formula), but printing that sum costs
  bytes: `print(a+l[0])` on the A000078 window is 46.
- The entry's a(n) = 2a(n−1) − a(n−5) (multiply the characteristic
  polynomial by x − 1) gives the growing list `l=[0,0,1,2,3]` /
  `for x in l:l+=2*l[-1]-x,;print(x)`, 47 bytes. Four named variables
  cost more, and no chain of in-place statements can win here: four
  variables need four statements, at least 45 bytes with the shortest start.
- Python's 4300-digit limit on int-to-str conversion stops the program
  after a(15089), the last term with at most 4300 digits; the limit
  is not counted as a failure.
- The b-file has 3504 terms (a(0) to a(3503)); they print in
  well under a second. The bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 41 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001630), CC BY-SA 4.0.
