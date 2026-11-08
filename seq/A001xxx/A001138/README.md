# A001138

> Number of red rooted red-black trees with n internal nodes.
> — [OEIS A001138](https://oeis.org/A001138)

Offset 1: 1, 0, 1, 4, 6, 4, 2, 8, 32, 96, 256, 608, 1268, 2392, 4177, 6720, 9976, 14064, …

### Python 3 — 82 bytes

```python
n=1
while 1:n+=1;s=B=X=3**n;exec('s+=B*B;B=(B+B*B)**2%X**-~n;'*n);print(s//X**n%X)
```

**How it works**

- A red root has two black children of the same black height, so with
  B_h(x) the black-rooted trees of black height h counted by leaves
  (B₀ = x, B_{h+1} = (B_h + B_h²)², see [A001137](../A001137/)),
  a(n) = [x^(n+1)] Σ_{h≥0} B_h² (n internal nodes = n + 1 leaves). The
  black-rooted sibling is [A001137](../A001137/), and
  [A001131](../A001131/)(n+1) = A001137(n) + a(n).
- The program is the A001137 one with x = X = 3^m, m = n + 1 leaves (`n` in
  the code), arithmetic mod X^(m+1), and the same proof that every
  coefficient in play is a tree count below X. Each round adds B_h² to the
  sum and then steps B to B_{h+1}, reduced.
- `s+=B*B` adds B_h² without reducing it, so `s` has junk above x^m; the
  digits up to x^m are still exact (carries only go upward), and the print
  takes digit m with `s//X**n%X`. That is 2 bytes cheaper than a second
  `%X**-~n` in the round. Starting with `s=X` only touches the digit of x¹.

**Notes**

- Keeping B_h² in a walrus (`B=(B+(D:=B*B))**2%…;s+=D`) or reducing the sum
  as well both come out longer.
- 277 terms in 60 s here; each term starts again from scratch with numbers
  of about 1.6·m² bits.
- The b-file has 35 terms (a(1) to a(35), synthesized from the entry); the
  bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 82 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001138), CC BY-SA 4.0.
