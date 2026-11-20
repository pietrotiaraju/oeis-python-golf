# A002119

> Bessel polynomial y_n(-2).
> — [OEIS A002119](https://oeis.org/A002119)

Offset 0: 1, -1, 7, -71, 1001, -18089, 398959, -10391023, 312129649, …

### Python 3 — 42 bytes

```python
a=b=n=1
while[print(a)]:a,b=b-2*n*a,a;n+=2
```

**How it works**

- **Recurrence.** The Bessel polynomials y_n(x) = Σ_k (n+k)!/((n−k)!·k!)·(x/2)^k
  satisfy the classical three-term recurrence
  y_(n+1)(x) = (2n+1)·x·y_n(x) + y_(n−1)(x), with y_0 = 1 and y_1 = 1 + x.
  At x = −2 this is a(n+1) = −2(2n+1)·a(n) + a(n−1), the D-finite
  recurrence in the entry.
- **Start.** The recurrence also gives y_1 from y_0 if y_(−1) = 1
  (Bessel polynomials have y_(−n−1) = y_n, the entry's a(−n−1) = a(n)), so
  the state starts at a = y_0 = 1, b = y_(−1) = 1.
- **Loop.** `n` holds the odd factor 2k+1 (1, 3, 5, …, `n+=2`), and
  `a,b=b-2*n*a,a` steps (y_k, y_(k−1)) to (y_(k+1), y_k). The `while`
  header prints the current a before each step.

**Notes**

- The absolute values are the denominators of the convergents of
  e = 1 + 2/(1 + 1/(6 + 1/(10 + …))) (comment in the entry); the signs
  alternate.
- a(n) has about 0.6·n·log₁₀ n digits; the b-file has 101 terms
  (n = 0 to 100), and the bar is the whole b-file in 60 s, which takes a
  fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-20 | Python 3 | 42 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002119), CC BY-SA 4.0.
