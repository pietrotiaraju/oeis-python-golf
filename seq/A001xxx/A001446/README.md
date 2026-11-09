# A001446

> a(n) = (4^n + 4^[n/2])/2.
> — [OEIS A001446](https://oeis.org/A001446)

Offset 2: 10, 34, 136, 520, 2080, 8224, 32896, 131200, 524800, 2097664, 8390656, …

### Python 3 — 38 bytes

```python
p=q=4
while[print(p*q+q>>1)]:p,q=4*q,p
```

**How it works**

- a(n) = (b^n + b^⌊n/2⌋)/2 with b = 4. Write p = b^⌈n/2⌉ and
  q = b^⌊n/2⌋: then b^n = pq, and a(n) = (pq + q)/2, `p*q+q>>1` (the sum is
  even: q ≥ 4 is even from n = 2 on).
- Going from n to n + 1, ⌈(n+1)/2⌉ = ⌊n/2⌋ + 1 and ⌊(n+1)/2⌋ = ⌈n/2⌉, so
  the pair steps as `p,q=4*q,p`. `p=q=4` is n = 2, the offset.
- Exact integer arithmetic, so the program is right for every n.

**Notes**

- The direct `n=2` / `while[print(4**n+4**(n>>1)>>1)]:n+=1` is 40 bytes;
  the swap saves 2. The same 38-byte program, with other constants, does
  [A001444](../A001444/), [A001445](../A001445/), [A001447](../A001447/).
- The b-file has 1000 terms (n = 2 to 1001); the bar is the whole b-file
  in 60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 38 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001446), CC BY-SA 4.0.
