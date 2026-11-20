# A001923

> a(n) = Sum_{k=1..n} k^k.
> — [OEIS A001923](https://oeis.org/A001923)

Offset 0: 0, 1, 5, 32, 288, 3413, 50069, 873612, 17650828, 405071317, 10405071317, …

### Python 3 — 34 bytes

```python
s=n=0
while[print(s)]:n+=1;s+=n**n
```

**How it works**

- `s` is the running sum, a(0) = 0 being the empty sum; each pass prints it,
  then moves `n` to the next k and adds kᵏ.
- Exact integer arithmetic, so the program is right for every n.

**Notes**

- With the walrus, `s+=(n:=n+1)**n`, it is 36 bytes; adding first and
  printing a walrus needs the start s = −1, 37.
- Python's 4300-digit int-to-str limit stops the program at about n = 1370
  (nⁿ has n·log₁₀ n digits).
- The b-file has 101 terms (n = 0 to 100); the bar is the whole b-file in
  60 s, which prints instantly.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-19 | Python 3 | 34 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A001923), CC BY-SA 4.0.
