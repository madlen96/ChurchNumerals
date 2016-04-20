
Liczebniki Churcha

Liczby naturalne możemy reprezentować za pomocą tzw. numerałów Churcha.
Liczbę naturalną n przedstawimy jako funkcję na funkcjach, która składa swój
argument ze sobą n razy. Numerał n to funkcja, która przyjmuje jako
argument pewną funkcję f, w wyniku czego daje nową funkcję
g będącą n-krotnym złożeniem f, czyli g(x) = f^n(x).

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
    
Procedura ta nie robi nic innego jak "dodaje" jeszcze jedno wywołanie funkcji do pewnej liczby, przez co staje się ona
liczbą o jeden większą. W zbiorze liczb naturalnych Churcha definiuje się operacje arytmetyczne takie jak dodawanie, mnożenie, potęgowanie, które nazywamy arytmetyką w rachunku lambda. Dzięki zdefiniowaniu funkcji "successor", możemy je teraz określić a później przetestować ich działanie za pomocą programu.

Aby dodać dwie liczby naturalne Churcha m i n należy m-krotnie zaaplikować funkcję następnika do liczby n (lub na odwrót, dodawanie jest przemienne):

    def add(m,n):
        return lambda f: lambda x: m(f)(n(f)(x))
        
Mnożenie w rachunku lambda zdefiniowane jest następująco:  

     def mul(m,n):
        return lambda f: lambda x: m(n(f))(x)
        
Działa następująco: n razy dodajemy m w funkcji, co łatwo sobie wyobrazić znając zasady zwykłego mnożenia.

A potęgowanie:

    def exp(m,n):
        return lambda f: lambda x: (n)(m)(f)(x)

tzn. n-krotnie mnożymy przez liczbę a.

Nadszedł czas na odrobinę praktyki - przetestowanie, jak działają liczebniki Churcha.
