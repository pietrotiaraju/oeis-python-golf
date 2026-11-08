# A001036

> Partial sums of A001037, omitting A001037(1).
> — [OEIS A001036](https://oeis.org/A001036)

Offset 1: 1, 2, 4, 7, 13, 22, 40, 70, 126, 225, 411, 746, 1376, 2537, 4719, 8799, …

### Python 3 — 90 bytes

```python
g=lambda n:2**n-sum(g(d)for d in range(1,n)if n%d<1)
s=n=1
while[print(s)]:n+=1;s+=g(n)//n
```

**How it works**

- L(n) = [A001037](../A001037/)(n) counts binary Lyndon words. Each binary
  word of length n is, in exactly one way, a power of a primitive word of
  length d | n, and the d rotations of a Lyndon word are the primitive
  words of its class; so Σ_{d|n} d·L(d) = 2ⁿ.
- `g(n)` = n·L(n) = 2ⁿ − Σ g(d) over the proper divisors d: Möbius
  inversion by subtraction, with no μ.
- a(n) = L(0) + L(2) + … + L(n) (L(1) = 2 is left out), so the running sum
  starts at a(1) = L(0) = 1 and adds g(n)/n.

**Notes**

- Exact integer arithmetic.
- The recursion is not memoized; it visits each chain of divisors of n
  once, which is cheap. The b-file is synthesized from the 34 terms of
  the entry; they print at once, and the bar is the whole b-file.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 90 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001036), CC BY-SA 4.0.
