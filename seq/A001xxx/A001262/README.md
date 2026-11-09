# A001262

> Strong pseudoprimes to base 2.
> — [OEIS A001262](https://oeis.org/A001262)

Offset 1: 2047, 3277, 4033, 4681, 8321, 15841, 29341, 42799, 49141, 52633, …

The odd composite numbers k that pass the Miller–Rabin test to base 2:
writing k − 1 = d·2ˢ with d odd, either 2ᵈ ≡ 1 (mod k) or
2^(d·2ʳ) ≡ −1 (mod k) for some 0 ≤ r < s.

### Python 3 — 116 bytes

```python
f=lambda e:pow(2,e,k)%~-k<=(e%2or f(e//2))
k=m=3
while[f(k-1)>all(k%i for i in range(2,m))==print(k)]:k+=2;m+=m*m<=k
```

**How it works**

- Only odd k ≥ 3 are tried (`k+=2`). Let xᵢ = 2^(d·2ⁱ) mod k for
  i = 0, …, s; each is the square of the one before, and xₛ = 2^(k−1).
- `pow(2,e,k)%~-k` is the residue v = 2ᵉ mod k taken mod k − 1: it turns
  v = k − 1 (that is, −1) into 0 and leaves 0, …, k − 2 alone. v = 0 never
  happens, since k is odd. So `…<=1` means v = ±1 and `…<=0` means v = −1.
- `f(e)` with e = d·2ʳ says whether x₀ = 1 or −1 is among x₀, …, xᵣ. For
  odd e (r = 0) the bound is `e%2` = 1, so it tests x₀ = ±1. For even e the
  bound is `f(e//2)`, the same question one level down: if that is false,
  the test is xᵣ = −1, as it should be; if it is true, then x₀ = 1 or some
  xᵢ = −1 with i < r, and every later square is 1, so xᵣ = 1 ≤ `True` and
  the answer stays true.
- `f(k-1)` asks this at r = s, which also allows xₛ = −1. That cannot
  happen: 2^(k−1) ≡ −1 would make the order of 2 modulo every prime p | k
  divisible by 2^(s+1), so p ≡ 1 (mod 2^(s+1)) and k ≡ 1 (mod 2^(s+1)),
  against 2ˢ being the exact power of 2 in k − 1. So `f(k-1)` is exactly
  the strong test, with no probabilistic step.
- `all(k%i for i in range(2,m))` is trial division, and `m` keeps
  m² > k: it starts at 3 > √3, and when k grows by 2 with m² ≤ k it
  grows to m + 1, whose square m² + 2m + 1 exceeds the new k. It only grows
  while m ≤ √k, so 2 ≤ i < m stays below k. Hence `all(…)` is true exactly
  when k is prime.
- `f(k-1)>all(…)` is `True > False`: strong probable prime and composite.
  The chained `==print(k)` prints k only then. The list `[…]` is never
  empty, so the loop runs forever.

**Notes**

- Trial division up to √k on every prime dominates the time: here a(70) =
  1907851 arrives after about 17 reference seconds, and about 88 terms
  arrive within the 30 that count.
- Testing compositeness with `math.gcd` against a running
  `lcm(1, …, isqrt(k))` is roughly twice as fast but 130 bytes, since
  `from math import*` hides the built-in three-argument `pow` and needs
  `P=pow` first; `gcd(perm(isqrt(k)),k)` is 122. Running the trial
  division only after the strong test passes (`1==f(k-1)>…`) saves about
  7% of the time for 3 bytes.
- The b-file has 10000 terms (up to 142899381901);
  the bar is 70 terms in 60 s.

## First 17 terms

A [separate record](../../../CONTRIBUTING.md#short-bar-records): the same
rules, but only a(1)…a(17) have to arrive in time.

### Python 3, 17 terms — 86 bytes

```python
f=lambda e:pow(2,e,k)in{k-1,e%2or f(e//2)}
k=P=2
while[P%k<f(k-1)==print(k)]:P*=k;k+=1
```

**How it works**

- Wilson's theorem instead of trial division: `P` is 2·(k − 1)! (it
  starts at 2 for k = 2 and gains a factor k per step). For an odd prime k
  it is ≡ −2 ≢ 0 (mod k); for an odd composite k ≥ 9, k divides (k − 1)!.
  So for odd k, `P%k` is 0 exactly when k is composite.
- Every k ≥ 2 is tried, so the strong test must reject even k. Here `f`
  checks `pow(2,e,k)in{k-1,e%2or f(e//2)}`: for odd e that is v ∈ {−1, 1};
  for even e the set is {−1, `f(e//2)`}, that is {−1, 1} when the level
  below holds and {−1, 0} when it does not, where 0 cannot occur for odd k.
  This is the same recursion as in the main record. For even k the top
  exponent k − 1 is odd and 2^(k−1) mod k is even, never −1 or 1, so even
  k are never printed.
- `P%k<f(k-1)` is `0 < True`: composite and a strong probable prime.

**Limits**

- `P` has about k·log₂ k bits, so each step costs time proportional to k:
  a(17) = 104653 arrives after about 19 reference seconds, and a(18) =
  130561 would come too close to the limit of 30.

## History

**Python 3**

| Date | Bytes | Note |
|---|---|---|
| 2026-11-09 | 116 | first entry |

**Python 3, 17 terms**

| Date | Bytes | Note |
|---|---|---|
| 2026-11-09 | 86 | first entry: Wilson's theorem with a running factorial |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001262), CC BY-SA 4.0.
