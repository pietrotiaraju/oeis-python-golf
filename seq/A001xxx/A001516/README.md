# A001516

> Bessel polynomial {y_n}''(1).
> — [OEIS A001516](https://oeis.org/A001516)

Offset 0: 0, 0, 6, 120, 1980, 32970, 584430, 11204676, 233098740, 5254404210, …

### Python 3 — 59 bytes

```python
a=b=k=1
while[print((k*k//4-2*k+6)*b-4*a)]:a,b=b,k*b+a;k+=2
```

**How it works**

- From the identity x²·y_n′ = (nx − 1)·y_n + y_{n−1} (proved from the
  coefficients on the [A001514](../A001514/) page) one gets, at x = 1,
  y_n′(1) = (n−1)·y_n + y_{n−1}, and differentiating it once more,
  2y_n′ + y_n″ = n·y_n + (n−1)·y_n′ + y_{n−1}′ at x = 1. Using
  y_{n−1}′ = (n−2)·y_{n−1} + y_{n−2} and y_{n−2} = y_n − (2n−1)·y_{n−1}
  (the three-term recurrence of the Bessel polynomials) everything
  collapses to
  **a(n) = (n² − 3n + 4)·y_n(1) − 4·y_{n−1}(1)**,
  with y = [A001515](../A001515/). It also holds at n = 0 and 1 with
  y_{−1} = 1 (0 = 4 − 4 and 0 = 2·2 − 4).
- The loop is the one of A001515: `b` = y_n(1), `a` = y_{n−1}(1), and
  `k` = 2n+1 when term n is printed. Then `k*k//4` = n² + n (k is odd),
  so `k*k//4-2*k+6` = n² − 3n + 4.

**Notes**

- `((k-4)**2+7)//4` and `(k*k-8*k+23)//4` are the same polynomial and one
  byte longer; keeping k = 2n−1 makes it `k*k//4-k+3` but costs three bytes
  at the start.
- Exact integer arithmetic, so the program is right for every n; the first
  term over the 4300-digit int-to-str limit is a(1422).
- The b-file has 401 terms (n = 0 to 400); they all print in well under a
  second, and the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-10 | Python 3 | 59 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001516), CC BY-SA 4.0.
