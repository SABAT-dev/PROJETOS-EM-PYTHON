## ASSESSMENT - AT (LÓGICA, COMPUTAÇÃO E ALGORITMOS)

​			:white_check_mark: Nesse projeto final (Assesment) da faculdade, eu tive **3 exercícios** de ***níveis intermediários*** e ***avançados*** em Python: :mortar_board: :computer: 

3. ------

   **Considere o argumento abaixo:** 

   > *Você já deve ter ouvido algum especialista dizer que as pessoas precisam dedicar, no máximo, 30% da sua renda mensal à moradia, 20% à educação e 15% ao transporte. Esses valores não devem ser totalmente desprezados, mas não podem funcionar como um norte para o orçamento doméstico de todas as famílias.*
   >
   > *Fonte: [BTG Pactual Digital](https://www.btgpactualdigital.com/blog/coluna-gustavo-cerbasi/orcamento-domestico#:~:text=Você já deve ter ouvido,doméstico de todas as famílias.)*

   * ***Crie um programa contendo uma função que, dados um valor de renda mensal total, gastos totais com moradia, gastos totais com educação e gastos totais com transporte, faça um diagnóstico da saúde financeira do usuário, com base nos valores percentuais acima expostos, informando qual é o percentual da renda mensal total comprometido por cada custo.*** 

     Se o gasto estiver dentro do percentual recomendado, informe ainda que:

     ```python
     Seus gastos estão dentro da margem recomendada.
     ```

   ​		Caso contrário, informe:

   ```python
   	Portanto, idealmente, o máximo de sua renda comprometida com {tipo} deveria ser de R$ {valor_max} 
   ```

   ​		Onde `tipo` deve ser moradia, educação ou transportes e `valor_max` deve ser o valor equivalente ao percentual máximo de gasto com esse tipo de custo.

   

------



4. **Seja a seguinte citação:**

   > *Os **juros compostos** são a força mais poderosa do universo e a maior invenção da humanidade, porque permitem uma confiável e sistemática acumulação de riqueza*

   ​		A frase, curiosamente, é de **Albert Einstein**, não de algum banqueiro ou gestor de fundos de capitais. 

   ​		Assim, suponha que você possui R$10.000 iniciais, consegue aportar R$1.000 por mês e obtém um rendimento de 0,54% ao mês. Por simplicidade, suponha que você faz o aporte após o rendimento no período acontecer.

   ​		No primeiro mês, terá R$10.000 + 0,54% deste valor = R$10.054,00. E, com o novo aporte, R$11.054,00.

   ​		No segundo mês, o valor inicial é de R$11.054,00. Ele rende 0,54%, totalizando R$11.113,69. Com o novo aporte, R$12.113,69, e assim sucessivamente.

   ​		Ao final de 120 meses, você terá o montante final de R$187.303,05.

   * ***Crie um programa que ponha a hipótese de Einstein à prova. Em uma função, receba, como entrada, um montante financeiro inicial, um percentual de rendimento por período, um valor de aporte para cada período e uma quantidade de períodos.***
   * ***Crie uma função que exiba um gráfico da evolução do valor acumulado, tendo como eixo das abscissas (horizontal) o número de períodos e, no eixo das ordenadas (vertical), o valor acumulado, em reais.***



------



5. **Considere a seguinte projeção de PIBs feita pelo FMI em 2014:**

   ***Maiores Economias do Mundo (PIB em trilhões de US$ - 2013-2020 – ordem decrescente de 2014)\****

   | **País**          | **2013** | **2014** | **2015** | **2016** | **2017** | **2018** | **2019** | **2020** |
   | ----------------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
   | **EUA**           | 16.76    | 17.41    | 18.12    | 18.95    | 19.86    | 20.76    | 21.61    | 22.48    |
   | **China**         | 9.46     | 10.38    | 11.21    | 11.96    | 12.86    | 13.87    | 14.96    | 16.15    |
   | **Japão**         | 4.92     | 4.61     | 4.21     | 4.34     | 4.48     | 4.59     | 4.75     | 4.93     |
   | **Alemanha**      | 3.73     | 3.86     | 3.41     | 3.51     | 3.64     | 3.78     | 3.93     | 4.1      |
   | **Reino Unido**   | 2.68     | 2.94     | 2.85     | 2.98     | 3.14     | 3.32     | 3.51     | 3.73     |
   | **França**        | 2.8      | 2.84     | 2.47     | 2.52     | 2.62     | 2.73     | 2.86     | 3.01     |
   | **Brasil**        | 2.39     | 2.35     | 1.9      | 1.92     | 2.03     | 2.13     | 2.24     | 2.35     |
   | **Itália**        | 2.13     | 2.14     | 1.84     | 1.88     | 1.94     | 2.01     | 2.08     | 2.17     |
   | **Índia**         | 1.87     | 2.05     | 2.3      | 2.51     | 2.75     | 3.01     | 3.31     | 3.64     |
   | **Rússia**        | 2.07     | 2.05     | 1.17     | 1.37     | 1.52     | 1.69     | 1.88     | 2.08     |
   | **Canadá**        | 1.83     | 1.78     | 1.61     | 1.68     | 1.76     | 1.85     | 1.94     | 2.04     |
   | **Coreia do Sul** | 1.3      | 1.41     | 1.43     | 1.51     | 1.61     | 1.73     | 1.86     | 2.01     |
   | **Espanha**       | 1.39     | 1.4      | 1.23     | 1.26     | 1.3      | 1.35     | 1.41     | 1.48     |
   | **México**        | 1.26     | 1.28     | 1.23     | 1.3      | 1.37     | 1.46     | 1.55     | 1.65     |
   | **Indonésia**     | 9.13     | 8.89     | 8.96     | 9.52     | 1.03     | 1.11     | 1.2      | 1.3      |

   *Dados de 2014; dados de 2015 em diante eram previsões do FMI em 2014. [Fonte](http://www.funag.gov.br/ipri/images/analise-pesquisa/tabelas/top15pib.pdf).

   Faça download dos dados em: 

   [Lista_Revisão_PIBs](https://docs.google.com/spreadsheets/d/17ph-3NHpGV3GH0R2_eErd-23K8gmpcGexQTxLDcjbDg/edit?usp=sharing) 

   [^No link acima]: Eu utilizei oMODELO 2 de PIB

   ​			(Use a função **Arquivo → Fazer o download → csv**, para baixar uma versão formatada dos dados para usá-los no projeto)

   * ***Desenvolva um programa contendo uma função que permita ao usuário solicitar o PIB de um país para um determinado ano.*** 

     * O programa solicita ao usuário o nome do país e o ano desejado.

     * Caso o país solicitado ou o ano não sejam válidos, o programa deve informar, na saída, a mensagem: 

       `País não disponível.` ou `Ano não disponível.`

       a depender do tipo de dado não encontrado. 

   * ***Desenvolva um programa contendo uma função que liste, por país, a estimativa de variação do PIB, em percentual, entre 2013 e 2020.***

   * ***Desenvolva uma função que, para um país, exiba o gráfico da evolução do PIB ao longo dos anos.***

   1. - A função deve receber, como entrada, o nome de um país, e exibir o gráfico para todo o período listado na tabela.
      - O gráfico deve conter os valores do PIB no eixo das ordenadas (vertical) e os anos no eixo das abscissas (horizontal)

