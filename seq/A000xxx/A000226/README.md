# A000226

> Number of n-node unlabeled connected graphs with one cycle of length 3.
> — [OEIS A000226](https://oeis.org/A000226)

Offset 3: 1, 1, 3, 7, 18, 44, 117, 299, 793, 2095, 5607, 15047, 40708, …

### Python 3 — 167 bytes

```python
R=[n:=1]
while[print(sum((R[a]+(a==b))*(R[b]+2*(n+~a==b+b))*R[~a-b]for a in range(n)for b in range(n-a))//6)]:R+=sum(-~j*R[j]*sum(R[~j::~j])for j in range(n))//n,;n+=1
```

**How it works**

- Cut the three edges of the triangle and each corner keeps a rooted tree,
  so a(n) counts multisets of three rooted trees with n nodes in all, or
  rooted trees on n+1 nodes whose root has degree 3. With r(x) the rooted
  trees ([A000081](../A000081/)), the OEIS g.f. is the cycle index of S₃:
  6·a = [xⁿ] (r(x)³ + 3·r(x)·r(x²) + 2·r(x³)).
- `R` lists the rooted forests f(0), f(1), … ([A000081](../A000081/)
  shifted: f(k) = r(k+1)), so R[i] is the number of trees with i+1 nodes.
  The update is the Euler-transform recurrence of [A000151](../A000151/)
  without its factor 2: N·f(N) = Σ_{e=1..N} e·f(e−1)·Σ_{t≥1} f(N−te), where
  `-~j*R[j]` is e·f(e−1) for e = j+1 and the slice `R[~j::~j]` steps back
  from the end of the list by e.
- Counting each tree by its node count minus one, three trees with n nodes
  in all have indices a+b+c = D = n−3. The three Burnside terms become
  T₁ = Σ_{a+b+c=D} R[a]R[b]R[c], T₂ = Σ_{a+2b=D} R[a]R[b] and
  T₃ = R[D/3] (for 3 | D), and 6·a(n) = T₁ + 3T₂ + 2T₃.
- They fold into one double sum:

  Σ_{a+b+c=D} (R[a] + [a=b])·(R[b] + 2[b=c])·R[c] = T₁ + 3T₂ + 2T₃.

  Expanding, the [a=b] term gives Σ_{2b+c=D} R[b]R[c] = T₂, the 2[b=c] term
  gives 2·Σ_{a+2c=D} R[a]R[c] = 2T₂, and the product of the two indicators
  gives 2T₃. (Weights α, β on the two indicators give T₁ + (α+β)T₂ + αβT₃,
  so 1 and 2 are the only choice.)
- When a(n) is printed the list holds `n` entries, R[0] … R[n−1], which is
  exactly what a(n+2) needs: D = n−1, so c = D−a−b is the index `~a-b`
  counted from the end, `range(n-a)` keeps c ≥ 0, and b = c reads
  `n+~a==b+b`. With `R=[n:=1]` the first pass prints a(3) = 6/6 = 1, which
  starts the sequence at its offset.

**Notes**

- Exact integer arithmetic, so the program is right for every n; both
  divisions are exact, since the recurrence and the cycle index give
  integers.
- The double sum costs O(n²) big-integer products per term and the
  recurrence O(n log n): about 680 terms in 60 s here, so the bar is 500
  terms in 60 s (the b-file has 998).
- a(n) grows like 2.9558ⁿ (Kotesovec), so its decimal form passes Python's
  4300-digit int-to-str limit only near n = 9100.
- Writing the three terms out with dot products (`map(int.__mul__,…)` over
  `R[n+~a::-1]` and `R[::-2]`, plus `R[n//3]*(n%3==1)`) costs about 120
  bytes for the print alone, against 83 here. Packing r(x), r(x²), r(x³)
  into big integers is longer still, because each needs its own
  `enumerate` pass over the list.
- Loops over a and u = a+b (`for u in range(a,n)`, with c read as `R[~u]`)
  tie at 167, as does any choice of which factor carries the weight 2.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 167 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000226), CC BY-SA 4.0.
