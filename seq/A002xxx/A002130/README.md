# A002130

> Generalized sum of divisors function.
> — [OEIS A002130](https://oeis.org/A002130)

Offset 3: 1, -1, 1, 3, -2, 1, -5, 23, -25, 27, -49, 74, …

### Python 3 — 136 bytes

```python
r=[1]
for n in r:r+=n+1,;n<3or print(sum((-1)**(u//i+(n-u)//j)*u//i*(n-u)//j for i in r for u in range(i,n,i)for j in r[i:]if(n-u)%j<1))
```

**How it works**

- The entry's g.f. is (t(1)² − t(2))/2 with t(i) = Σ_m x^(m·i)/(1+x^m)^(2i),
  that is Σ_{0<i<j} f_i·f_j with f_m = x^m/(1+x^m)²: the square of the
  sum minus the sum of the squares, halved. And
  x^m/(1+x^m)² = Σ_{d≥1} (−1)^(d+1)·d·x^(d·m), so a(n) is the sum of
  (−1)^(x+y)·x·y over sizes i < j and multiplicities x, y ≥ 1 with
  x·i + y·j = n (the signs (−1)^(x+1)(−1)^(y+1) multiply to (−1)^(x+y)).
- `r` is the list being looped over, and each pass appends n+1 to it, so
  the `for` never ends and r holds 1, …, n+1 (the loop of
  [A000203](../../A000xxx/A000203/)). u = x·i runs over the multiples of i
  below n, `r[i:]` over the sizes j > i, and `if(n-u)%j<1` keeps the j
  dividing n − u, so x = `u//i` and y = `(n-u)//j`. The product
  `(-1)**(…)*u//i*(n-u)//j` is evaluated left to right, and both floor
  divisions are exact.
- `n<3or print(…)` skips n = 1, 2: the offset is 3.

**Notes**

- Integer arithmetic only, so it is correct for every n.
- The b-file has the 55 terms of the entry (n = 3…57); the bar is all of
  them in 60 s, which takes a tenth of a second.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-20 | Python 3 | 136 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A002130), CC BY-SA 4.0.
