# A000614

> Number of complemented types of Boolean functions of n variables under action of AG(n,2).
> — [OEIS A000614](https://oeis.org/A000614)

Offset 1: 2, 3, 6, 18, 206, 7888299, 8112499583888855378066, …

### Python 3 — 217 bytes

```python
n=r=b=1
while 1:
 t=k=0
 for i in range((N:=2**n)<<n*n):
  for _ in[m:=[i%N]]*n:i>>=n;m+=[y^~i%N for y in m];t+=r<<b;b=r=len({*m})>>n;k+=2*r
  for x in m:
   while~x:b&=m[x]!=x;m[x],x=-1,m[x];r<<=x<0
 print(t//k);n+=1
```

**What is counted**

- Classes of Boolean functions of n variables under the affine group
  AG(n,2) (substitutions x → Ax ⊕ s) together with complementing the
  output. By Burnside's lemma
  a(n) = Σ_g (fix(g) + #{f : f∘g = ¬f}) / (2·|AG(n,2)|).
- fix(g) = 2^c(g), with c(g) the number of cycles of g on the 2ⁿ points.
  f∘g = ¬f needs f to alternate along every cycle, which has 2^c(g)
  solutions when all cycles are even and none otherwise.
- For an affine map over GF(2), an odd cycle exists exactly when g has a
  fixed point: the XOR of the points of an odd cycle is fixed (see
  [A000370](../A000370/)). So each g contributes 2^c(g) times 2 if it has
  no fixed point and 1 otherwise.

**How it works**

- The loop is the A000214 program: `i` holds a translation s (its low n
  bits) and n complemented columns, the doubling builds `m[x]` = Ax ⊕ s,
  `len({*m})>>n` is 1 exactly for an invertible A, and the walk leaves
  `r` = 2^c(g).
- The walk also clears `b` at a fixed point (`b&=m[x]!=x`), so `r<<b` is
  2^c(g)·(2 or 1). Like `r`, it is added to `t` one element late, at the
  first column of the next element, before `b=r=…` resets both; the last
  element of each n has A = 0, which contributes 0.
- `k` grows by 2 per element of AG(n,2). The initial r = b = 1 adds a
  spurious 2 at n = 1, where the true t is 8 and k = 4, so `t//k` is still 2.

**Notes**

- The loop visits all 2^(n+n²) maps: n = 4 (about a million) takes about
  40 s here, n = 5 would need 2³⁰. The bar is the 4 terms n = 1 to 4 in
  120 s; the b-file has 8.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-07 | Python 3 | 217 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000614), CC BY-SA 4.0.
