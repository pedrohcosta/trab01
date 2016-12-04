# TRABALHO 01
Trabalho BD1

#Sumário

###1	COMPONENTES<br>
Pedro Henrique<br>
Romildo Costa<br>

###2	INTRODUÇÃO E MOTIVAÇAO<br>
O objetivo do nosso sistema e realizar crawling o site de classificados (OLX, ZAP e etc) para extração de informações de imóveis (bairro, município, valor e etc.) e veículos (bairro, município, valor, modelo, ano e etc.) disponibilizando para usuário varios filtro de informações históricas com maior facilidade.<br>
Além dos filtros com as principais informações, usuário também poderá visualizar relatórios e gráficos sobre valorizações/desvalorizações, valores mínimos máximos e médios, realizar comparações de valores de imóveis e veículo. <br>

###3	MINI-MUNDO<br>
Descrever o mini-mundo. Não deve ser maior do que 30 linhas <br>

###4	RASCUNHOS BÁSICOS DA INTERFACE (MOCKUPS)<br>
neste ponto a codificação não e necessária, somente as ideias de telas devem ser criadas, o princípio aqui é pensar na criação da interface para identificar possíveis informações a serem armazenadas ou descartadas <br>

Sugestão: https://balsamiq.com/products/mockups/<br>

![Alt text](https://github.com/discipbd1/trab01/blob/master/balsamiq.png?raw=true "Title")


###5	MODELO CONCEITUAL<br>
    5.1 NOTACAO ENTIDADE RELACIONAMENTO
![Alt text](https://github.com/pedrohcosta/trab01/blob/master/imagens/ModeloConteitual.jpg?raw=true "Modelo Conceitual")
    
    5.2 NOTACAO UML (Caso esteja fazendo a disciplina de analise)

####5.1 Validação do Modelo Conceitual
    [Grupo01]: [Edson Wevertom]
    [Grupo02]: [Nomes dos que participaram na avaliação]

####5.2 DECISÕES DE PROJETO
    [atributo]: [descrição da decisão]
    
    EXEMPLO:
    a) Campo endereço: em nosso projeto optamos por um campo multivalorado e composto, pois a empresa 
    pode possuir para cada departamento mais de uma localização... 
    b) justifique!

####5.3 DESCRIÇÃO DOS DADOS 
    bairro: Tabela que contém os nomes dos bairros dos classificados.
        idbairro: chave primária da tabela bairro.
        nome: campo que armazena o nome do bairro.

    cambio: Tabela que contém os nomes dos cambios dos veiculo.
        idcambio: chave primária da tabela cambio.
        nome: campo que armazena o nome do cambio.

    caracteristica: Tabela que contém os nomes dos caracteristicas dos imovel.
        idcaracteristica: chave primária da tabela caracteristica.
        nome: campo que armazena o nome da caracteristica.

    categoria: Tabela que contém os nomes dos categoria dos classificados.
        idcategoria: chave primária da tabela categoria.
        nome: campo que armazena o nome da categoria.

    classificado: Tabela que contém os atributos em comum entre todas as entidades (imovel/veiculo).
        idclassificado: chave primária da tabela classificado.
        data: campo que armazena o data do classificado.
        titulo: campo que armazena o titulo do classificado.
        descricao: campo que armazena o descricao do classificado.
        valor: campo que armazena o valor do classificado.
        cep: campo que armazena o cep do classificado.
        latitude: campo que armazena o latitude do classificado.
        longitude: campo que armazena o longitude do classificado.
        codigo_anuncio: campo que armazena o codigo_anuncio do classificado.
        idbairro: chave estrangeira da tabela bairro.
        idmunicipio: chave estrangeira da tabela municipio.

    combustivel: Tabela que contém os nomes dos tipos de combustivel dos veiculos.
        idcombustivel: chave primária da tabela combustivel.
        nome: campo que armazena o nome do combustivel.

    imovel: Tabela que contém as informações do imovel.
        idimovel: chave primária da tabela imovel.
        idclassificado: chave estrangeira da tabela classificado.
        idtipo: chave estrangeira da tabela tipo.
        area_construida: campo que armazena o area construida do imovel.
        area_util: campo que armazena o area util do imovel.
        vagas_garagem: campo que armazena o quantidad de vagas de garagem do imovel.
        valor_condominio: campo que armazena o valor do condominio do imovel.
        quantidade_quartos: campo que armazena a quantidade de quartos do imovel.
        iptu: campo que armazena o valor do iptu do imovel.

    imovel_caracteristica: Tabela que contém as informações das caracteristicas do imovel.
        idimovel: chave estrangeira da tabela imovel.
        idcaracteristica: chave estrangeira da tabela caracteristica.

    veiculo_opcional: Tabela que contém as informações dos opcionais do veiculo.
        idopcional: chave estrangeira da tabela opcional.
        idveiculo: chave estrangeira da tabela opcional.

    marca: Tabela que contém os nomes dos tipos de marcas dos veiculos.
        idmarca: chave primária da tabela marca.
        nome: campo que armazena o nome da marca.

    modelo: Tabela que contém os nomes dos tipos de modelos dos veiculos.
        idmodelo: chave primária da tabela modelo.
        nome: campo que armazena o nome do modelo.

    municipio: Tabela que contém os nomes dos municipio dos classificados.
        idmunicipio: chave primária da tabela municipio.
        nome: campo que armazena o nome do municipio.

    tipo: Tabela que contém os nomes dos tipos de imoveis.
        idtipo: chave primária da tabela tipo.
        nome: campo que armazena o nome do tipo.
        idcategoria: chave estrangeira da tabela categoria.

    opcinal: Tabela que contém os nomes dos opcionais dos veiculos.
        idopcinal: chave primária da tabela opcinal.
        nome: campo que armazena o nome da opcinal.

    veiculo: Tabela que contém as informações do veiculo.
        idveiculo: chave primária da tabela veiculo.
        idclassificado: chave estrangeira da tabela classificado.
        idcategoria: chave estrangeira da tabela categoria.
        idmodelo: chave estrangeira da tabela modelo.
        idcambio: chave estrangeira da tabela cambio.
        idcombustivel: chave estrangeira da tabela combustivel.
        idmarca: chave estrangeira da tabela marca.
        ano: campo que armazena o ano do veiculo.	
        cilindrada: campo que armazena o cilindrada do veiculo.	
        quilomeragem: campo que armazena o quilometragem do veiculo.	
        quantidade_porta: campo que armazena o quantidade_porta do veiculo.	

