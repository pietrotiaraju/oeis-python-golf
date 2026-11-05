# A000101

> Record gaps between primes (upper end) (compare A002386, which gives lower
> ends of these gaps).
> — [OEIS A000101](https://oeis.org/A000101)

Offset 1: 3, 5, 11, 29, 97, 127, 541, 907, 1151, 1361, 9587, 15727, 19661, …

### Python 3 — 67 bytes

```python
P=k=1;c=g=0
while k:=k+1:g<P%k*c!=[print(k),g:=c];c-=P%k*c-1;P*=k*k
```

**How it works**

- Wilson's theorem, squared: (k − 1)!² mod k is 1 when k is prime and 0 when
  it is not (4 included: 3!² = 36). `P` is kept equal to (k − 1)!², so `P%k`
  is a 0/1 prime flag, as in the squared variant noted on
  [A000040](../A000040/).
- `while k:=k+1:` moves the increment into the condition, so the first k
  tested is 2 with P = 1!² = 1, and `P*=k*k` at the end turns (k − 1)!² into
  k!².
- `c` is k − p, the distance back to the last prime p below k, and `g` is the
  record gap so far. `P%k*c` is the gap ending at k when k is prime and 0
  otherwise. `c-=P%k*c-1` adds 1, or resets `c` to 1 after a prime.
- `g<P%k*c!=[print(k),g:=c]` is `g<P%k*c and P%k*c!=[…]`: only for a new
  record is the list built, which prints k and stores the gap. An int never
  equals a list, so the second test is only there to run it.
- At k = 2, `c` is still 0, so 2 is not printed, and the gap 1 up to 3 then
  beats g = 0: the first term is 3, as on the OEIS page.

**Notes**

- P has about 2k log₂ k bits, so the cost grows like k² log k: the 14 terms up
  to 31 469 print in 2–5 s, but the next one, 156 007, would take minutes. The
  bar is 14 terms in 60 s. The b-file has 85 terms, up to about 10²⁰.
- The plain factorial, with the flag `(~P%k<1)` and `P*=k`, is 75 bytes: the
  flag is used twice. It is about twice as fast, but 156 007 still takes a
  minute or more, so it would not clear a 15-term bar either.
- Trial division up to `isqrt(k)`, with the gap kept as `k-p`, is 116 bytes
  and prints 22 terms (up to 4 652 507) in 60 s.
- Keeping the last prime p instead of `c` needs `(k-p)` twice and an update
  `p+=P%k*(k-p)`: longer. Naming the flag product with `(d:=P%k*c)` and
  updating with `c+=1-d` ties.
- With the test in the condition, `while[g<P%k*c!=[print(k),g:=c]]:` and
  `k+=1` in the body, k has to start at 2, which costs 1 byte more.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-05 | Python 3 | 67 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000101), CC BY-SA 4.0.
