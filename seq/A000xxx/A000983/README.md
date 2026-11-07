# A000983

> Size of minimal binary covering code of length n and covering radius 1.
> — [OEIS A000983](https://oeis.org/A000983)

Offset 1: 1, 2, 2, 4, 7, 12, 16, 32, 62, …

### Python 3 — 180 bytes

```python
P=[0,1];k=1
f=lambda U,k:not U or k*len(P)>=len(U)and any(f(U-{w^i^j for j in P},k-1)for w in[min(U)]for i in P)
while 1:
 if f({*range(2*P[-1])},k):print(k);P+=2*P[-1],
 else:k+=1
```

**How it works**

- Exhaustive search with a growing code size k. `P` holds 0 and the
  one-bit masks, so the ball of radius 1 around c is `{c^j for j in P}`,
  n+1 words.
- `f(U,k)` decides whether k codewords can cover the set U of words not
  yet covered. Take the smallest uncovered word w: some codeword lies in
  its ball, so branch over the n+1 words w^i and remove their balls. Prune
  when k(n+1) < |U|, since a codeword covers at most n+1 words.
- k is not reset between lengths: K(n+1,1) ≥ K(n,1), because deleting the
  last coordinate of a covering code of length n+1 gives one of length n
  (the word (x, 0) is within distance 1 of some codeword). So k carries on
  from the previous term, and the `if`/`else` loop prints k when f says
  yes and raises it when f says no.
- `for w in[min(U)]for i in P` binds w once, 1 B under building the set of
  candidate codewords.

**Notes**

- Exact search; the only fact used is the monotonicity above.
- a(6) = 12 needs the proof that 11 words cannot cover all 64: about 45 s
  here. a(7) = 16 is the perfect Hamming code, where the counting bound
  leaves no slack and the search is instant. a(8) = 32 would mean ruling
  out 31 words among 256, far out of reach.
- The b-file is synthesized from the 9 terms of the entry; the bar is
  7 terms in 120 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 180 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000983), CC BY-SA 4.0.
