# A001444

> Bending a piece of wire of length n+1 (configurations that can only be brought into coincidence by turning the figure over are counted as different).
> — [OEIS A001444](https://oeis.org/A001444)

Offset 0: 1, 2, 6, 15, 45, 126, 378, 1107, 3321, 9882, 29646, 88695, 266085, 797526, …

### Python 3 — 38 bytes

```python
p=q=1
while[print(p*q+q>>1)]:p,q=3*q,p
```

**How it works**

- a(n) = (b^n + b^⌊n/2⌋)/2 with b = 3 (the entry's formula: a wire with n bends, each to the
  left, to the right or none, counted up to reversal of the wire). Write p = b^⌈n/2⌉ and
  q = b^⌊n/2⌋: then b^n = pq, and a(n) = (pq + q)/2, `p*q+q>>1` (the sum is
  even: p and q are odd).
- Going from n to n + 1, ⌈(n+1)/2⌉ = ⌊n/2⌋ + 1 and ⌊(n+1)/2⌋ = ⌈n/2⌉, so
  the pair steps as `p,q=3*q,p`. `p=q=1` is n = 0, the offset.
- Exact integer arithmetic, so the program is right for every n.

**Notes**

- The direct `n=0` / `while[print(3**n+3**(n>>1)>>1)]:n+=1` is 40 bytes;
  the swap saves 2. The same 38-byte program, with other constants, does
  [A001445](../A001445/), [A001446](../A001446/), [A001447](../A001447/).
- The b-file has 1001 terms (n = 0 to 1000); the bar is the whole b-file
  in 60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 38 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001444), CC BY-SA 4.0.
