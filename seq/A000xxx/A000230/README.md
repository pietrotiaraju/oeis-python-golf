# A000230

> a(0)=2; for n>=1, a(n) = smallest prime p such that there is a gap of exactly 2n between p and next prime, or -1 if no such prime exists.
> — [OEIS A000230](https://oeis.org/A000230)

Offset 0: 2, 3, 7, 23, 89, 139, 199, 113, 1831, 523, 887, 1129, …

### Python 3 — 71 bytes

```python
p=m=2
while[print(p)]:
 P=k=p=1
 while(g:=p*P%k)-m:p+=g;P*=k;k+=1
 m+=2
```

**How it works**

- The loop header prints the previous answer, so `p=m=2` prints a(0) = 2
  before any search; after that m = 2n is the gap being looked for.
- Each search restarts at k = 1 with P = (k−1)! and p = the last prime below
  k (p = 1 stands in before 2). Wilson's theorem gives P ≡ −1 (mod k) for a
  prime k, so `p*P%k` is −p mod k = k − p, the gap from the previous prime.
  For a composite k > 4, k divides (k−1)!, so it is 0. `p+=g` then moves p
  to k exactly when k is prime, with no prime test of its own.
- The one exception is k = 4: 3!·3 = 18 ≡ 2 (mod 4), so the gap 3 → 5 is
  reported one step early, p jumps to 5, and at k = 5 the value is
  5·4! ≡ 0. The gaps still come out once each and in order.
- The sentinel gives a fake gap 1 at k = 2, and 2 → 3 the real gap 1; m is
  even and at least 2, so neither can stop the search. The first k with
  g = m ends it, and p is then the smallest prime followed by a gap of
  exactly m.

**Notes**

- The program never prints −1. If some even number were never a gap between
  consecutive primes, it would search forever at that n. That every even
  number occurs as a gap at least once is a conjecture (de Polignac's
  conjecture says infinitely often), still open: Zhang and Maynard–Polymath
  only show that some gap ≤ 246 occurs infinitely often. All 722 terms in the
  b-file exist.
- Every term restarts the scan, and (k−1)! grows to a few hundred thousand
  digits, so the time goes with the largest a(n) so far: 29 terms in 60 s
  here, the 24th (a(23) = 81463) at 25 s. The bar is 24 terms.
- Walking the primes once and keeping the first prime of each gap in a dict
  is 92 bytes and gets 33 terms in 60 s:

  ```python
  d={};n=0;P=k=1;p=2
  while 1:
   if g:=p*P%k:d={g>>1:p}|d;p+=g
   n+=n in d!=print(d[n]);P*=k;k+=1
  ```

  `{g>>1:p}|d` keeps the first prime for each gap (the right operand wins),
  and `n+=n in d!=print(d[n])` prints at most one term per k, which is
  enough to keep up.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 71 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000230), CC BY-SA 4.0.
