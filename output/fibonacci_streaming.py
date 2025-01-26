"""Kata - Fibonacci Streaming

completed at: 2025-01-19 20:02:45
by: Jakub Červinka

You're going to provide a needy programmer a utility method that generates an infinite amount of sequential fibonacci numbers.

~~~if:java
to do this return an `IntStream` starting with 1
~~~
~~~if:typescript
to do this return an `Iterator<BigInt> ` starting with 1
~~~
~~~if:javascript
to do this return an `Iterator<BigInt>` starting with 1
~~~
~~~if:python
to do this write a 'generator' starting with 1
~~~
~~~if:rust
to do this write a function returning an `Iterator<Item = BigUint>` starting with 1
~~~
~~~if:ocaml
to do this create an infinite sequence of big integers (from the `Z` module) with the `Seq` module
~~~
~~~if:lua
to do this write a function returning an iterator starting with 1
~~~
~~~if:scala
to do this write a function returning an `Iterator[BigInt]` starting with 1
~~~

A fibonacci sequence starts with two `1`s. Every element afterwards is the sum of the two previous elements. See:

    1, 1, 2, 3, 5, 8, 13, ..., 89, 144, 233, 377, ...

"""

def all_fibonacci_numbers():
    a, b = 1, 1
    while True:
        yield a
        b, a = a + b, b
