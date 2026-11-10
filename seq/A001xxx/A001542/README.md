# A001542

> a(n) = 6*a(n-1) - a(n-2) for n > 1, a(0)=0 and a(1)=2.
> — [OEIS A001542](https://oeis.org/A001542)

Offset 0: 0, 2, 12, 70, 408, 2378, 13860, 80782, 470832, 2744210, 15994428, …

### Python 3 — 34 bytes

```python
a=b=-2
while[print(a:=a-b)]:b-=4*a
```

**How it works**

- Before a(n) is printed, `a` is a(n−1) and `b` is a(n−1) − a(n), so the
  walrus `a:=a-b` in the print steps `a` to a(n).
- The recurrence a(n+1) = 6·a(n) − a(n−1) gives
  a(n) − a(n+1) = (a(n−1) − a(n)) − 4·a(n), which is `b-=4*a`.
- The start is one step before a(0), with the recurrence run backwards:
  a(−1) = 6·0 − 2 = −2 and a(−1) − a(0) = −2, so `a=b=-2`. This is the
  [A001109](../A001109/) program with −2 in place of −1: a(n) is twice
  A001109(n).

**Notes**

- a(n) = 2y where x² − 2y² = 1 is the Pell equation (x =
  [A001541](../A001541/)(n)); equally, a(n) is the Pell number P(2n).
- Without the walrus, `a=0;b=2` / `while[print(a)]:a+=b;b+=4*a` is
  35 bytes.
- Exact integer arithmetic, so the program is right for every n; Python's
  4300-digit int-to-str limit stops it at about n = 5600.
- The b-file has 101 terms (a(0) to a(100)); the bar is the whole b-file in
  60 s, which prints instantly.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-10 | Python 3 | 34 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001542), CC BY-SA 4.0.
