Trabalho Computacional: Geração e Observação de Variáveis Aleatórias
Geradores de Números Aleatórios

Um Gerador Congruencial Linear é um algoritmo que retorna uma sequência de
números pseudo-aleatórios que são calculados e gerados através de uma função
linear de trecho (função afim em certo intervalo).
- Método Congruencial Misto:
X0 = Semente (valor inicial)
Xn = aXn−1 + c modulo m; n ≥ 1
Onde:
c é o incremento
a é o multiplicador
X0 = termo inicial (seed)
m é o módulo que irá determinar o intervalo, no qual os números poderão
aparecer.

Questão 01:
Para realizar a questão 01, iniciaremos entrando com os valores de a, c, m e seed,
e declarando os vetores n e v, que vão percorrer nossa função dentro do loop for,
de modo que percorra as 10000 amostras. Com base na formula do método
congruencial misto, a transformaremos de forma que funcione dentro da sintaxe
do python (linguagem que usei para realizar o trabalho). Depois foi usada a
função “.append” do python, para adicionar os valores X e r dentro dos vetores
V e n. Como mostrado abaixo:

v = [ ]
n= [ ]

a = 5 #inicio
c = 8 #final
m = 2**30
seed = 30

for i in range(10000):
seed = (a*seed+c)%m
r = seed/m
X = a+(c-a)*r
v.append(X)
n.append(r)

Para o cálculo da média e da variância, utilizaremos como base as formulas
abaixo:

μ =
1
N
xi
N

i=1

σ2 =
1
N
(xi − μ)2
N

i=1

Em jupyter:
Med = (max(v) - min(v))/2 + min(v)
Sig2 = ((max(v) - min(v))**2)/12

Questão 02:
Para realizar a questão 02, iniciaremos entrando com os valores de a, c, m, seed e
h (lambda), e declarando os vetores n e v, que vão percorrer nossa função dentro
do loop for, de modo que percorra as 10000 amostras. Com base na formula do
método congruencial misto e na formula da Função de Distribuição Acumulada
Inversa, a transformaremos de forma que funcione dentro da sintaxe do python.
Depois foi usada a função “.append” para adicionar os valores X e r dentro dos
vetores V e n e a função “.sort” para ordenar os valores, nesse caso se for falso
inverte. Como mostrado abaixo:

for i in range(10000):
seed = (a * seed + c) % m
r = seed / m
w = math.log(1-r)/6*(-1)

v.append(w)
n.append(r)
v.sort(reverse=False)
n.sort(reverse=False)

Com a fórmula da Função de Distribuição Acumulada Inversa, mostrada abaixo:

Fx(x) = λe
−λx

Utilizaremos a seguinte fórmula equivalente em código, utilizando variáveis
de tipo float, para obter uma maior precisão:
U = float('%g' % max(v))
O = float('%g' % max(n))
lc = (-1)*math.log(1-O)/U

Questão 03:
Para realizar a questão 03, iniciaremos entrando com os valores de alpha, e
declarando os vetores n e v, que vão percorrer nossa função dentro do loop for,
de modo que percorra as 10000 amostras. Com base na formula do método

congruencial misto e na formula da Distribuição de Cauchy, números pseudo-
aleatórios serão gerados através de uma uniforme. Para isso, foi usada a função

“random” que gera números pseudo-aleatórios em um intervalo de 0 a 1, e
posteriormente foi feito o mesmo processo das questões anteriores, com o uso de
“.append” para adicionar os valores X e r dentro dos vetores V e n e de“.sort”
para ordenar os valores, e inverte-los, se for falso. Como mostrado abaixo:
v = [ ]
n = [ ]
alpha = 4
pi = math.pi
for i in range(10000):
x = random.uniform(0, 1)
w = 4*math.tan(x*pi - pi/2)

v.append(w)
v.sort(reverse=False)
n.append(x)
n.sort(reverse=False)

Questão 04:
Para realizar a questão 04, iniciaremos entrando com os valores de Mi e sigma
(media e variância, respectivamente). Com base na formula do método

congruencial misto e na formula da Distribuição de Gaussiana, números pseudo-
aleatórios serão gerados através de uma uniforme em 10000 amostras. Para isso,

foi usada a função “np.random.normal(Mi, sigma, 10000)” que gera números
pseudo-aleatórios a partir da média e da variância. Como mostrado abaixo:
Mi, sigma = 5, 2
s = np.random.normal(Mi, sigma, 10000)

Para plotar o histograma foi usada a função “numpy.histogram”:

#Histograma
count, bins, ignored = plt.hist(s, 20, density=True)

#Curva
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
np.exp( - (bins - Mi)**2 / (2 * sigma**2) ))
plt.show()

Resultados e Gráficos
Questão 01:
Com Px(x) = 1/3
Foi obtido uma média teórica igual à 6.5 e a variância igual à 0.75
Os valores estão bem próximos dos ideais, porém é muito difícil chegar
exatamente ao teórico, principalmente por conta da quantidade de amostras.
Média gerada: 6.49997522868216
Variância gerada: 0.7499747874471545

Questão 02:

Com Média = 1/λ e a com variância = 1/λ2
Foi obtido uma média teórica igual à 0,1666... e a variância igual à 0.027
Os valores estão bem próximos dos ideais, porém é muito difícil chegar
exatamente ao teórico, principalmente por conta da quantidade de amostras.
Média gerada: 0.16646193108402052
Variância gerada: 0.02770957450022119
