# A000531

> From area of cyclic polygon of 2n + 1 sides.
> — [OEIS A000531](https://oeis.org/A000531)

Offset 1: 1, 7, 38, 187, 874, 3958, 17548, 76627, 330818, 1415650, …

a(n) = ((2n+1)·C(2n, n) − 4ⁿ)/2 (Simon Norton's formula on the entry). It
is also the total weight of the up-steps in all Dyck paths of semilength
n when each up-step is weighted by its position in the path: for n = 2,
UDUD gives 1 + 3 and UUDD gives 1 + 2, together 7.

### Python 3 — 48 bytes

```python
b=n=1
while[print((b:=4*b+2*b//n)-4**n>>1)]:n+=1
```

**How it works**

- **A running factorial quotient.** Put b(n) = (2n+1)·C(2n, n) =
  (2n+1)!/(n!)², so a(n) = (b(n) − 4ⁿ)/2. From the factorials,
  b(n)/b(n−1) = (2n+1)(2n)/n² = 4 + 2/n, so b(n) = 4b(n−1) + 2b(n−1)/n.
- **Exactness.** The division is exact: b(n−1) = (2n−1)!/((n−1)!)² =
  n·(2n−1)!/(n!(n−1)!) = n·C(2n−1, n), so 2b(n−1)/n = 2·C(2n−1, n).
  Python reads `2*b//n` as (2b)//n, which is that integer.
- **Halving.** For n ≥ 1, C(2n, n) = 2·C(2n−1, n) is even, so b(n) − 4ⁿ
  is even and `>>1` halves it exactly. `>>` binds looser than `-`, so
  `(b:=…)-4**n>>1` needs no more parentheses.
- **The loop.** `b=n=1` starts from b(0) = 1, and the walrus in the print
  turns it into b(n) before the subtraction. `print` sits in the loop
  condition: it returns `None`, and `[None]` is a non-empty list, so the
  loop never ends (the [A000007](../A000007/) loop).

**Notes**

- Other versions that print the same terms:
  - `b=6;n=1` / `while[print(b-4**n>>1)]:n+=1;b=4*b+2*b//n`: 49 bytes;
  - `b*(4*n+2)//n` in place of `4*b+2*b//n`: 50 bytes;
  - the closed form, `import math` /
    `while[print((2*n+1)*math.comb(2*n,n)-4**n>>1)]:n+=1`: 67 bytes (71
    with `from math import*`);
  - Michael Somos's recurrence n·a(n) = (8n − 2)a(n−1) − (16n − 8)a(n−2),
    `a,b=0,1;n=2` / `while[print(b)]:a,b=b,((8*n-2)*b-(16*n-8)*a)//n;n+=1`:
    64 bytes.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 100 terms (up to a(100)); the bar is the whole b-file in
  60 s, and it prints in well under a second.
- a(n) is close to 4ⁿ·√(n/π), so it passes 4300 digits (Python's int-to-str
  limit) at n = 7140: printing stops there, after about 2 s here.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 71 | first entry |
| 2026-11-07 | Python 3 | 48 | running (2n+1)!/n!² with an exact 2b/n step |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000531), CC BY-SA 4.0.
