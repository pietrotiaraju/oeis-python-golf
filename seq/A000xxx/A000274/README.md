# A000274

> Number of permutations of length n with 2 consecutive ascending pairs.
> — [OEIS A000274](https://oeis.org/A000274)

Offset 1: 0, 0, 1, 3, 18, 110, 795, 6489, 59332, 600732, …

### Python 3 — 40 bytes

```python
d=m=0
while[print(m*(d:=d*m^1)>>1)]:m+=1
```

**How it works**

- a(n) = m·D(m)/2 with m = n−1, where D(m) is the number of derangements
  (A000166). Proof: by Riordan, the permutations of [n] with exactly k
  successions number C(n−1,k)·A000255(n−1−k), and A000255 has e.g.f.
  e^(−x)/(1−x)². For k = 2 the e.g.f. in m = n−1 is
  (x²/2)·e^(−x)/(1−x)², and that is x·D′(x)/2 for D(x) = e^(−x)/(1−x),
  since D′(x) = x·e^(−x)/(1−x)². Multiplying an e.g.f. by x after taking
  the derivative turns its coefficients into m·D(m), so a(n) = m·D(m)/2.
  A brute-force count of successions matches for n ≤ 9.
- `d` follows D(m) with the A000166 update D(m) = m·D(m−1) xor 1 (m·D(m−1)
  has the parity of m, so xor 1 is +1 for even m and −1 for odd m).
- The loop starts one step early: with `d=m=0`, the first update gives
  0·0 xor 1 = 1 = D(0) whatever `d` held, so both start at 0 in one
  assignment. The update sits inside `print` as a walrus, and the body
  only counts.
- m·D(m) is always even (D(m) is even for odd m), so `>>1` halves it
  exactly. `*` binds tighter than `>>`, which binds tighter than `^`.

**Notes**

- Exact integer arithmetic, correct for every n. The whole b-file (150
  terms) prints at once; the program stops after a(1558), when the next
  term passes the 4300-digit int-to-str limit of Python 3.11+. The bar is
  the whole b-file in 60 s.
- `d=1;m=0` / `while[print(m*d>>1)]:m+=1;d=d*m^1` is 41 bytes. Counting
  m in steps of 2 to absorb the halving makes the update `d*k>>1^1` and the
  print `k*d>>2`, which is longer.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 40 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000274), CC BY-SA 4.0.
