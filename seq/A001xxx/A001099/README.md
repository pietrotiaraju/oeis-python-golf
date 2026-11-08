# A001099

> a(n) = n^n - a(n-1), with a(1) = 1.
> — [OEIS A001099](https://oeis.org/A001099)

Offset 1: 1, 3, 24, 232, 2893, 43763, 779780, 15997436, 371423053, 9628576947, …

### Python 3 — 35 bytes

```python
a=n=0
while 1:n+=1;print(a:=n**n-a)
```

**How it works**

- With the virtual start a(0) = 0, the recurrence a(n) = nⁿ − a(n−1)
  gives a(1) = 1 − 0 = 1 as the OEIS sets it, so the loop needs no special
  first case: `n` counts 1, 2, 3, … and `a:=n**n-a` is the new term,
  printed through the walrus.
- Unrolled, a(n) = nⁿ − (n−1)ⁿ⁻¹ + … ± 1¹, the alternating sum in the OEIS
  formula section. Exact integers.

**Notes**

- `a=0;n=1` with `while[print(a:=n**n-a)]:n+=1` is 36 bytes. Starting that
  loop from n = 0 does not work, although 0**0 = 1 in Python: it prints
  1, then 1¹ − 1 = 0.
- nⁿ has about n·log₁₀ n digits: Python's 4300-digit int-to-str limit stops
  the program at a(1371), the first term with 4301 digits, after printing
  a(1) to a(1370).
- The b-file has 100 terms (a(1) to a(100), 200 digits); the whole of it
  prints instantly, and the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 35 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001099), CC BY-SA 4.0.
