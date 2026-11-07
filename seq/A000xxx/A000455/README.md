# A000455

> Digits of powers of 2.
> — [OEIS A000455](https://oeis.org/A000455)

Offset 0: 1, 2, 4, 8, 1, 6, 3, 2, 6, 4, …

The decimal digits of 1, 2, 4, 8, 16, 32, … written one after another.

### Python 3 — 34 bytes

```python
n=1
while[*map(print,str(n))]:n*=2
```

**How it works**

- n runs through the powers 1, 2, 4, 8, … and `str(n)` is its decimal
  string, most significant digit first.
- `map(print,str(n))` prints each digit character on its own line, and
  `[*…]` unpacks it into a list of `None`s so that the prints actually
  run. A power of 2 has at least one digit, so the list is never empty
  and the `while` never ends.
- After the last digit of 2ᵏ the body doubles n.

**Notes**

- Other versions that print the same terms: the comprehension
  `while[print(d)for d in str(n)]:n*=2`, 39 bytes; `'%d'%n` or `f'{n}'`
  in place of `str(n)` tie.
- Exact integer arithmetic, so the program is right for every n.
- The b-file's 10000 terms (the powers up to 2²⁵⁶) print in 0.8 s here.
  The b-file has 10000 terms (up to a(9999)); the bar is the whole b-file
  in 60 s.
- 2¹⁴²⁸⁵ is the first power with more than 4300 digits, so after the
  digits of 2¹⁴²⁸⁴ (about 30.7 million terms) `str` raises and printing
  stops.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 39 | first entry |
| 2026-11-07 | Python 3 | 34 | `[*map(print,str(n))]` |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000455), CC BY-SA 4.0.
