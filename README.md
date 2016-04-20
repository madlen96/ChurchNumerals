
Liczebniki Churcha

Liczby naturalne możemy reprezentować za pomocą tzw. numerałów Churcha.
Liczbę naturalną n przedstawimy jako funkcję na funkcjach, która składa swój
argument ze sobą n razy. Numerał n to funkcja, która przyjmuje jako
argument pewną funkcję f: ( N->N ), w wyniku czego daje nową funkcję
g=n(f) : N->N, będącą n-krotnym złożeniem f, czyli g(x) = f^n(x).

W rachunku lambda odpowiednie numerały będą miały postać:
    0 = lambda f: lambda x: x
    1 = lambda f: lambda x: f(x)
    2 = lambda f: lambda x: f(f(x))
    3 = lambda f: lambda x: f(f(f(x)))
        .
        .
        .
    n = lambda f: lambda x: f^n x

  Po kilku pierwszych numerałach możemy dostrzec pewną analogię - f jest
  funkcją wywoływaną n-krotnie, a x jest parametrem. Z tego wynika, że mając
  daną definicję zera, każdą kolejną liczbę naturalną możemy opisać za pomocą
  funkcji następnika  - successor.

  successor = lambda n: lambda f: lambda x: (f)(n(f)(x))
    
    Dzięki zdefiniowaniu takiej funkcji, możemy teraz określić podstawowe
    operacje arytmetyczne na liczebnikach a później przetestować ich działanie za pomocą programu.
  
