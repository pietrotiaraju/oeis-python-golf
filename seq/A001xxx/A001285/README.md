# A001285

> Thue-Morse sequence: let A_k denote the first 2^k terms; then A_0 = 1 and for k >= 0, A_{k+1} = A_k B_k, where B_k is obtained from A_k by interchanging 1's and 2's.
> — [OEIS A001285](https://oeis.org/A001285)

Offset 0: 1, 2, 2, 1, 2, 1, 1, 2, 2, 1, 1, 2, 1, 2, 2, 1, …

### Python 3 — 40 bytes

```python
n=0
while[print(n.bit_count()%2+1)]:n+=1
```

**How it works**

- a(n) = 1 + (number of 1 bits of n) mod 2. By the definition, for
  2^k ≤ n < 2^(k+1) the term a(n) is a(n − 2^k) with 1 and 2 interchanged
  (it lies in B_k, the copy of A_k). Removing the top bit of n lowers its
  number of 1 bits by one, so by induction on n (from a(0) = 1, zero 1 bits)
  a(n) is 1 when n has an even number of 1 bits and 2 when it is odd.
- `n.bit_count()` (Python 3.10+) counts the 1 bits exactly, for every n.
- `print` returns `None` and `[None]` is a non-empty list, so the loop
  never ends.

**Notes**

- Expanding the morphism 1 → 12, 2 → 21 in a growing list, `print(1);s=[2]`
  and `for x in s:print(x);s+=x,3-x`, is 43 bytes (a(0) needs its own
  print, because the image of a(0) is a(0), a(1) themselves).
  `bin(n).count('1')` is 4 bytes longer than `n.bit_count()`.
- The b-file has 10001 terms (n = 0 to 10000); the bar is the whole b-file
  in 60 s, which takes about 0.2 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 40 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001285), CC BY-SA 4.0.
