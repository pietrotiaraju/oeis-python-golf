# A000435

> Normalized total height of all nodes in all rooted trees with n labeled nodes.
> — [OEIS A000435](https://oeis.org/A000435)

Offset 1: 0, 1, 8, 78, 944, 13800, 237432, 4708144, 105822432, 2660215680, …

### Python 3 — 72 bytes

```python
n=1
while 1:
 a=0;f=1
 for j in range(1,n):f*=n-j;a=a*n+f
 print(a);n+=1
```

**How it works**

- The formula a(n) = (n−1)!·Σ_{k=0}^{n−2} nᵏ/k! from the OEIS page, with
  k = n − 1 − j, is the polynomial Σ_{j=1}^{n−1} f_j·n^(n−1−j) in n with
  integer coefficients f_j = (n−1)!/(n−1−j)! = (n−1)(n−2)···(n−j).
- Horner's rule evaluates it from the top power down: in pass j, `f*=n-j`
  turns f into f_j and `a=a*n+f` appends that coefficient. For n = 4 the
  pairs (f, a) are (3, 3), (6, 18), (6, 78), and 78 = 3!·(1 + 4 + 4²/2!).
- At n = 1 the loop is empty and a(1) = 0 is printed.

**Notes**

- Counting k down, `for k in range(n-1,0,-1):f*=k;a=a*n+f`: 75 bytes. The
  Horner loop as a walrus comprehension on one line,
  `a=0;f=1;[a:=a*n+(f:=f*(n-j))for j in range(1,n)];print(a);n+=1`: 74. The
  sum with `math.perm(n-1,j)*n**(n+~j)`: 85, and too slow for the bar.
- Exact integer arithmetic, so the program is right for every n.
- The b-file in this repository differs from the one on the OEIS site: the
  OEIS file has lost leading digits at n = 841, 846, 857, 858, 859, 929, 936,
  938, 939, 940 and 941, and the repository's values there agree with the
  formula above.
- The b-file has 1000 terms (up to a(1000)); the bar is the whole b-file in
  60 s, which takes about a second here.
- a(1372) is the first term with more than 4300 digits, so Python's
  int-to-str limit stops the printing there, after about 3 s here.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 75 | first entry |
| 2026-11-07 | Python 3 | 72 | Horner counter j with `f*=n-j` |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000435), CC BY-SA 4.0.