###6	MODELO LÓGICO<br>
![Alt text](https://github.com/pedrohcosta/trab01/blob/master/imagens/ModeloLogico.jpg?raw=true "Modelo Conceitual")


###7	MODELO FÍSICO<br>



        Entrega até este ponto em 25/10/2016

###8	INSERT APLICADO NAS TABELAS DO BANCO DE DADOS<br>
####8.1 DETALHAMENTO DAS INFORMAÇÕES
        Detalhamento sobre as informações e processo de obtenção ou geração dos dados.
        Referenciar todas as fontes referentes a :
        a) obtenção dos dados
        b) obtenção de códigos reutilizados
        c) fontes de estudo para desenvolvimento do projeto


####8.2 INCLUSÃO DO SCRIPT PARA CRIAÇÃO DE TABELA E INSERÇÃO DOS DADOS
        a) inclusão das instruções para criação das tabelas e estruturas de amazenamento do BD
        b) inclusão das instruções de inserção dos dados nas referidas tabelas
        c) inclusão das instruções para execução de outros procedimentos necessários


        Entrega até este ponto em 01/11/2016


###9	TABELAS E PRINCIPAIS CONSULTAS<br>
####9.1	CONSULTAS DAS TABELAS COM TODOS OS DADOS INSERIDOS (Todas) <br>
        Entrega até este ponto em 08/11/2016
####9.2	CONSULTAS DAS TABELAS COM FILTROS WHERE (Mínimo 3)<br>
####9.3	CONSULTAS QUE USAM OPERADORES LÓGICOS, ARITMÉTICOS E CAMPOS RENOMEADOS (Mínimo 2)<br>
####9.4	CONSULTAS QUE USAM OPERADORES LIKE (Mínimo 3) <br>
####9.5	ATUALIZAÇÃO E EXCLUSÃO DE DADOS (Mínimo 6)<br>
####9.6	CONSULTAS COM JUNÇÃO E ORDENAÇÃO (Todas Junções)<br>
        Entrega até este ponto em 22/11/2016
####9.7	CONSULTAS COM GROUP BY (Mínimo 5)<br>
####9.8	CONSULTAS COM LEFT E RIGHT JOIN (Mínimo 4)<br>
####9.9	CONSULTAS COM SELF JOIN E VIEW (Todas Possíveis)<br>
####9.10	SUBCONSULTAS (Mínimo 3)<br>
        Entrega até este ponto em 29/11/2016
###10	ATUALIZAÇÃO DA DOCUMENTAÇÃO DOS SLIDES PARA APRESENTAÇAO FINAL (Mínimo 6 e Máximo 10)<br>
###11	DIFICULDADES ENCONTRADAS PELO GRUPO<br>
###12  FORMATACAO NO GIT: https://help.github.com/articles/basic-writing-and-formatting-syntax/

###OBSERVAÇÕES IMPORTANTES

#### Em tese todos os arquivos do trabalho devem ser compartilhados no git 
1. Caso existam arquivos com conteúdos sigilosos, comunicar o professor que definirá em conjunto com o grupo a melhor forma de armazenamento do arquivo.

#### Todos os grupos deverão fazer Fork deste repositório e dar permissões administrativas ao usuário deste GIT, para acompanhamento do trabalho.

#### Os usuários criados no GIT devem possuir o nome de identificação do aluno (não serão aceitos nomes como Eu123, meuprojeto, pro456, etc). Em caso de dúvida comunicar o professor.



