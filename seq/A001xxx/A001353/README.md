# A001353

> a(n) = 4*a(n-1) - a(n-2) with a(0) = 0, a(1) = 1.
> — [OEIS A001353](https://oeis.org/A001353)

Offset 0: 0, 1, 4, 15, 56, 209, 780, 2911, 10864, 40545, 151316, 564719, 2107560, …

### Python 3 — 34 bytes

```python
a=b=-1
while[print(a:=a-b)]:b-=2*a
```

**How it works**

- `b` holds minus the first difference: before a(n) is printed, `a` is
  a(n−1) and `b` is a(n−1) − a(n), so the walrus `a:=a-b` in the print
  steps `a` to a(n).
- The recurrence a(n+1) = 4·a(n) − a(n−1) gives
  a(n) − a(n+1) = (a(n−1) − a(n)) − 2·a(n), which is `b-=2*a`.
- The start is one step before a(0), with the recurrence run backwards:
  a(−1) = 4·0 − 1 = −1 and a(−1) − a(0) = −1, so `a=b=-1`. This is the
  [A001109](../A001109/) program with 4 in place of 6 (and
  [A001090](../A001090/) with 8).

**Notes**

- a(n) = U(n−1, 2), the Chebyshev polynomial of the second kind at 2:
  (2+√3)ⁿ = [A001075](../A001075/)(n) + a(n)·√3, the solutions of the Pell
  equation x² − 3y² = 1.
- The best without the walrus is `a=0;b=1` /
  `while[print(a)]:a+=b;b+=2*a`, 35 bytes; the plain pair update
  `a,b=b,4*b-a` is 35 too.
- Exact integer arithmetic, so the program is right for every n; Python's
  4300-digit int-to-str limit stops it at about n = 7500.
- The b-file has 201 terms (a(0) to a(200)); the whole of it prints
  instantly, and the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 34 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001353), CC BY-SA 4.0.
