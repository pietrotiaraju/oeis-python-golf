# A001907

> Expansion of e.g.f. exp(-x)/(1-4*x).
> — [OEIS A001907](https://oeis.org/A001907)

Offset 0: 1, 3, 25, 299, 4785, 95699, 2296777, 64309755, 2057912161, 74084837795, …

### Python 3 — 38 bytes

```python
b=n=0
while[print(abs(b:=1-b*n))]:n+=4
```

**How it works**

- **Recurrence.** exp(−x)/(1 − 4x) is exp(−x) times Σ 4ⁿxⁿ, so
  a(n) = n!·4ⁿ·Σⱼ₌₀ⁿ (−1/4)ʲ/j!, and the last term of that sum gives
  a(n) = 4n·a(n − 1) + (−1)ⁿ, a(0) = 1.
- **No signs.** b(n) = (−1)ⁿ·a(n) satisfies b(n) = 1 − 4n·b(n − 1). The loop
  variable `n` holds 4n, `b:=1-b*n` makes b(n), and `abs` prints a(n).
- The parity trick of [A000180](../../A000xxx/A000180/) (k = 3) and
  [A001908](../A001908/) (k = 5), `a*n^1`, needs 4n·a(n − 1) to be odd for odd
  n, which never happens here.

**Notes**

- Since 4n·a(n − 1) ≡ 4n (mod 8) (a(n) is odd), `a=a*n+1-n%8//2` is a correct
  sign-free alternative, 2 bytes longer.
- Exact integer arithmetic, so the program is right for every n; it stops at
  the 4300-digit int-to-str limit of Python 3.11+, first passed by a(1309).
- The b-file has 351 terms (n = 0 to 350); the bar is the whole b-file in
  60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-18 | Python 3 | 38 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001907), CC BY-SA 4.0.
