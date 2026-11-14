# A001684

> From a continued fraction.
> — [OEIS A001684](https://oeis.org/A001684)

Offset 0: 1, 1, 1, 1, 2, 6, 30, 390, 32370, 81022110, 79098077953830, …

### Python 3 — 48 bytes

```python
a=0;b=c=1
while[print(c)]:a,b,c=b,c*b+a,c*a or c
```

**How it works**

- **One continued fraction, three sequences.** [A001684](../A001684/)
  lists the partial quotients c_n of a continued fraction
  [c_0; c_1, c_2, …], [A001685](../A001685/) the numerators p_n and
  [A001686](../A001686/) the denominators q_n of its convergents
  p_n/q_n. The partial quotients are made from the numerators:
  c_0 = c_1 = c_2 = 1 and c_n = p_0·p_1⋯p_(n−3) for n ≥ 3 (Irvine's
  formulas in the entries). The convergents follow the usual recurrence
  p_n = c_n·p_(n−1) + p_(n−2), q_n = c_n·q_(n−1) + q_(n−2), from
  p_(−2) = 0, p_(−1) = 1 and q_(−2) = 1, q_(−1) = 0.
- **The loop** is the one of [A001685](../A001685/): a = p_(n−2),
  b = p_(n−1), c = c_n, and a step makes b → c·b + a = p_n and
  c → c·a = c_(n+1) (the product c_n = p_0⋯p_(n−3) takes in one more
  factor, p_(n−2)). Here it prints c.
- **Starting one step earlier.** To print c_0 too, it starts at n = 0 with
  the standard seeds a = p_(−2) = 0, b = p_(−1) = 1, c = c_0 = 1. The first
  step gives p_0 = 1·1 + 0 = 1 as it should, but the product rule would
  give c_1 = c_0·p_(−2) = 0; `c*a or c` keeps c when c·a is 0. That
  happens only at this step, since every p_k with k ≥ −1 is at least 1.
  After it the state is a = b = c = 1, the state A001685 starts from
  (2 B under printing a(0) separately with `print(1)`).

**Notes**

- Exact integers, so the program is right for every n. a(20) has 3850
  digits; a(21) is over Python's 4300-digit limit for printing ints, where
  the program stops with a ValueError.
- The b-file (18 terms) prints at once; the bar is the whole b-file in
  60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-14 | Python 3 | 48 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001684), CC BY-SA 4.0.
