# A002249

> a(n) = a(n-1) - 2*a(n-2) with a(0) = 2, a(1) = 1.
> — [OEIS A002249](https://oeis.org/A002249)

Offset 0: 2, 1, -3, -5, 1, 11, 9, -13, -31, -5, 57, 67, -47, -181, -87, 275, …

### Python 3 — 35 bytes

```python
a,b=2,1
while[print(a)]:a,b=b,b-2*a
```

**How it works**

- The recurrence as given: (a, b) holds two consecutive terms and
  `a,b=b,b-2*a` moves the pair one place. This is the Lucas sequence
  Vₙ(1, 2) = αⁿ + βⁿ with α, β = (1 ± √−7)/2, the roots of x² − x + 2.
- `print` returns `None` and `[None]` is a non-empty list, so the loop
  never ends. Exact integers, so it is right for every n.

**Notes**

- A walrus step does not help here: b's new value needs the old a, so
  `b-=…(a:=b)…` has to hide the assignment in a term worth zero, which
  costs more than the tuple swap.
- |a(n)| ≤ 2·2ⁿᐟ², so the terms reach the 4300-digit int-to-str limit of
  Python 3.11+ only at n = 28568, where the program stops with a
  `ValueError`.
- [A002248](../A002248/) counts the points of an elliptic curve over
  GF(2ⁿ) as 2ⁿ + 1 − a(n).
- The b-file has 501 terms (n = 0 to 500); the bar is the whole b-file in
  60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-23 | Python 3 | 35 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002249), CC BY-SA 4.0.
