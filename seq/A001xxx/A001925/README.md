# A001925

> From rook polynomials.
> — [OEIS A001925](https://oeis.org/A001925)

Offset 0: 1, 6, 22, 64, 162, 374, 809, 1668, 3316, 6408, 12108, 22468, 41081, …

### Python 3 — 59 bytes

```python
n=p=q=r=s=0
while 1:n+=1;p,q=n*n+p+q,p;r,s=p+r+s,r;print(r)
```

**How it works**

- **Definition.** The entry gives one formula, Riordan's generating function
  (1 + x)/((1 − x − x²)²·(1 − x)³), from his paper on discordant
  permutations, where it comes out of rook polynomials; the name says no more.
  The program prints the coefficients of that series, and all 1001 terms of
  the b-file agree with it.
- **Two filters.** (1 + x)/(1 − x)³ = Σ (n + 1)²·xⁿ, and dividing a series by
  1 − x − x² is the filter y(n) = u(n) + y(n − 1) + y(n − 2). So a(n) is
  (n + 1)² passed twice through that filter: `p`, `q` hold the last two outputs
  of the first, `r`, `s` of the second, and `n` is n + 1 when it is squared.

**Notes**

- Exact integer arithmetic, so the program is right for every n.
- The b-file has 1001 terms (n = 0 to 1000); the bar is the whole b-file in
  60 s, which takes a fraction of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-18 | Python 3 | 59 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001925), CC BY-SA 4.0.
