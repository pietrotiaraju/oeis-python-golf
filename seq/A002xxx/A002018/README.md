# A002018

> From a distribution problem.
> — [OEIS A002018](https://oeis.org/A002018)

Offset 0: 1, 1, 4, 33, 480, 11010, 367560, 16854390, 1016930880, 78124095000, 7446314383200, …

### Python 3 — 53 bytes

```python
a=b=n=1
while[print(a)]:a,b=n*(n*a-b//2),n*~-n*a;n+=1
```

**How it works**

- The title only names the source (Anand, Dumir and Gupta, *A
  combinatorial distribution problem*, Duke Math. J. 33). The
  entry gives a(n) = (n − 1)!·n!·[x^{n−1}] (1 − x)^{−3/2}·e^{x/2} for
  n > 0 and the recurrence **a(n) = n·(n·a(n − 1) − C(n − 1, 2)·a(n − 2))**
  (Manyama). They agree: y = (1 − x)^{−3/2}e^{x/2} satisfies
  2(1 − x)·y′ = (4 − x)·y, so its coefficients obey
  2(m + 1)c(m + 1) = (2m + 4)c(m) − c(m − 1), and with
  a(n) = (n − 1)!·n!·c(n − 1) this is the recurrence above.
- `b` holds (n − 1)(n − 2)·a(n − 2). That is a product of two consecutive
  integers times an integer, so it is even and `b//2` = C(n − 1, 2)·a(n − 2)
  exactly. Each pass prints a = a(n − 1), then sets a = n·(n·a − b/2) and
  b = n(n − 1)·a(n − 1) for the next n.
- The recurrence also holds at n = 1, where C(0, 2) = 0: the start value
  b = 1 gives `b//2` = 0, so a(1) = 1·(1·1 − 0) = 1.

**Notes**

- `~-n` is n − 1. Exact integer arithmetic, so the program is right for
  every n.
- The b-file has 254 terms (n = 0 to 253); the bar is the whole b-file in
  60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 53 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002018), CC BY-SA 4.0.
