# A000078

> Tetranacci numbers: a(n) = a(n-1) + a(n-2) + a(n-3) + a(n-4) for n >= 4 with a(0) = a(1) = a(2) = 0 and a(3) = 1.
> — [OEIS A000078](https://oeis.org/A000078)

Offset 0: 0, 0, 0, 1, 1, 2, 4, 8, 15, 29, 56, 108, 208, 401, …

### Python 3 — 41 bytes

```python
l=0,0,0,1
while 1:a,*l=*l,sum(l);print(a)
```

**How it works**

- `l` holds four consecutive terms, a(n) to a(n+3), starting from the tuple
  a(0), a(1), a(2), a(3) = 0, 0, 0, 1.
- `*l,sum(l)` builds the five terms a(n) to a(n+4): the old four and their sum,
  which is the next term by the recurrence.
- `a,*l=` splits that tuple: `a` takes the oldest term a(n), and `l` becomes a
  list of the newest four, a(n+1) to a(n+4), so the window has moved one step.
  The first pass turns the tuple into a list, and from then on `l` stays a
  list of four.
- `print(a)` then prints a(n). Integers are exact, so every term is right.

**Notes**

- Printing in the loop condition, as in [A000027](../A000027/), needs a term to
  print before the first step: `while[print(l[0])]:_,*l=*l,sum(l)` is 43 bytes,
  and `a,*l=0,0,0,1,1` + `while[print(a)]:a,*l=*l,sum(l)` is 46.
- Four named variables, `a,b,c,d=0,0,0,1` + `while[print(a)]:a,b,c,d=b,c,d,a+b+c+d`,
  are 53 bytes. Growing a list while iterating over it,
  `l=[0,0,0,1]` + `for x in l:print(x);l+=sum(l[-4:]),`, is 47.
- Python's 4300-digit limit on int-to-str conversion stops the program at
  a(15092), the first term with 4301 digits, after printing a(0) to a(15091).
  The limit is not counted as a failure.
- The b-file has 3506 terms (n = 0 to 3505, the last one has 998 digits) and
  the whole of it prints instantly; the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 41 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000078), CC BY-SA 4.0.
