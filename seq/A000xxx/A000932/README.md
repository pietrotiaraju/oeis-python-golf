# A000932

> a(n) = a(n-1) + n*a(n-2); a(0) = a(1) = 1.
> — [OEIS A000932](https://oeis.org/A000932)

Offset 0: 1, 1, 3, 6, 18, 48, 156, 492, 1740, 6168, 23568, 91416, …

### Python 3 — 40 bytes

```python
a=b=n=1
while[print(a)]:n+=1;a,b=b,b+n*a
```

**How it works**

- After t passes, a = a(t), b = a(t+1) and n = t+1. A pass raises n to
  t+2 and shifts in a(t+2) = a(t+1) + (t+2)·a(t): `a,b=b,b+n*a`.
- The start a(0) = a(1) = 1 with n = 1 is the single chain `a=b=n=1`.

**Notes**

- Folding the counter into the tuple, `a,b=b,b+(n:=n+1)*a`, is 2 bytes
  longer; the in-place pair `b+=n*a;a=b-n*a` is 3 longer.
- Exact integer arithmetic.
- The b-file has 800 terms; they print at once. The bar is the whole
  b-file in 60 s. a(2834) is the first term with more than 4300 digits, so
  printing stops there with a ValueError.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 40 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000932), CC BY-SA 4.0.
