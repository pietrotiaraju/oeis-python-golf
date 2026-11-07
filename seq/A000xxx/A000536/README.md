# A000536

> Number of 3-line Latin rectangles.
> — [OEIS A000536](https://oeis.org/A000536)

Offset 4: 24, 240, 2520, 26880, 304080, 3671136, 47391120, 653463360, …

The name comes from Riordan's chapter on 3-line Latin rectangles (Riordan
1958, p. 210); the sequence is not the rectangle count itself (that is
[A000186](../A000186/)). The entry defines a(n) = K(n, 2) in the table
K(0,0) = 1, K(n,0) = n·K(n−1,0) + (−1)ⁿ, and for j ≥ 1
j·K(n,j) = n(n+1−2j)·K(n−1,j−1) + n(n−1)·K(n−2,j−1) (Sean A. Irvine).

### Python 3 — 57 bytes

```python
d=2;n=4
while[print(n*(-~-n*d+(n-2)*(d:=d*n^1))//2)]:n+=1
```

**How it works**

- **A closed form.** K(n,0) = D_n, the derangement numbers
  ([A000166](../A000166/)), with D_n = (n−1)(D_{n−1} + D_{n−2}). The
  table rule at j = 1 gives K(n,1) = n(n−1)(D_{n−1} + D_{n−2}) = n·D_n, and
  at j = 2
  2a(n) = n(n−1)(n−3)·D_{n−1} + n(n−1)(n−2)·D_{n−2}.
  Replacing (n−1)·D_{n−2} by D_n − (n−1)·D_{n−1} leaves
  a(n) = n·((n−2)·D_n − (n−1)·D_{n−1})/2.
- **One state.** `d` holds D_{n−1}. Python evaluates `-~-n*d`
  (= −(n−1)·D_{n−1}) first, then the walrus replaces `d` by D_n, so one
  variable serves both terms and is ready for the next n.
- **`d*n^1` is D_n.** D_n = n·D_{n−1} + (−1)ⁿ, and D_m ≡ m + 1 (mod 2)
  (induction: m·D_{m−1} + (−1)^m ≡ m² + 1 ≡ m + 1), so n·D_{n−1} has the
  parity of n. XOR with 1 adds 1 to an even number and subtracts 1 from an
  odd one, which is exactly + (−1)ⁿ. `*` binds tighter than `^`.
- **Exactness.** The bracket times n is 2a(n), so `//2` is exact.
- **The loop.** `d=2;n=4` is D_3 at the first n. `print` sits in the loop
  condition: it returns `None`, and `[None]` is a non-empty list, so the
  loop never ends (the [A000007](../A000007/) loop).

**Notes**

- Other versions that print the same terms: two derangement states and
  the j = 2 formula as it stands,
  `a,b,n=1,2,4` / `while[print(n*(n-1)*((n-3)*b+(n-2)*a)//2)]:a,b=b,(n-1)*(a+b);n+=1`:
  77 bytes.
- Exact integer arithmetic, so the program is right for every n.
- The b-file has 30 terms (up to a(33)); the bar is 15 terms in 60 s, and
  the whole b-file prints in well under a second.
- a(n) is about n·(n−3)·n!/(2e), so it passes 4300 digits (Python's int-to-str
  limit) at n = 1557: printing stops there, after about 1 s here.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 77 | first entry |
| 2026-11-07 | Python 3 | 57 | a(n) = n((n−2)D_n − (n−1)D_{n−1})/2 with one derangement state |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000536), CC BY-SA 4.0.
