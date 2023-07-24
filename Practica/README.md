# AChurch

AChurch és un petit intèrpret de λ-càlcul corresponent 
a la pràctica de GEI-LP (edició 2022-2023 Q2).

## Installation

Use the package manager pip to install python-telegram-bot and pydot.

```bash
pip install python-telegram-bot
pip install pydot
```
Also you need too install graphviz with "sudo apt install graphviz".

```bash
sudo apt install graphviz
```

## Usage

### Intèrpret AChurch a la terminal

```bash
python3 achurch.py 
```

Es poden avaluar termes de λ-càlcul, en el procés d’avaluació es mostrarant 
quines regles (β-reduccions i α-conversions) es van aplicant fins assolir l’objectiu.
Les variables es codifiquen amb una única lletra minúscula per motius estètics. 
Així, el terme `xy` correspon a l’aplicació del terme xsobre el terme `y`.
Per tant, només poden haver-hi 26 variables.

```bash
? (λyx.y)x
Arbre:
((λy.(λx.y))x)
α-conversió: x → z
(λy.(λx.y)) → (λy.(λz.y))
β-reducció:
((λy.(λz.y))x) → (λz.x)
Resultat:
(λz.x)
```

Existeix un màxim de reduccions per evitar els casos en que les crides recursives no acaben.

```bash
? (λx.(xx))(λx.(xx))
Arbre:
((λx.(xx))(λx.(xx)))
β-reducció:
((λx.(xx))(λx.(xx))) → ((λx.(xx))(λx.(xx)))
β-reducció:
((λx.(xx))(λx.(xx))) → ((λx.(xx))(λx.(xx)))
β-reducció:
((λx.(xx))(λx.(xx))) → ((λx.(xx))(λx.(xx)))
...
Resultat:
Nothing
```

Es permet definir i usar macros (o combinadors) dins l’intèrpret.
Els noms de les macros han de començar per una lletra majúscula i poden contenir majúscules i xifres. 
La forma de definir les macros es fa mitjançant els caràcters ≡ o = amb notació infixa.

```bash
? N2≡λs.λz.s(s(z))
N2 ≡ (λs.(λz.(s(sz))))
? SUCC≡λa.λb.λc.b(abc)
N2 ≡ (λs.(λz.(s(sz))))
SUCC ≡ (λa.(λb.(λc.(b((ab)c)))))
? SUCC N2
Arbre:
((λa.(λb.(λc.(b((ab)c)))))(λs.(λz.(s(sz)))))
β-reducció:
((λa.(λb.(λc.(b((ab)c)))))(λs.(λz.(s(sz))))) → (λb.(λc.(b(((λs.(λz.(s(sz))))b)c))))
β-reducció:
((λs.(λz.(s(sz))))b) → (λz.(b(bz)))
β-reducció:
((λz.(b(bz)))c) → (b(bc))
Resultat:
(λb.(λc.(b(b(bc)))))
```

També es poden definir macros amb notació infixa.
En aquests casos els noms seran /,*,+,-.

```bash
? N2≡λs.λz.s(s(z))
N2 ≡ (λs.(λz.(s(sz))))
? N3≡λs.λz.s(s(s(z)))
N2 ≡ (λs.(λz.(s(sz))))
N3 ≡ (λs.(λz.(s(s(sz)))))
? +≡λp.λq.λx.λy.(px(qxy))
N2 ≡ (λs.(λz.(s(sz))))
N3 ≡ (λs.(λz.(s(s(sz)))))
+ ≡ (λp.(λq.(λx.(λy.((px)((qx)y))))))
? N2+N3
Arbre:
(((λp.(λq.(λx.(λy.((px)((qx)y))))))(λs.(λz.(s(sz)))))(λs.(λz.(s(s(sz))))))
β-reducció:
((λp.(λq.(λx.(λy.((px)((qx)y))))))(λs.(λz.(s(sz))))) → (λq.(λx.(λy.(((λs.(λz.(s(sz))))x)((qx)y)))))
β-reducció:
((λq.(λx.(λy.(((λs.(λz.(s(sz))))x)((qx)y)))))(λs.(λz.(s(s(sz)))))) → (λx.(λy.(((λs.(λz.(s(sz))))x)(((λs.(λz.(s(s(sz)))))x)y))))
β-reducció:
((λs.(λz.(s(sz))))x) → (λz.(x(xz)))
β-reducció:
((λz.(x(xz)))(((λs.(λz.(s(s(sz)))))x)y)) → (x(x(((λs.(λz.(s(s(sz)))))x)y)))
β-reducció:
((λs.(λz.(s(s(sz)))))x) → (λz.(x(x(xz))))
β-reducció:
((λz.(x(x(xz))))y) → (x(x(xy)))
Resultat:
(λx.(λy.(x(x(x(x(xy)))))))
```

### Intèrpret AChurch a Telegram

Les dades del bot creat són les següents:
- Name: *AChurch*
- Username: *AChurchLambdaBot*
- Enllaç: *t.me/AChurchLambdaBot*

Per tal de posar el bot en marxa:

```bash
python3 telegram_bot.py
```

De la mateixa manera que l'interprèt de la terminal, el bot de Telegram,
avalua les expressions λ-càlcul i, a més, es representen gràficament els arbres
semàntics.

El bot conté les comandes: help, start, author i macros.

- /help: Mostra la llista de comandes.
- /start: Es presenta el bot i es fa una salutació a l'usuari.
- /author: Es mostra l'autor del bot i la data de creació
- /macros: Es mostra un llistat de les macros definides

## References

- README: https://www.makeareadme.com/
- Alonzo Church - Wikipedia: https://en.wikipedia.org/wiki/Alonzo_Church
- ANTLR en Python: https://gebakx.github.io/Python3/compiladors.html#1
- Fonaments: λ-càlcul: https://jpetit.jutge.org/lp/03-lambda-calcul.html
- Lambda calculus - Lambda Calculus: http://www-cs-students.stanford.edu/~blynn/lambda/
- Lambda-Calculus Evaluator: https://www.cl.cam.ac.uk/~rmk35/lambda_calculus/lambda_calculus.ht
- Lambda Calculus Interpreter: https://jacksongl.github.io/files/demo/lambda/index.htm
- python-telegram-bot: https://docs.python-telegram-bot.org/en/stable/
- pydot: https://github.com/pydot/pydot
