# A000392

> Stirling numbers of second kind S(n,3).
> — [OEIS A000392](https://oeis.org/A000392)

Offset 0: 0, 0, 0, 1, 6, 25, 90, 301, 966, 3025, 9330, 28501, 86526, …

### Python 3 — 38 bytes

```python
a=e=0
while[print(a)]:a=3*a+e//2;e-=~e
```

**How it works**

- The triangle recurrence S(n+1, 3) = 3·S(n, 3) + S(n, 2) (the new ball
  joins one of the 3 boxes, or opens the third box) drives `a`, and
  S(n, 2) = 2ⁿ⁻¹ − 1 for n ≥ 1 is ⌊e/2⌋ with e = 2ⁿ − 1.
- `e-=~e` is e − (−e − 1) = 2e + 1, so e runs through 0, 1, 3, 7, … = 2ⁿ − 1
  from `e=0`. At n = 0 the closed form 2ⁿ⁻¹ − 1 would be −½, but S(0, 2) = 0,
  and the floor gives exactly that: ⌊0/2⌋ = 0. For n ≥ 1, e is odd and
  ⌊e/2⌋ = 2ⁿ⁻¹ − 1. So `a=3*a+e//2` turns S(n, 3) into S(n+1, 3) for every
  n ≥ 0, starting from S(0, 3) = 0.
- The loop prints a before each step, so the output starts at a(0).

**Notes**

- Exact integer arithmetic, correct for every n; only the 4300-digit
  int-to-str limit of Python 3.11+ stops it, after 9015 terms (about 1 s
  here). The b-file has 201 terms (up to a(200)); the bar is the whole
  b-file in 60 s.
- Also 38 bytes: `a=0;e=1` / `while[print(a)]:a+=a+e//6;e*=3`, from
  S(n+1, 3) = 2·S(n, 3) + ⌊3ⁿ/6⌋. That is the recurrence above, because
  S(n, 3) + S(n, 2) = (3ⁿ − 3)/6 for n ≥ 1 by the closed forms, which is
  ⌊3ⁿ/6⌋ since 3ⁿ ≡ 3 (mod 6), and at n = 0 both sides are 0.
- A search over two-variable loops of this shape (23 updates for a, 17 for
  e, both orders, 14 print expressions, start values −3 to 3) found nothing
  under 38 bytes. Without the floor the recurrence would need a third
  state: S(n, 3) has no closed form α3ⁿ + β2ⁿ + γ valid at n = 0
  (it would give 1/6 there).
- The previous record (40 bytes) used the closed form,
  `n=0` / `while[print(3**n//6-~-2**n//2)]:n+=1`: by inclusion–exclusion
  S(n, 3) = (3ⁿ − 3·2ⁿ + 3 − 0ⁿ)/6, `3**n//6` is (3ⁿ⁻¹ − 1)/2 and `~-2**n//2`
  is 2ⁿ⁻¹ − 1 for n ≥ 1, and both floors are 0 at n = 0. The plain
  `(3**n-3*2**n+3)//6` is a byte longer, and keeping 3ⁿ and 2ⁿ in variables,
  `t=b=1` / `while[print(t//6-~-b//2)]:t*=3;b*=2`, is 41 bytes.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 40 | first entry |
| 2026-11-07 | Python 3 | 38 | S(n+1,3) = 3S(n,3) + ⌊e/2⌋ with e = 2ⁿ − 1 stepped by `e-=~e` |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000392), CC BY-SA 4.0.
