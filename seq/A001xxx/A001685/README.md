# A001685

> a(0) = 1, a(1) = 2, a(2) = 3; for n >= 3, a(n) = a(n-2) + a(n-1)*Product_{i=1..n-3} a(i).
> — [OEIS A001685](https://oeis.org/A001685)

Offset 0: 1, 2, 3, 5, 13, 83, 2503, 976253, 31601312113, 2560404986164794683, …

### Python 3 — 41 bytes

```python
a=b=c=1
while[print(b)]:a,b,c=b,c*b+a,c*a
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
- **The definition is that recurrence.** Here a(n) = a(n−2) +
  a(n−1)·Π_(i=1..n−3) a(i), and since a(0) = 1 the product is
  Π_(k=0..n−3) a(k) = c_n. So a(n) = c_n·a(n−1) + a(n−2) = p_n for n ≥ 3,
  and the seeds agree too: p_0 = 1, p_1 = 1·1 + 1 = 2, p_2 = 1·2 + 1 = 3.
- **The loop** keeps a = p_(n−2), b = p_(n−1) and c = c_n. One step makes
  b → c·b + a = p_n, and c → c·a, because c_(n+1) = c_n·p_(n−2): the
  product takes in one more factor. For n = 1, 2 that factor is
  p_(−1) = p_0 = 1, matching c_1 = c_2 = c_3 = 1.
- It starts at n = 1 with a = p_(−1) = 1, b = p_0 = 1, c = c_1 = 1, so a
  single `a=b=c=1` seeds everything, and the header prints b before
  each step.

**Notes**

- Exact integers, so the program is right for every n. The terms grow
  like C^(dⁿ) with d ≈ 1.7549 (d(d−1)² = 1, Kotesovec in the entry):
  a(18) has 2907 digits, and a(19) is over Python's 4300-digit limit for
  printing ints, where the program stops with a ValueError.
- The b-file (17 terms) prints at once; the bar is the whole b-file in
  60 s.
- Kotesovec's form a(n) = a(n−2) + a(n−1)a(n−3)(a(n−1)−a(n−3))/a(n−2)
  needs no product but three back terms and a division, and comes out
  longer.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-14 | Python 3 | 41 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001685), CC BY-SA 4.0.
