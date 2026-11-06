# A000288

> Tetranacci numbers: a(n) = a(n-1) + a(n-2) + a(n-3) + a(n-4) with a(0) = a(1) = a(2) = a(3) = 1.
> — [OEIS A000288](https://oeis.org/A000288)

Offset 0: 1, 1, 1, 1, 4, 7, 13, 25, 49, 94, 181, 349, 673, 1297, 2500, …

### Python 3 — 39 bytes

```python
l=[1]*4
while 1:a,*l=*l,sum(l);print(a)
```

**How it works**

- The [A000078](../A000078/) window: `l` holds four consecutive terms,
  a(n) to a(n+3), starting from a(0) = a(1) = a(2) = a(3) = 1.
- `*l,sum(l)` builds the five terms a(n) to a(n+4), the old four and their
  sum, which is the next term by the recurrence.
- `a,*l=` splits them: `a` takes the oldest term a(n), `l` keeps the newest
  four, and `print(a)` prints a(n).
- Four equal starting terms make the start `[1]*4`, two bytes under the
  `l=0,0,0,1` of A000078.

**Notes**

- Printing in the loop condition needs a term to print before the first
  step: `a,*l=[1]*4` + `while[print(a)]:a,*l=*l,a+sum(l)` is 43 bytes.
- The shorter recurrence a(n) = 2·a(n−1) − a(n−5) (Librandi, on the OEIS
  page) needs a five-term window and the start 1, 1, 1, 1, 4, so it costs
  more than it saves.
- Exact integers, so every term is right. Python's 4300-digit int-to-str
  limit stops the program at a(15090), after printing a(0) to a(15089).
- The b-file has 3504 terms (up to a(3503), 998 digits) and all of them
  print at once; the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 39 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000288), CC BY-SA 4.0.
