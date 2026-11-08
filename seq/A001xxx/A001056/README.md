# A001056

> a(n) = a(n-1)*a(n-2) + 1, a(0) = 1, a(1) = 3.
> — [OEIS A001056](https://oeis.org/A001056)

Offset 0: 1, 3, 4, 13, 53, 690, 36571, 25233991, 922832284862, …

### Python 3 — 35 bytes

```python
a,b=1,3
while[print(a)]:a,b=b,a*b+1
```

**How it works**

- `a` and `b` hold a(n) and a(n+1), starting from a(0) = 1 and a(1) = 3.
- `a,b=b,a*b+1` moves one step: the new pair is a(n+1) and
  a(n+1)·a(n) + 1 = a(n+2). Exact integer arithmetic.
- `print(a)` in the loop condition returns `None`, and `[None]` is a
  non-empty list, so the loop never ends.

**Notes**

- Starting one step earlier, from a(−1) = 2 (3 = 1·2 + 1), saves nothing.
- The product is symmetric, so a walrus can do the shift inside it:
  `b*(b:=a)` multiplies the old `b` by `a` and leaves the old `a` in `b`.
  `a=2;b=0` / `while 1:print(a:=b*(b:=a)+1)` is correct but 36 bytes.
- a(n) ~ c^(φⁿ) with c ≈ 1.7979: a(17) has 910 digits, a(20) 3854 and a(21)
  6236. The program prints a(0) to a(20) and then stops on Python's
  4300-digit int-to-str limit (a `ValueError` on stderr), an interpreter
  limit, not a failure.
- The b-file has 18 terms (a(0) to a(17)); the bar is the whole b-file in
  60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 35 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001056), CC BY-SA 4.0.
