# A001038

> Invertible Boolean functions with GL(n,2) acting on the domain and range.
> — [OEIS A001038](https://oeis.org/A001038)

Offset 1: 2, 2, 10, 52246, 2631645209645100680144, 312242081385925594286511113384607360432260178128338777217975928751832

### Python 3 — 274 bytes

```python
n=1
while 1:
 N=2**n;Q=[]
 for i in range(N**n):
  for _ in[m:=[0]]*n:m+=[y^i%N for y in m];i>>=n
  c=[0]*N*2;z=1
  for x in m:
   k=0
   while~x:m[x],x=-1,m[x];k-=1
   if k:c[k]+=1;z*=~k*c[k]
  Q+=[(z,*c)]*-max(m)
 print(sum(Q.count(K)**2*K[0]for K in{*Q})//len(Q)**2);n+=1
```

**What is counted**

An invertible Boolean function is a permutation π of the N = 2ⁿ points of
{0,1}ⁿ. G = GL(n,2) acts on both sides, π ↦ h∘π∘g, and a(n) is the number
of orbits. By Burnside's lemma it is (1/|G|²) Σ_{g,h} #{π : h∘π∘g = π}. The
condition says π g π⁻¹ = h⁻¹, so there is no such π unless g and h have the
same cycle type λ on the N points, and then there are exactly as many as
permutations commuting with g, z_λ = Π_L L^(m_L)·m_L! (m_L cycles of length
L). Hence

a(n) = Σ_λ c_λ²·z_λ / |G|²,

where c_λ is the number of elements of GL(n,2) with cycle type λ.

**How it works**

- **Every matrix.** i runs over the 2^(n²) = Nⁿ choices of n columns of n
  bits. `for _ in[m:=[0]]*n:m+=[y^i%N for y in m];i>>=n` starts from m = [0]
  and doubles it once per column, so m[x] is the image of x (the walrus
  resets m and gives the n passes at once).
- **Cycles.** As on [A000214](../../A000xxx/A000214/), `for x in m` reads
  each position; a −1 means visited and skips, anything else starts a walk
  that marks its cycle −1 and stops after L+1 steps. k counts the steps
  down, so `c[k]` (a negative index) counts the cycles of each length and
  `~k` is L itself: `z*=~k*c[k]` multiplies L·(number of L-cycles so far),
  which is z_λ when the walk is over.
- **Only bijections.** A singular map has points with no preimage; no walk
  ever reaches them, so their entries of m stay ≥ 0 and `-max(m)` is ≤ 0. A
  bijection leaves every entry −1, so `[(z,*c)]*-max(m)` adds its key once
  and the others not at all.
- The key (z, cycle counts) names the cycle type and carries z_λ. Q holds
  one key per element of GL(n,2), so `Q.count(K)` is c_λ and `len(Q)` is
  |G|; the sum runs over the distinct keys.

**Speed**

All 2^(n²) matrices are visited: a(4) (65536 matrices, |GL(4,2)| = 20160)
takes under a second here, but a(5) needs 2²⁵ matrices with
|GL(5,2)| ≈ 10⁷ walks of 32 points, far beyond a minute. The bar is the
first 4 terms within 60 s; the b-file is the OEIS data, 6 terms.

**Notes**

- Lorens' paper gave a(5) = 2631645209645100680142; the OEIS has the
  corrected …144 (Sean A. Irvine).
- Summing cycle types over conjugacy classes of GL(n,2) (rational canonical
  forms) would reach a(5) and a(6) but is far longer.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-08 | Python 3 | 274 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001038), CC BY-SA 4.0.
