# A001514

> Bessel polynomial {y_n}'(1).
> — [OEIS A001514](https://oeis.org/A001514)

Offset 0: 0, 1, 9, 81, 835, 9990, 137466, 2148139, 37662381, 733015845, …

### Python 3 — 49 bytes

```python
a=b=k=1
while[print(k//2*b-b+a)]:a,b=b,k*b+a;k+=2
```

**How it works**

- The Bessel polynomials obey **x²·y_n′(x) = (nx − 1)·y_n(x) + y_{n−1}(x)**.
  With c(n,k) = (n+k)!/(2^k·k!·(n−k)!) the coefficient of x^k in y_n
  ([A001498](../A001498/)), the coefficient of x^(k+1) on the right is
  n·c(n,k) − c(n,k+1) + c(n−1,k+1), and
  c(n,k+1) − c(n−1,k+1) = (n+k)!·((n+k+1) − (n−k−1))/(2^(k+1)·(k+1)!·(n−k−1)!)
  = (n−k)·c(n,k), so it equals k·c(n,k), the coefficient on the left; the
  constant terms are −1 + 1 = 0. At x = 1:
  **a(n) = (n−1)·y_n(1) + y_{n−1}(1)**.
- y_n(1) is [A001515](../A001515/), run by the same loop:
  y_n = (2n−1)·y_{n−1} + y_{n−2} from (y_{−1}, y_0) = (1, 1), where
  y_{−1} = 1 is the value the recurrence gives backwards (it also makes the
  identity hold at n = 0: 0 = −1 + 1).
- When term n is printed, `b` = y_n(1), `a` = y_{n−1}(1) and `k` = 2n+1, so
  `k//2` = n and `k//2*b-b+a` = (n−1)·y_n + y_{n−1}.

**Notes**

- Keeping k = 2n−1 instead (printing `k//2*b+a`) needs `a=b=1;k=-1` and
  a step before the print: one byte more. Carrying y′ as a second pair
  through the differentiated recurrence y_n′ = (2n−1)(y_{n−1} + y_{n−1}′) +
  y_{n−2}′ is 62 bytes.
- Exact integer arithmetic, so the program is right for every n; the first
  term over the 4300-digit int-to-str limit is a(1423).
- The b-file has 401 terms (n = 0 to 400); they all print in well under a
  second, and the bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-10 | Python 3 | 49 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001514), CC BY-SA 4.0.
