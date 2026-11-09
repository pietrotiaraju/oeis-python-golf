# A001445

> a(n) = (2^n + 2^[ n/2 ] )/2.
> — [OEIS A001445](https://oeis.org/A001445)

Offset 2: 3, 5, 10, 18, 36, 68, 136, 264, 528, 1040, 2080, 4128, 8256, 16448, 32896, …

### Python 3 — 38 bytes

```python
p=q=2
while[print(p*q+q>>1)]:p,q=2*q,p
```

**How it works**

- a(n) = (b^n + b^⌊n/2⌋)/2 with b = 2. Write p = b^⌈n/2⌉ and
  q = b^⌊n/2⌋: then b^n = pq, and a(n) = (pq + q)/2, `p*q+q>>1` (the sum is
  even: q ≥ 2 is even from n = 2 on).
- Going from n to n + 1, ⌈(n+1)/2⌉ = ⌊n/2⌋ + 1 and ⌊(n+1)/2⌋ = ⌈n/2⌉, so
  the pair steps as `p,q=2*q,p`. `p=q=2` is n = 2, the offset.
- Exact integer arithmetic, so the program is right for every n.

**Notes**

- The direct `n=2` / `while[print(2**n+2**(n>>1)>>1)]:n+=1` is 40 bytes;
  the swap saves 2. The same 38-byte program, with other constants, does
  [A001444](../A001444/), [A001446](../A001446/), [A001447](../A001447/).
- The b-file has 1000 terms (n = 2 to 1001); the bar is the whole b-file
  in 60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 38 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001445), CC BY-SA 4.0.
