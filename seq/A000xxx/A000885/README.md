# A000885

> Number of twin prime pairs < square of n-th prime.
> — [OEIS A000885](https://oeis.org/A000885)

Offset 1: 0, 2, 4, 6, 10, 12, 19, 21, 25, 33, 35, 46, 53, 56, 67, 80, 93, 98, …

### Python 3 — 86 bytes

```python
P=k=1;h=t=0;S={0}
while 1:k in S==print(t);h=h*2+P%k;t+=h&5>4;S|={P%k*k*k};P*=k*k;k+=1
```

**How it works**

- Pairs are counted when the loop reaches their larger member k. a(1) = 0
  shows that (3, 5), which straddles 4 = 2², does not count, so a pair
  counts only when both members are below p_n². For p ≥ 3, p² is odd and
  composite, so it is neither a member nor the even middle of a pair, and
  "larger member below p²" is the whole condition.
- Wilson's theorem with `P` = ((k−1)!)²: `P%k` is 1 at primes, 0 otherwise.
- `h` keeps the 0/1 flags as bits, newest in bit 0 (`h=h*2+P%k`), so
  (k−2, k) is a twin pair exactly when bits 0 and 2 are set: `h&5>4` (`&`
  binds tighter than `>`). At k = 4 the primes 2, 3 sit in bits 2 and 1,
  and `h&5` is 4, so the pair (2, 3) is not counted.
- `S` holds k² for every prime k found (and 0), and
  `k in S==print(t)` prints the count t when k is a prime square, before
  anything at k is counted. Each prime p is added at k = p, long before p².
- A set of prime squares can also detect the pairs,
  `t+={k*k,(k-2)**2}<=S` after adding k² (with t starting at −1, since
  k = 2 meets the filler 0), but that is 1 byte longer.

**Notes**

- Exact integer arithmetic; the only facts used are Wilson's theorem and
  that p² is composite.
- `P` has about 2k·log₂k bits and each step multiplies it and takes a
  remainder, so reaching k costs about k² operations: 58 terms in 60 s (up
  to p = 271, k ≈ 73000). `h` grows by one bit per step, far less.
- The b-file has 10000 terms; the bar is 44 terms in 60 s.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 86 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000885), CC BY-SA 4.0.
