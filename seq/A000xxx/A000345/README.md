# A000345

> Number of partitions into non-integral powers.
> — [OEIS A000345](https://oeis.org/A000345)

Offset 3: 1, 5, 22, 71, 186, 427, 888, 1704, 3053, 5203, 8476, 13318, …

### Python 3 — 141 bytes

```python
n=3
while[N:=n*n,print(sum((q:=(N+z-x-y)**2-4*x*y-4*N*z)*abs(q)>=64*N*x*y*z for z in range(N)for y in range(z+1)for x in range(1,y+1)))]:n+=1
```

**How it works**

- As the OEIS comment puts it, a(n) counts the triples of integers
  1 ≤ x ≤ y ≤ z with √x + √y + √z ≤ n: Agarwala and Auluck's partitions
  of n into three parts k^(1/2), counted with ≤.
- The program tries every triple with z < n² (enough, since √z ≤ n − 2)
  and decides √x + √y ≤ n − √z with integers only, by squaring twice:
  - n − √z > 0, so the inequality is x + y + 2√(xy) ≤ n² + z − 2n√z, that
    is 2√(xy) + 2n√z ≤ m with m = n² + z − x − y. Here m > 0 because
    x + y ≤ 2z < n² + z, so squaring is safe again:
  - 4xy + 4n²z + 8n√(xyz) ≤ m², that is 8n√(xyz) ≤ q with
    q = m² − 4xy − 4n²z, which holds exactly when q ≥ 0 and
    q² ≥ 64n²xyz. Since 64n²xyz > 0, both together are `q*abs(q)>=64*N*x*y*z`.
- `N:=n*n` in the list that `while` tests saves a byte over writing `n*n`
  four times.

**Notes**

- Round n tries about n⁶/6 triples, so the program prints about 19 terms in
  60 s of the 74 in the b-file (OEIS synthesizes it from the entry's
  terms). The bar is 15 terms in 60 s.
- The floor/ceiling recursion of [A000333](../A000333/) restricted to three
  parts is far faster (it only visits triples that fit) but about 30 bytes
  longer.
- `(q:=…)>0<=q*q-64*N*x*y*z` is the same length as the `abs` form.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 141 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000345), CC BY-SA 4.0.
