# A000322

> Pentanacci numbers: a(n) = a(n-1) + a(n-2) + a(n-3) + a(n-4) + a(n-5) with a(0) = a(1) = a(2) = a(3) = a(4) = 1.
> — [OEIS A000322](https://oeis.org/A000322)

Offset 0: 1, 1, 1, 1, 1, 5, 9, 17, 33, 65, 129, 253, 497, 977, 1921, …

### Python 3 — 39 bytes

```python
l=[1]*5
while 1:a,*l=*l,sum(l);print(a)
```

**How it works**

- The [A000288](../A000288/) window with five terms: `l` holds a(n) to
  a(n+4), starting from five 1s, which `[1]*5` writes in 7 bytes.
- `*l,sum(l)` builds the six terms a(n) to a(n+5), the old five and their
  sum, which is the next term by the recurrence.
- `a,*l=` splits them: `a` takes the oldest term a(n), `l` keeps the newest
  five, and `print(a)` prints a(n).

**Notes**

- Exact integers, so every term is right.
- Printing in the loop condition needs a term before the first step:
  `a,*l=[1]*5` + `while[print(a)]:a,*l=*l,a+sum(l)` is 43 bytes. A list that
  grows while a `for` loop reads it, `for x in l:print(x);l+=sum(l[-5:]),`,
  is 43 as well. The shorter recurrence a(n) = 2·a(n−1) − a(n−6) needs a
  six-term window and a start that is not all equal, so it costs more than
  it saves.
- Python's 4300-digit int-to-str limit stops the program at a(14650), after
  printing a(0) to a(14649).
- The b-file has 3403 terms (n = 0 to 3402) and all of them print at once;
  the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 39 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000322), CC BY-SA 4.0.
