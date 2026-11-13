# A001629

> Self-convolution of Fibonacci numbers.
> — [OEIS A001629](https://oeis.org/A001629)

Offset 0: 0, 0, 1, 2, 5, 10, 20, 38, 71, 130, 235, 420, 744, 1308, 2285, …

### Python 3 — 49 bytes

```python
p=q=f=0;g=1
while[print(p)]:p,q,f,g=q,p+q+g,g,f+g
```

**How it works**

- a(n) = Σ F(k)F(n−k), with generating function x²/(1 − x − x²)². Times
  (1 − x − x²) it is x·(x/(1 − x − x²)), the Fibonacci generating function
  shifted once, so a(n) = a(n−1) + a(n−2) + F(n−1) (a(n) = 0 for n < 0).
- `p`, `q` hold a(n), a(n+1) and `f`, `g` hold F(n), F(n+1): one
  simultaneous assignment moves both windows, a(n+2) = q + p + F(n+1)
  and the Fibonacci pair steps as usual. The start is a(0) = a(1) = 0,
  F(0) = 0, F(1) = 1.

**Notes**

- The closed form a(n) = (n·L(n) − F(n))/5 with a Fibonacci pair and a
  counter is 55 bytes; the order-4 linear recurrence on a list is longer
  still. The second-order recurrence (n−2)a(n) = (n−1)a(n−1) + n·a(n−2)
  that does it for [A001628](../A001628/) cannot start here: it says
  nothing at n = 2, where the first nonzero term appears.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 501 terms (n = 0 to 500); the bar is the whole b-file in
  60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 49 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001629), CC BY-SA 4.0.
