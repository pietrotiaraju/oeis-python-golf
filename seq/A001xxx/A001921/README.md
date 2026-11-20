# A001921

> a(n) = 14*a(n-1) - a(n-2) + 6 for n>1, a(0)=0, a(1)=7.
> — [OEIS A001921](https://oeis.org/A001921)

Offset 0: 0, 7, 104, 1455, 20272, 282359, 3932760, 54776287, 762935264, 10626317415, …

### Python 3 — 37 bytes

```python
a=b=-1
while[print(a:=a-b)]:b-=12*a+6
```

**How it works**

- Call the printed values x₀, x₁, … and the value of `b` after pass n bₙ.
  The program sets xₙ₊₁ = xₙ − bₙ and bₙ = bₙ₋₁ − 12xₙ − 6. Subtracting
  xₙ − xₙ₋₁ = −bₙ₋₁ from xₙ₊₁ − xₙ = −bₙ leaves
  xₙ₊₁ − 2xₙ + xₙ₋₁ = 12xₙ + 6, that is xₙ₊₁ = 14xₙ − xₙ₋₁ + 6, the
  recurrence of the name.
- The start `a=b=-1` gives x₀ = −1 − (−1) = 0, then b₀ = −7 and
  x₁ = 0 + 7 = 7: a(0) = 0 and a(1) = 7, so xₙ = a(n) for every n.

**Notes**

- a(n) = [A001922](../A001922/)(n) − 1. `a=0;b=7` / `a+=b;b+=12*a+6` is
  38 bytes and the pair update `a,b=b,14*b-a+6` is 39; with the walrus in
  the print the start can be `a=b=…`.
- Exact integer arithmetic, so the program is right for every n; Python's
  4300-digit int-to-str limit stops it at about n = 3760.
- The b-file has 201 terms (n = 0 to 200); the bar is the whole b-file in
  60 s, which prints instantly.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 37 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001921), CC BY-SA 4.0.
