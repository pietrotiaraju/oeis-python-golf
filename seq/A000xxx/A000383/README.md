# A000383

> Hexanacci numbers with a(0) = ... = a(5) = 1.
> — [OEIS A000383](https://oeis.org/A000383)

Offset 0: 1, 1, 1, 1, 1, 1, 6, 11, 21, 41, 81, 161, 321, 636, 1261, …

### Python 3 — 39 bytes

```python
l=[1]*6
while 1:a,*l=*l,sum(l);print(a)
```

**How it works**

- The tetranacci frame of [A000078](../A000078/) with a window of six:
  `l` holds a(n) to a(n+5), starting from six 1s.
- `*l,sum(l)` lists the window and the next term, a(n+6) = a(n) + … + a(n+5);
  `a,*l=` takes the oldest term into `a` and keeps the newest six in `l`.
- `print(a)` prints a(n). Integers are exact, so every term is right.

**Notes**

- Six equal seeds are `[1]*6`, a byte under the tuple `(1,)*6` and four under
  writing them out.
- Printing in the loop condition needs a term ready before the first step:
  `while[print(l[0])]:l=l[1:]+[sum(l)]` is 43 bytes, and
  `a,*l=[1]*6+[6]` + `while[print(a)]:a,*l=*l,sum(l)` is 45. Growing a list
  while iterating over it, `for x in l:print(x);l+=sum(l[-6:]),`, is 43.
- Python's 4300-digit limit on int-to-str conversion stops the program at
  a(14460), the first term with more than 4300 digits, with a `ValueError`;
  the limit is not counted as a failure.
- The b-file has 3359 terms (n = 0 to 3358, the last one has 998 digits) and
  prints at once; the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 39 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000383), CC BY-SA 4.0.
