# A001949

> Solutions of a fifth-order probability difference equation.
> — [OEIS A001949](https://oeis.org/A001949)

Offset 0: 0, 0, 0, 0, 0, 1, 2, 4, 8, 16, 32, 63, 124, 244, 480, 944, 1856, 3649, 7174, …

### Python 3 — 41 bytes

```python
l=[0]*5
while 1:a,*l=*l,sum(l,1);print(a)
```

**How it works**

- **Definition.** The name only says "solutions of a fifth-order
  probability difference equation" (Dunkel, 1925). The entry pins it down
  with the generating function x⁵/((1 − x)(1 − x − x² − x³ − x⁴ − x⁵)), and
  Petros Hadjicostas's formula from Dunkel's Eq. (4): a(n) = 1 + a(n − 1) +
  … + a(n − 5) for n ≥ 5, with a(0) = … = a(4) = 0. They agree: multiplying
  the series by 1 − x − … − x⁵ leaves x⁵/(1 − x), that is,
  a(n) − a(n − 1) − … − a(n − 5) is 1 for n ≥ 5 and 0 below (with zeros for
  n < 0). All 1001 terms of the b-file agree with it.
- **Program.** `l` is the window a(n), …, a(n + 4), starting with five
  zeros. `sum(l,1)` is 1 + a(n) + … + a(n + 4) = a(n + 5), and
  `a,*l=*l,…` pops a(n) into `a` and shifts the new term in (the window
  trick of [A000322](../../A000xxx/A000322/)); then a(n) is printed.
- Exact integer arithmetic, so the program is right for every n.

**Notes**

- The list form `for x in l:print(x);l+=sum(l[-5:],1),` is 44 bytes; the
  order-6 form a(n + 1) = 2a(n) − a(n − 5) from a(−1) = −1 is 50.
- The b-file has 1001 terms (n = 0 to 1000); the bar is the whole b-file in
  60 s, which prints instantly.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 41 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001949), CC BY-SA 4.0.
