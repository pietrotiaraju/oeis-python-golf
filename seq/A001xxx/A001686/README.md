# A001686

> From a continued fraction.
> — [OEIS A001686](https://oeis.org/A001686)

Offset 0: 1, 1, 2, 3, 8, 51, 1538, 599871, 19417825808, 1573273218577214751, …

### Python 3 — 59 bytes

```python
a=b=c=v=1;u=0
while[print(v)]:a,b,c,u,v=b,c*b+a,c*a,v,c*v+u
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
- **The loop** is the one of [A001685](../A001685/) (a = p_(n−2),
  b = p_(n−1), c = c_n; b → c·b + a and c → c·a, the product taking in
  p_(n−2)), with the denominators riding along: u = q_(n−2), v = q_(n−1),
  and v → c·v + u. The numerators cannot be dropped, since the partial
  quotients are built from them.
- It starts at n = 1: a = p_(−1) = 1, b = p_0 = 1, c = c_1 = 1, u = q_(−1) = 0,
  v = q_0 = 1, and the header prints v = q_n before each step. Check:
  q_2 = 1·1 + 1 = 2, q_3 = 1·2 + 1 = 3, q_4 = 2·3 + 2 = 8,
  q_5 = 6·8 + 3 = 51.

**Notes**

- Exact integers, so the program is right for every n. a(18) has 2907
  digits; a(19) is over Python's 4300-digit limit for printing ints, where
  the program stops with a ValueError.
- The b-file holds the 12 terms of the entry, which print at once; the bar
  is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-14 | Python 3 | 59 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001686), CC BY-SA 4.0.
