# A001835

> a(n) = 4*a(n-1) - a(n-2), with a(0) = 1, a(1) = 1.
> — [OEIS A001835](https://oeis.org/A001835)

Offset 0: 1, 1, 3, 11, 41, 153, 571, 2131, 7953, 29681, 110771, 413403, 1542841, …

### Python 3 — 33 bytes

```python
a=b=1
while[print(a)]:a,b=b,4*b-a
```

**How it works**

- `a` is a(n) and `b` is a(n + 1); the tuple update applies
  a(n + 2) = 4a(n + 1) − a(n). Both seeds are 1, so one chained assignment
  starts them.
- a(n) counts the domino tilings of a 3 × 2(n − 1) rectangle; exact
  integers, so every term is right.

**Notes**

- The in-place form `a+=b;b+=2*a` (as in [A001075](../A001075/) and
  [A001834](../A001834/)) needs the start `a=1;b=0` here: 35 bytes.
- a(1 − n) = a(n), and 3a(n + 1)² − [A001834](../A001834/)(n)² = 2.
- Python's 4300-digit int-to-str limit stops the program at a(7520) (an
  interpreter limit, not a wrong term).
- The b-file has 201 terms (n = 0 to 200); the bar is the whole b-file
  in 60 s, which takes well under a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-16 | Python 3 | 33 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001835), CC BY-SA 4.0.
