# A001614

> Connell sequence: 1 odd, 2 even, 3 odd, ...
> — [OEIS A001614](https://oeis.org/A001614)

Offset 1: 1, 2, 4, 5, 7, 9, 10, 12, 14, 16, 17, 19, 21, 23, 25, 26, 28, 30, …

### Python 3 — 40 bytes

```python
m=k=0
while 1:m+=2;k+=m>k*k+k;print(m-k)
```

**How it works**

- The sequence comes in blocks: block k has k terms with the parity of k,
  1 | 2, 4 | 5, 7, 9 | 10, 12, 14, 16 | …. The step is 2 inside a block and 1
  into the next one, so a(n) = 2n − k, where k is the block of n: the k with
  k(k − 1)/2 < n ≤ k(k + 1)/2 ([A002024](https://oeis.org/A002024)). Block k
  ends at 2·k(k + 1)/2 − k = k².
- `m` holds 2n and steps by 2. Block k is over once 2n > k(k + 1), so
  `k+=m>k*k+k` moves k on at the first n of each block (blocks are never
  empty, so one step at a time is enough), and `m-k` is the term.
- From m = k = 0 the first pass makes m = 2, k = 1 and prints a(1) = 1, so
  the offset 1 needs no special start. The print at the end of a `while 1:`
  body costs a byte more than `while[print(m-k)]:`, but that header would
  need the start `m=2;k=1`, two bytes more than `m=k=0`.

**Notes**

- `m=2;k=1` / `while[print(m-k)]:m+=2;k+=m>k*k+k` is 41 bytes. Keeping the
  term itself and stepping by 1 or 2 depending on whether it is k²,
  `a=k=1` / `while[print(a)]:a+=1+(a<k*k);k+=a>k*k`, is 43; the OEIS closed
  form 2n − ⌊(1 + √(8n − 7))/2⌋ with `math.isqrt` is 64.
- Exact integers, so every term is right.
- The b-file has 1000 terms (n = 1 to 1000) and all of them print at once; the
  bar is the whole b-file in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-13 | Python 3 | 40 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001614), CC BY-SA 4.0.
