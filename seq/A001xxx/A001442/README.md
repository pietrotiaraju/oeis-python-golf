# A001442

> G-symmetric Costas arrays of order n that are inequivalent under dihedral group.
> — [OEIS A001442](https://oeis.org/A001442)

Offset 1: 1, 1, 0, 2, 1, 4, 0, 3, 0, 24, 0, 44, 4, 31, 0, 77, 0, 29, 0, 3, …

A Costas array of order n is an n × n permutation array (one dot per row
and column) whose dots have pairwise distinct displacement vectors. The
entry gives no definition of G-symmetry; this page reads it as the
glide-reflection ("anti-reflective") symmetry of the Costas array
literature: with columns and rows numbered from 0 and h = ⌈n/2⌉, the
permutation f satisfies f(i) + f(i + h) = n − 1 for every i < n − h. The
right half of the array is the left half shifted h columns and turned
upside down; for odd n the middle column then holds the centre dot. The
term counts the classes, under the eight symmetries of the square, of
Costas arrays that contain a G-symmetric one. Read this way, a separate
faster search of the same definition gives all 23 terms of the entry
(Welch arrays, of order p − 1 for a prime p, all have this symmetry).

### Python 3 — 289 bytes

```python
g=lambda P,k:k//n*(2-all(c-w+w%K*2in P for w in P if w%K<n-h)+2*({w%K*K+w//K for w in P}=={*P}))+sum(g(Q,k+1)for v in range(n)if k<h or v+P[k-h]%K==n-1for Q in[P+[K*k+v]]if len({a-b for a in Q for b in Q if(a-b)%K})==k*k+k)
n=1
while[K:=2*n,h:=n-n//2,c:=K*n-K+h,print((g([],0)+7)//8)]:n+=1
```

**How it works**

- **Costas test.** The dot in column x and row y is the number K·x + y with
  K = 2n. Since |Δy| < n, the difference of two codes, K·Δx + Δy,
  determines the displacement (Δx, Δy). Differences divisible by K are
  exactly those with Δy = 0 (zero, or two dots in one row); the others
  are kept, and k + 1 dots in distinct rows with distinct displacements
  give exactly k(k + 1) of them: `len({…if(a-b)%K})==k*k+k`. A part of a
  Costas array passes too, so `g` places one dot per column k and prunes
  as it goes (a dot in column n would repeat a row, so it stops there).
- **G-symmetry.** Columns k < h are free; from column h on, the row is
  forced: `v+P[k-h]%K==n-1`. So only about half of the columns branch,
  and `g` meets every G-symmetric Costas array once.
- **Classes, by Burnside.** Let X be the set of Costas arrays whose class
  contains a G-symmetric one. Turning upside down, reversing the columns
  and the half-turn keep G-symmetry, and the other four symmetries of the
  square are these followed by the transpose, so X is the G-symmetric
  arrays together with their transposes: |X| = 2G − B, where G counts the
  G-symmetric arrays and B those whose transpose is G-symmetric too. For
  n ≥ 3 no Costas array is fixed by the half-turn (the dot pairs in
  columns 0, 1 and in columns n − 2, n − 1 would have the same
  displacement), hence none by a quarter-turn, and the reflections in the
  middle row or column fix no permutation array; the transpose fixes the
  I involutions of X, which are G-symmetric, and the other diagonal
  reflection as many (a quarter-turn carries one to the other). So
  a(n) = (2G − B + 2I)/8, and each G-symmetric array f adds
  2 − [f transposed is G-symmetric] + 2·[f is an involution] (at k = n,
  the only k with `k//n` = 1).
- **The two tests.** f transposed is G-symmetric when every dot (x, y)
  with y < n − h has a partner (n − 1 − x, y + h); for a dot with code w
  the partner's code is c − w + 2y, c = K(n − 1) + h (`c-w+w%K*2in P`). f is an
  involution when swapping x and y maps the codes onto themselves
  (`{w%K*K+w//K for w in P}=={*P}`).
- `(…+7)//8` is exact for n ≥ 3 and also gives a(1) = 1 (one array,
  weight 3) and a(2) = 1 (two arrays, weight 3 each).
- This is not simply G/4: at n = 8 there are 16 G-symmetric arrays, but
  one class has all eight of its arrays G-symmetric, so a(8) = 3.

**Notes**

- Exact integers, no stored terms.
- a(12) = 44 comes after about 20 s here and a(13) = 4 after about two
  and a half minutes: the bar is 12 terms in 60 s (the b-file has the 23
  terms of the entry).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-09 | Python 3 | 289 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001442), CC BY-SA 4.0.
