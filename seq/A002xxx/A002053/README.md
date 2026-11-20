# A002053

> a(n) = least value of m for which Liouville's function A002819(m) = -n.
> — [OEIS A002053](https://oeis.org/A002053)

Offset 0: 2, 3, 8, 13, 20, 31, 32, 53, 76, 79, 80, 117, 176, 181, 182, 193, 200, …

### Python 3 — 118 bytes

```python
l=[0,1];u=m=1;D={}
while m:=m+1:
 p=D.pop(m,m);x=m+p
 while x in D:x+=p
 D[x]=p;l+=-l[m//p],;u+=l[-1];u+=u<1!=print(m)
```

**How it works**

- A002819(m) = L(m) = λ(1) + … + λ(m), with Liouville's
  λ(k) = (−1)^Ω(k). L(1) = 1 and each step changes L by ±1, so L first
  reaches −n just after it first reaches −(n − 1): the terms are the m
  where L sets a new low, in increasing order (a(0) = 2, since
  L(2) = 0).
- λ is completely multiplicative, so λ(m) = −λ(m/p) for any prime p
  dividing m. `l[k]` holds λ(k).
- D is an incremental sieve of Eratosthenes. Every prime p < m has
  exactly one key in D, a multiple of p at or after m, with value p;
  when that key is reached it moves on to the next multiple of p that is
  not already a key (`while x in D:x+=p`). A multiple it walks past is
  already a key of another prime, so every multiple of p from 2p on is a
  key when it is reached. Hence a composite m is always popped with one
  of its prime factors, while a prime m is never a key: `D.pop(m,m)`
  gives p = m, so m//p = 1 and λ(m) = −λ(1) = −1, and the new prime
  starts its walk at 2m.
- u is L(m) + n, where n terms have been printed so far: it starts at
  L(1) = 1, follows λ, and when it hits 0, L(m) = −n for the first time;
  `u<1!=print(m)` then prints m and is true, so u goes back to 1.

**Notes**

- Exact integer arithmetic, so the program is right for every n. It
  keeps λ for every k ≤ m and one entry per prime in D, so memory grows
  linearly: about 250 MB by m = 1.3·10⁷.
- The b-file has 10001 terms, up to 75748786. The bar is 4500 terms
  (up to 12861418) in 60 s; they take about 26 s here. The terms come in
  bursts, as L dips to a new low and stays near it.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 118 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002053), CC BY-SA 4.0.
