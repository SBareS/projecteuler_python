"""
Connectedness of a Network

Here are the records from a busy telephone system with one million users:

RecNr   Caller  Called
1       200007  100053
2       600183  500439
3       600863  701497
...     ...     ...

The telephone number of the caller and the called number in record are 
$Caller(n)=S_{2n-1}$ and $Called(n)=S_{2n}$ where S_{1,2,3,...} come from the
"Lagged Fibonacci Generator":

For 1 <= k <= 55, S_k = [100003 - 200003k + 300007k^3] (mod 1000000).
For 56 <= k, S_k = [S_{k-24} + S_{k-55}] (mod 1000000).

If Caller(n) = Called(n) then the user is assumed to have misdialled and the 
call fails; otherwise the call is successful.

From the start of the records, we say that any pair of users X and Y are 
friends if X calls Y or vice-versa. Similarly, X is a friend of a friend of Z 
if X is a friend of Y and Y is a friend of Z; and so on for longer chains.

The Prime Minister's phone number is 524287. After how many successful calls, 
not counting misdials, will of the users (including the PM) be a friend, or a
friend of a friend etc., of the Prime Minister?
"""

from itertools import islice
import operator

from unionfind import UnionFind

def the_seq():
    q = [(100003 - 200003*k + 300007*k**3) % 1_000_000 for k in range(1, 56)]
    yield from q
    while True:
        x = (q[-24] + q[-55]) % 1_000_000
        yield x
        q.append(x)
        if len(q) > 100:
            q = q[-55:]

uf = UnionFind(operator.add)
for i in range(1_000_000):
    uf.add_node(i, 1)

result = 0
it = the_seq()
while uf.get_data(524287) < 990_000:
    while (caller := next(it)) == (called := next(it)):
        pass
    uf.union(caller, called)
    result += 1

print(result)
correct_answer = "2325629"