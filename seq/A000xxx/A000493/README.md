# A000493

> a(n) = floor(sin(n)).
> — [OEIS A000493](https://oeis.org/A000493)

Offset 0: 0, 0, 0, 0, -1, -1, -1, 0, 0, 0, …

### Python 3 — 126 bytes

```python
s=lambda t,d=1:t and t+s(t*d//(d-~d),d+1)
n=j=0
while 1:
 j+=1;p=2*s(S:=2**j)
 while(q:=n*S//(p+8*j))==n*S//p:print(q%-2);n+=1
```

**How it works**

- For n ≥ 1, sin n is strictly between −1 and 1 and never 0, so its floor
  is 0 when sin n > 0 and −1 when sin n < 0, that is, when ⌊n/π⌋ is even or
  odd. So a(n) = −(⌊n/π⌋ mod 2), and `q%-2` is exactly that: Python's `%`
  takes the sign of the divisor, so q % −2 is 0 or −1.
- π comes from Euler's series π/2 = Σ_{k≥0} k!/(2k+1)!! =
  1 + 1/3 + 1·2/(3·5) + …, whose terms satisfy T_k = T_{k−1}·k/(2k+1).
  `s(t)` adds t, then calls itself on ⌊t·d/(2d+1)⌋ (`d-~d` is 2d + 1)
  until the term is 0.
- **Error bound.** Let S = 2^j and t_k the floored terms. Since
  k/(2k+1) < ½, induction gives 0 ≤ T_k − t_k < 2, and since T_k < S/2^k,
  the first zero term t_K has K ≤ j. The loss is then below 2(K − 1) for the
  terms kept (t₀ = S is exact) plus 2T_K < 4 for the tail, so
  s(S) ≤ Sπ/2 < s(S) + 2j + 2. With p = 2s(S) this gives
  p ≤ Sπ < p + 4j + 4 ≤ p + 8j.
- Hence ⌊nS/(p + 8j)⌋ ≤ ⌊n/π⌋ ≤ ⌊nS/p⌋, and when the two floors agree the
  value is certain. The inner loop prints as many n as the current bounds
  settle; otherwise j grows by one, so the bounds get one bit sharper each
  pass.
- n/π is never an integer for n ≥ 1 (π is irrational), so every n is
  settled once S is large enough; n = 0 gives 0 on both sides.

**Notes**

- Same program with the exact bound `4*j+4`: 128 bytes. `print(-(q%2))`
  costs 4 bytes more than `q%-2`. Machin's formula
  π = 16·atan(1/5) − 4·atan(1/239) with an error allowance: 195 bytes.
- Summing the Taylor series of sin n directly, with the sign-flipping
  denominator of [A000494](../A000494/) and floor instead of rounding
  (`N=p=n;F=1;d=0` / `while N%F<p:d+=2;p*=n*n;N=p+N*~d*d;F*=~d*d`), is
  89 bytes, but each term costs about 1.4n big-number steps: only about
  1400 terms in 60 s here, far short of the bar.
- Exact integer arithmetic, so the program is right for every n. `s`
  recurses j levels deep; Python's default recursion limit (1000) would
  only bite for an n whose n/π lies within about 2^−990·n of an integer.
- About 3.3 million terms in 60 s here. The b-file has 10001 terms (up to
  a(10000)); the bar is the whole b-file in 60 s, which takes 0.2 s.
- The terms are 0 and −1, so the 4300-digit int-to-str limit never applies.

## First 1000 terms

A [separate record](../../../CONTRIBUTING.md#short-bar-records): the same
rules, but only a(0)…a(999) have to arrive in time.

### Python 3, 1000 terms — 89 bytes

```python
n=0
while 1:
 N=p=n;F=1;d=0
 while N%F<p:d+=2;p*=n*n;N=p+N*~d*d;F*=~d*d
 print(N//F);n+=1
```

**How it works**

- It sums the Taylor series sin n = Σ_k (−1)^k n^(2k+1)/(2k+1)! exactly.
  After k steps, N/F is the partial sum S_k, and |p/F| = n^(2k+1)/(2k+1)! =
  t_k is its last term. `~d*d` is −(d+1)·d with d = 2k, so F = (−1)^k·(2k+1)!
  changes sign at every step and N stays an integer:
  N_k = n^(2k+1) − (2k+1)(2k)·N_{k−1}.
- When F < 0 (odd k), `N%F` lies in (F, 0], below p, so the loop goes on.
  When F > 0 (even k, the last term was added), `N%F<p` fails exactly when
  the fractional part of S_k is at least t_k.
- Stopping there is safe. If t_k < 1 then n < 2k + 1 (because
  (2k+1)! ≤ (2k+1)^(2k+1)), so from term k on the terms decrease and
  alternate, and sin n lies in [S_k − t_k, S_k]. With fractional part at
  least t_k, that interval holds no integer, so ⌊sin n⌋ = ⌊S_k⌋ = `N//F`.
  While t_k ≥ 1 the test cannot pass, since the fractional part is below 1.
- It always stops. For n ≥ 1, sin n is not an integer, S_k → sin n and
  t_k → 0, so the fractional part of S_k tends to that of sin n > 0 and
  ends up above t_k. For n = 0, p = 0 and the loop is skipped: a(0) = 0.

**Limits**

- Exact integer arithmetic. Each term costs about 1.4·n big-number steps
  on numbers of about n·log n digits. Here a(999) arrives after about
  11 s (about 6 reference seconds) and the 1600th term after 60 s, far
  short of the main bar of 10001 terms.

## History

**Python 3**

| Date | Bytes | Note |
|---|---|---|
| 2026-11-06 | 210 | first entry |
| 2026-11-06 | 195 | share the Machin summand and remove multiplication by one |
| 2026-11-07 | 126 | Euler's series k!/(2k+1)!! for π, `q%-2` |

**Python 3, 1000 terms**

| Date | Bytes | Note |
|---|---|---|
| 2026-11-09 | 89 | first entry: exact Taylor series of sin n, stop when the floor is certain |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000493), CC BY-SA 4.0.
