# A001148

> Final digit of 3^n.
> — [OEIS A001148](https://oeis.org/A001148)

Offset 0: 1, 3, 9, 7, 1, 3, 9, 7, 1, 3, 9, 7, …

### Python 3 — 27 bytes

```python
x=1
while[print(x%10)]:x*=3
```

**How it works**

- Keep x = 3ⁿ itself (`x*=3`) and print its last digit `x%10`: the
  definition word for word, so there is nothing to prove.
- Reducing as we go, `x=x*3%10` with `print(x)`, is one byte longer:
  `%10` in the print costs 3 bytes, the reducing update costs 4 more than
  `x*=3`. Printing the period `1, 3, 9, 7` in a `while 1:` loop with
  `sep='\n'` is 30 bytes.
- `while[print(…)]:` prints in the loop test (`[None]` is a true list).

**Notes**

- Exact for every n. x grows by about 1.6 bits a step, so a step costs time
  linear in n; the program still prints about 176 000 terms in 10 s.
  `x%10` is a one-digit int, so the 4300-digit int-to-str limit never
  applies.
- The b-file is the OEIS one synthesized from the entry (81 terms,
  a(0)…a(80)); the bar is all of them in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 27 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001148), CC BY-SA 4.0.
