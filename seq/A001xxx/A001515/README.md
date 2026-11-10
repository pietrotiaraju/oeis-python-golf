# A001515

> Bessel polynomial y_n(x) evaluated at x=1.
> — [OEIS A001515](https://oeis.org/A001515)

Offset 0: 1, 2, 7, 37, 266, 2431, 27007, 353522, 5329837, 90960751, …

### Python 3 — 40 bytes

```python
a=b=k=1
while[print(b)]:a,b=b,k*b+a;k+=2
```

**How it works**

- The Bessel polynomials y_n(x) = Σ (n+k)!/(2^k·k!·(n−k)!)·x^k (the rows
  of [A001498](../A001498/)) satisfy the three-term recurrence
  **y_n(x) = (2n−1)·x·y_{n−1}(x) + y_{n−2}(x)**, with y_0 = 1 and
  y_1 = 1 + x (Krall and Frink, 1949; Grosswald, *Bessel Polynomials*,
  1978). At x = 1 this is a(n) = (2n−1)·a(n−1) + a(n−2).
- Run backwards from n = 1, the recurrence gives y_{−1} = y_1 − x·y_0 = 1,
  so the pair (a, b) = (y_{−1}, y_0) = (1, 1) starts the loop and the first
  step needs no special case. `k` is the odd multiplier 2n−1 of the next
  step, so it starts at 1 too: `a=b=k=1`.
- `while[print(b)]:` prints in the loop condition (`[None]` is true), then
  `a,b=b,k*b+a;k+=2` moves one step.

**Notes**

- Exact integer arithmetic, so the program is right for every n; the first
  term over the 4300-digit int-to-str limit is a(1424).
- The b-file has 405 terms (n = 0 to 404); they all print in well under a
  second, and the bar is the whole b-file in 60 s.
- The same loop with another starting multiplier and step gives y_n(2)
  ([A001517](../A001517/)) and y_n(3) ([A001518](../A001518/)); the
  derivatives at 1 are [A001514](../A001514/) and [A001516](../A001516/).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-10 | Python 3 | 40 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001515), CC BY-SA 4.0.
