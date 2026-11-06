# A000321

> H_n(-1/2), where H_n(x) is Hermite polynomial of degree n.
> — [OEIS A000321](https://oeis.org/A000321)

Offset 0: 1, −1, −1, 5, 1, −41, 31, 461, −895, −6481, 22591, 107029, …

### Python 3 — 43 bytes

```python
n=a=0;b=1
while[print(b)]:a,b=b,-b-n*a;n+=2
```

**How it works**

- The Hermite recurrence H_(k+1)(x) = 2x·H_k(x) − 2k·H_(k−1)(x) at
  x = −1/2 is the recurrence in the OEIS entry,
  a(k+1) = −a(k) − 2k·a(k−1), with a(0) = 1 (the e.g.f. is exp(−x − x²)).
- `b` is a(k) and `a` is a(k−1); `n` holds 2k, so one tuple update moves
  the window one step and `n+=2` keeps the coefficient.
- The program starts one step early: at k = 0 the coefficient 2k is 0, so
  a(−1) can be anything and `n=a=0` sets it together with n.

**Notes**

- Exact integer arithmetic, correct for every n.
- Updating inside `print`, `a=b=1;n=-2` / `while[print(b:=-n*a-(a:=b))]:n+=2`
  (the walrus reads the old `a` before overwriting it), is 44 bytes; the
  two plain steps `b=-b-n*a;a=-b-n*a` (the second gives back the old b)
  are 5 bytes longer than the tuple.
- The whole b-file (733 terms) prints in well under a second; the program
  stops after a(2618), when the next term passes the 4300-digit
  int-to-str limit of Python 3.11+. The bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 43 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000321), CC BY-SA 4.0.
