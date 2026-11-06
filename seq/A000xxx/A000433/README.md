# A000433

> n written in base where place values are positive cubes.
> — [OEIS A000433](https://oeis.org/A000433)

Offset 0: 0, 1, 2, 3, 4, 5, 6, 7, 10, 11, …

### Python 3 — 114 bytes

```python
n=0
while 1:
 r=n;s='';k=1
 while k**3<=n:k+=1
 while k>1:
  k-=1;d,r=divmod(r,k**3);s+=str(d)
 print(s or 0);n+=1
```

**How it works**

- The place values are 1³, 2³, 3³, … . A representation is chosen
  greedily from the largest available cube downward; this is not
  ordinary positional notation with powers of a fixed base.
- The first loop leaves k one above the largest cube root needed.
  The second decrements k before use and computes
  `d,r=divmod(r,k**3)`: d is the next digit and r the remainder
  to represent using the smaller cubes.
- Immediately before the k³ place, r<(k+1)³. Its digit is at
  most ⌊((k+1)³−1)/k³⌋, which is at most 7 for k≥1.
  Thus each quotient is a single decimal digit, and `s+=str(d)`
  records the intended notation without separators.
- For n=9, the 8 and 1 places give digits 1 and 1, hence 11;
  for n=27, the 27, 8 and 1 places give 100. Intermediate zero
  digits must be retained.
- At n=0 no place is visited and s stays empty. `s or 0` prints
  the required zero while avoiding a leading empty output line.

**Notes**

- Exact integer divisions; no approximate cube root is needed. The
  representation is deterministic because the page uses the greedy
  convention, even though unrestricted cube-place expansions need
  not be unique.
- Both loops visit O(n^(1/3)) place indices per output. The printed
  representation is held as a string, so the digit sequence is never
  parsed as a potentially huge decimal integer.
- Compare [A000462](../A000462/), the same descending-division
  method with triangular numbers as place values.
- The b-file has 10001 terms (indices 0 through 10000). The bar is the
  whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 114 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000433), CC BY-SA 4.0.
