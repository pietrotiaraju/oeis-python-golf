# A000472

> a(n) = a(n-1)^2 + (a(n-2) + 1)*(a(n-1) - a(n-2)^2).
> — [OEIS A000472](https://oeis.org/A000472)

Offset 1: 2, 5, 28, 802, 643726, 414383582242, 171713753231982206218246, 29485613049014079571725771288849499850026859242, 869401376876189366008603664962520703088459987798626788985159595026678611496977754082506135886, 755858754114213857656603113420675810884838006478829986130891722713470138443059286330596770611262539256240920756092672154727041680815771409333728105993616009678903886154302740105437684242, …

### Python 3 — 41 bytes

```python
a=2;d=1
while[print(a)]:a,d=a*a+d,d*(a+1)
```

**How it works**

Let d=a(n+1)-a(n)². The defining recurrence says that the next
difference is (a(n)+1)*d. Initially a(1)=2 and d=5-2²=1.
A simultaneous assignment therefore advances both a and d using
only the old state, avoiding a separate copy of the preceding term.

**Notes**

- The program uses exact integer arithmetic and the standard library only.
- The verification bar is 14 terms in 60 s; the official b-file contains 14 terms.
- Python 3.11+ eventually reaches its default 4300-digit integer-to-string limit; that interpreter limit is not counted as a correctness failure.

## History

| Date | Category | Bytes | Note |
|---|---|---|---|
| 2026-11-06 | Python 3 | 41 | first entry |

---
Sequence name and terms from [The On-Line Encyclopedia of Integer
Sequences](https://oeis.org/A000472), CC BY-SA 4.0.
