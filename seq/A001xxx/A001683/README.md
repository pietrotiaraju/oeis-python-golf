# A001683

> Number of one-sided triangulations of the disk; or flexagons of order n; or unlabeled plane trivalent trees (n-2 internal vertices, all of degree 3 and hence n leaves).
> — [OEIS A001683](https://oeis.org/A001683)

Offset 2: 1, 1, 1, 1, 4, 6, 19, 49, 150, 442, 1424, 4522, 14924, 49536, …

### Python 3 — 88 bytes

```python
m=2;L=[c:=1]
while 1:L+=[0]*5+[c];print((6*c//m+3*L[3*m]+4*L[2*m])//6);c=4*c-6*c//m;m+=1
```

**How it works**

a(m) counts the triangulations of a convex m-gon up to rotation (entry
comment, Bowman and Regev). The C_{m−2} triangulations (C_k the Catalan
numbers) fall into orbits under the cyclic group of order m, so by
Burnside's lemma a(m) is the average number of triangulations fixed by a
rotation. Only rotations of order 1, 2 and 3 fix any: a half turn fixes
those with a diameter, m/2 choices times C_{m/2−1} for one half, and each
of the two third turns fixes those with a central triangle, m/3 choices
times C_{m/3−1}. That is the formula in the entry,

  a(m) = C_{m−2}/m + C_{m/2−1}/2 + (2/3)·C_{m/3−1}

(a term dropped when its index is not an integer), and times 6:

  **6a(m) = 6C_{m−2}/m + 3·[2 | m]·C_{m/2−1} + 4·[3 | m]·C_{m/3−1}.**

- `c` holds C_{m−2}. The Catalan identity 6C_{m−2}/m = 4C_{m−2} − C_{m−1}
  makes `6*c//m` exact, and the same identity is the update
  C_{m−1} = 4C_{m−2} − 6C_{m−2}/m (the trick of [A000207](../../A000xxx/A000207/),
  the same count up to reflections as well).
- The list `L` keeps the Catalan numbers six apart with zeros between
  them: L[6k+6] = C_k. Then `L[3*m]` is C_{m/2−1} when m is even and 0
  when it is odd, and `L[2*m]` is C_{m/3−1} when 3 | m and 0 otherwise,
  so neither divisibility needs a test. L[0] is never read.
- Each pass appends C_{m−2} before printing, so the largest index read,
  3m, is always inside the list (it has 6m − 5 entries).

**Golf tricks**

- One list spaced by 6 = lcm(2, 3) serves both divisors; `[0]*5+[c]` is
  1 byte under `0,0,0,0,0,c`.

**Notes**

- Exact integer arithmetic throughout, so the program is right for every
  m; the only inputs are Burnside's lemma and the fixed-point counts
  above.
- The whole b-file (199 terms, up to a(200)) prints in about 0.1 s; the
  bar is the whole b-file in 60 s.
- a(7161) is the first term with more than 4300 digits, where Python's
  int-to-str limit stops the program (after about 2.5 s).

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-14 | Python 3 | 88 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001683), CC BY-SA 4.0.
