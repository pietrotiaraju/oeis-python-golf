# A001541

> a(0) = 1, a(1) = 3; for n > 1, a(n) = 6*a(n-1) - a(n-2).
> — [OEIS A001541](https://oeis.org/A001541)

Offset 0: 1, 3, 17, 99, 577, 3363, 19601, 114243, 665857, 3880899, 22619537, …

### Python 3 — 35 bytes

```python
a=1;b=2
while[print(a)]:a+=b;b+=4*a
```

**How it works**

- `b` holds the forward difference: before a(n) is printed, `a` = a(n) and
  `b` = a(n+1) − a(n). Then `a+=b` makes a = a(n+1), and the recurrence
  a(n+2) = 6a(n+1) − a(n) gives
  a(n+2) − a(n+1) = (a(n+1) − a(n)) + 4·a(n+1), which is `b+=4*a`.
- The start is a(0) = 1 and a(1) − a(0) = 2.

**Notes**

- a(n) is the x part of (3 + 2√2)ⁿ = x + y√2, the solutions of the Pell
  equation x² − 2y² = 1 (y = [A001109](../A001109/)(n)).
- `a=b=1` / `while[print(a)]:a+=2*b;b+=2*a` (two steps of the √2
  convergents, as in [A001075](../A001075/)) and `a=1;b=3` /
  `a,b=b,6*b-a` are 35 bytes too. The walrus form of
  [A001542](../A001542/) needs the start a=3;b=2 here, 35 again. A search
  over all two-variable programs with one or two in-place statements, with
  or without a walrus in the print (coefficients up to 6, starts −3 to 9),
  found nothing shorter.
- Exact integer arithmetic, so the program is right for every n; Python's
  4300-digit int-to-str limit stops it at about n = 5600.
- The b-file has 201 terms (a(0) to a(200)); the bar is the whole b-file in
  60 s, which prints instantly.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-10 | Python 3 | 35 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001541), CC BY-SA 4.0.
