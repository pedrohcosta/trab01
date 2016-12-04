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
![Alt text](https://github.com/pedrohcosta/trab01/blob/master/imagens/ModeloLogico.jpg?raw=true "Modelo Lógico")


###7	MODELO FÍSICO<br>


    CREATE TABLE classificado (
    data VARCHAR(10),
    longitude NUMERIC(10),
    codigo_anuncio VARCHAR(20),
    cep VARCHAR(10),
    valor NUMERIC(10),
    descricao VARCHAR(255),
    latitude NUMERIC(10),
    idclassificado SERIAL PRIMARY KEY,
    titulo VARCHAR(200),
    idbairro INTEGER,
    idmunicipio INTEGER
    )

    CREATE TABLE municipio (
    idmunicipio SERIAL PRIMARY KEY,
    nome VARCHAR(100)
    )

    CREATE TABLE bairro (
    idbairro SERIAL PRIMARY KEY,
    nome VARCHAR(100)
    )

    CREATE TABLE tipo (
    nome VARCHAR(100),
    idtipo SERIAL PRIMARY KEY,
    idcategoria INTEGER
    )

    CREATE TABLE imovel_caracteristica (
    idcaracteristica INTEGER,
    idimovel INTEGER
    )

    CREATE TABLE caracteristica (
    idcaracteristica SERIAL PRIMARY KEY,
    nome VARCHAR(100)
    )

    CREATE TABLE imovel (
    vagas_garagem INTEGER,
    idimovel SERIAL PRIMARY KEY,
    iptu NUMERIC(10),
    area_construida NUMERIC(10),
    valor_condominio NUMERIC(10),
    quantidade_quartos INTEGER,
    area_util DECIMAL(10),
    oferta VARCHAR(10),
    idclassificado INTEGER,
    idtipo INTEGER,
    FOREIGN KEY(idclassificado) REFERENCES classificado (idclassificado),
    FOREIGN KEY(idtipo) REFERENCES tipo (idtipo)
    )

    CREATE TABLE opcional (
    idopcional SERIAL PRIMARY KEY,
    nome VARCHAR(100)
    )

    CREATE TABLE veiculo_opcional (
    idopcional INTEGER,
    idveiculo INTEGER,
    FOREIGN KEY(idopcional) REFERENCES opcional (idopcional)
    )

    CREATE TABLE marca (
    nome VARCHAR(100),
    idmarca SERIAL PRIMARY KEY
    )

    CREATE TABLE modelo (
    idmodelo SERIAL PRIMARY KEY,
    nome VARCHAR(100)
    )

    CREATE TABLE combustivel (
    nome VARCHAR(100),
    idcombustivel SERIAL PRIMARY KEY
    )

    CREATE TABLE cambio (
    idcambio SERIAL PRIMARY KEY,
    nome VARCHAR(100)
    )

    CREATE TABLE categoria (
    idcategoria SERIAL PRIMARY KEY,
    nome VARCHAR(100)
    )

    CREATE TABLE veiculo (
    quilometragem NUMERIC(10),
    idveiculo SERIAL PRIMARY KEY,
    cilindrada NUMERIC(10),
    ano INTEGER,
    quantidade_porta INTEGER,
    idclassificado INTEGER,
    idmodelo INTEGER,
    idmarca INTEGER,
    idcombustivel INTEGER,
    idcategoria INTEGER,
    idcambio INTEGER,
    FOREIGN KEY(idclassificado) REFERENCES classificado (idclassificado),
    FOREIGN KEY(idmodelo) REFERENCES modelo (idmodelo),
    FOREIGN KEY(idmarca) REFERENCES marca (idmarca),
    FOREIGN KEY(idcombustivel) REFERENCES combustivel (idcombustivel),
    FOREIGN KEY(idcategoria) REFERENCES categoria (idcategoria),
    FOREIGN KEY(idcambio) REFERENCES cambio (idcambio)
    )

    ALTER TABLE classificado ADD FOREIGN KEY(idbairro) REFERENCES bairro (idbairro)
    ALTER TABLE classificado ADD FOREIGN KEY(idmunicipio) REFERENCES municipio (idmunicipio)
    ALTER TABLE tipo ADD FOREIGN KEY(idcategoria) REFERENCES categoria (idcategoria)
    ALTER TABLE imovel_caracteristica ADD FOREIGN KEY(idcaracteristica) REFERENCES caracteristica (idcaracteristica)
    ALTER TABLE imovel_caracteristica ADD FOREIGN KEY(idimovel) REFERENCES imovel (idimovel)
    ALTER TABLE veiculo_opcional ADD FOREIGN KEY(idveiculo) REFERENCES veiculo (idveiculo)      
     
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

    select * from bairro;
![Alt text](https://github.com/pedrohcosta/trab01/blob/master/imagens/prints/bairro.png?raw=true "Bairro")

    select * from cambio;
![Alt text](https://github.com/pedrohcosta/trab01/blob/master/imagens/prints/cambio.png?raw=true "Cambio")

    select * from caracteristica;
![Alt text](https://github.com/pedrohcosta/trab01/blob/master/imagens/prints/caracteristica.png?raw=true "Caracteristica")

    select * from categoria;
![Alt text](https://github.com/pedrohcosta/trab01/blob/master/imagens/prints/categoria.png?raw=true "Categoria")

    select * from classificado;
![Alt text](https://github.com/pedrohcosta/trab01/blob/master/imagens/prints/classificado.png?raw=true "Classificado")

    select * from combustivel;
![Alt text](https://github.com/pedrohcosta/trab01/blob/master/imagens/prints/combustivel.png?raw=true "Combustivel")

    select * from imovel;
![Alt text](https://github.com/pedrohcosta/trab01/blob/master/imagens/prints/imovel.png?raw=true "Imovel")

    select * from imovel_caracteristica;
![Alt text](https://github.com/pedrohcosta/trab01/blob/master/imagens/prints/imovel_caracteristica.png?raw=true "Imovel Caracteristica")

    select * from marca;
![Alt text](https://github.com/pedrohcosta/trab01/blob/master/imagens/prints/marca.png?raw=true "Marca")

    select * from modelo;
![Alt text](https://github.com/pedrohcosta/trab01/blob/master/imagens/prints/modelo.png?raw=true "Modelo")

    select * from municipio;
![Alt text](https://github.com/pedrohcosta/trab01/blob/master/imagens/prints/municipio.png?raw=true "Municipio")

    select * from opcional;
![Alt text](https://github.com/pedrohcosta/trab01/blob/master/imagens/prints/opcional.png?raw=true "Opcional")

    select * from tipo;
![Alt text](https://github.com/pedrohcosta/trab01/blob/master/imagens/prints/tipo.png?raw=true "Tipo")

    select * from veiculo;
![Alt text](https://github.com/pedrohcosta/trab01/blob/master/imagens/prints/veiculo.png?raw=true "Veiculo")

    select * from veiculo_opcional;
![Alt text](https://github.com/pedrohcosta/trab01/blob/master/imagens/prints/veiculo_opcional.png?raw=true "Veiculo Opcional")

####9.2	CONSULTAS DAS TABELAS COM FILTROS WHERE (Mínimo 3)<br>

    select * from imovel where vagas_garagem < 2
![Alt text](https://github.com/pedrohcosta/trab01/blob/master/imagens/prints/where_1.png?raw=true "")

    select * from imovel where quantidade_quartos = 2
![Alt text](https://github.com/pedrohcosta/trab01/blob/master/imagens/prints/where_2.png?raw=true "")

    select * from imovel inner join classificado ON imovel.idclassificado = classificado.idclassificado where valor < 100000
![Alt text](https://github.com/pedrohcosta/trab01/blob/master/imagens/prints/where_3.png?raw=true "")

####9.3	CONSULTAS QUE USAM OPERADORES LÓGICOS, ARITMÉTICOS E CAMPOS RENOMEADOS (Mínimo 2)<br>

    select * from imovel where vagas_garagem < 2 AND quantidade_quartos = 2
![Alt text](https://github.com/pedrohcosta/trab01/blob/master/imagens/prints/operadores_1.png?raw=true "")
    
    select * from veiculo where ano = 2010 AND quilometragem < 40000  AND quantidade_porta = 4
![Alt text](https://github.com/pedrohcosta/trab01/blob/master/imagens/prints/operadores_2.png?raw=true "")


####9.4	CONSULTAS QUE USAM OPERADORES LIKE (Mínimo 3) <br>

    select * from veiculo
    inner join classificado ON veiculo.idclassificado = classificado.idclassificado
    where titulo like '%toyota%'
![Alt text](https://github.com/pedrohcosta/trab01/blob/master/imagens/prints/like_1.png?raw=true "")

    select * from opcional
    inner join veiculo_opcional ON opcional.idopcional = veiculo_opcional.idopcional
    inner join veiculo ON veiculo_opcional.idveiculo = veiculo.idveiculo
    where opcional.nome like '%vidro elétrico%' or opcional.nome like '%trava elétrico%'
![Alt text](https://github.com/pedrohcosta/trab01/blob/master/imagens/prints/like_2.png?raw=true "")


    select * from veiculo
    inner join combustivel ON veiculo.idcombustivel= combustivel.idcombustivel
    inner join categoria ON veiculo.idcategoria = categoria.idcategoria
    WHERE combustivel.nome LIKE '%Gasolina%' AND categoria.nome LIKE '%Carro%'
![Alt text](https://github.com/pedrohcosta/trab01/blob/master/imagens/prints/like_3.png?raw=true "")


####9.5	ATUALIZAÇÃO E EXCLUSÃO DE DADOS (Mínimo 6)<br>

    delete from imovel;
    delete from veiculo;
    delete from cidade;

    update caracteristica set nome = 'Ar condicionado' where nome like '%Ar condicionado%'
    update opcional set nome = 'Ar condicionado' where nome like '%ar condicionado%'
    update municipio set nome = 'Teste' where idmunicipio = 1

![Alt text](https://github.com/pedrohcosta/trab01/blob/master/imagens/prints/delete_update.png?raw=true "")


####9.6	CONSULTAS COM JUNÇÃO E ORDENAÇÃO (Todas Junções)<br>

    SELECT * FROM veiculo
    INNER JOIN modelo ON veiculo.idmodelo = modelo.idmodelo
    INNER JOIN marca ON veiculo.idmarca = marca.idmarca
    INNER JOIN combustivel ON veiculo.idcombustivel = combustivel.idcombustivel
    INNER JOIN cambio ON veiculo.idcambio = cambio.idcambio
    INNER JOIN categoria ON veiculo.idcategoria = categoria.idcategoria
    INNER JOIN classificado ON veiculo.idclassificado = classificado.idclassificado
    INNER JOIN bairro ON classificado.idbairro = bairro.idbairro
    INNER JOIN municipio ON classificado.idbairro = municipio.idmunicipio
    LIMIT 10
![Alt text](https://github.com/pedrohcosta/trab01/blob/master/imagens/prints/juncao_ordenacao_1.png?raw=true "")

    SELECT * FROM imovel
    INNER JOIN tipo ON imovel.idtipo = tipo.idtipo
    INNER JOIN classificado ON imovel.idclassificado = classificado.idclassificado
    INNER JOIN bairro ON classificado.idbairro = bairro.idbairro
    INNER JOIN municipio ON classificado.idbairro = municipio.idmunicipio
    LIMIT 10
![Alt text](https://github.com/pedrohcosta/trab01/blob/master/imagens/prints/juncao_ordenacao_2.png?raw=true "")

    select * from opcional
    inner join veiculo_opcional ON opcional.idopcional = veiculo_opcional.idopcional
    inner join veiculo ON veiculo_opcional.idveiculo = veiculo.idveiculo
![Alt text](https://github.com/pedrohcosta/trab01/blob/master/imagens/prints/juncao_ordenacao_3.png?raw=true "")

    select * from caracteristica
    inner join imovel_caracteristica ON caracteristica.idcaracteristica = imovel_caracteristica.idcaracteristica
    inner join imovel ON imovel_caracteristica.idimovel = imovel.idimovel
![Alt text](https://github.com/pedrohcosta/trab01/blob/master/imagens/prints/juncao_ordenacao_4.png?raw=true "")

        
####9.7	CONSULTAS COM GROUP BY (Mínimo 5)<br>

    SELECT bairro.nome, count(*) AS total  FROM imovel
    INNER JOIN classificado ON imovel.idclassificado = classificado.idclassificado
    INNER JOIN bairro ON classificado.idbairro = bairro.idbairro
    GROUP BY bairro.nome
![Alt text](https://github.com/pedrohcosta/trab01/blob/master/imagens/prints/groupby_1.png?raw=true "")

    SELECT municipio.nome, count(*) AS total FROM imovel
    INNER JOIN classificado ON imovel.idclassificado = classificado.idclassificado
    INNER JOIN municipio ON classificado.idbairro = municipio.idmunicipio
    GROUP BY municipio.nome
![Alt text](https://github.com/pedrohcosta/trab01/blob/master/imagens/prints/groupby_2.png?raw=true "")

    SELECT classificado.cep, count(*) AS total FROM imovel
    INNER JOIN classificado ON imovel.idclassificado = classificado.idclassificado
    GROUP BY classificado.cep
![Alt text](https://github.com/pedrohcosta/trab01/blob/master/imagens/prints/groupby_3.png?raw=true "")

    SELECT bairro.nome, AVG(valor) AS total  FROM imovel
    INNER JOIN classificado ON imovel.idclassificado = classificado.idclassificado
    INNER JOIN bairro ON classificado.idbairro = bairro.idbairro
    where idtipo = 2
    GROUP BY bairro.nome
![Alt text](https://github.com/pedrohcosta/trab01/blob/master/imagens/prints/groupby_4.png?raw=true "")

    SELECT marca.nome, veiculo.ano, count(*)  FROM veiculo
    INNER JOIN classificado ON veiculo.idclassificado = classificado.idclassificado
    INNER JOIN marca ON veiculo.idmarca = marca.idmarca
    GROUP BY marca.nome, veiculo.ano order by 3 desc
![Alt text](https://github.com/pedrohcosta/trab01/blob/master/imagens/prints/groupby_5.png?raw=true "")


####9.8	CONSULTAS COM LEFT E RIGHT JOIN (Mínimo 4)<br>
####9.9	CONSULTAS COM SELF JOIN E VIEW (Todas Possíveis)<br>
####9.10	SUBCONSULTAS (Mínimo 3)<br>

    select * from veiculo where idveiculo IN (select idveiculo from veiculo where quantidade_porta < 5000)
![Alt text](https://github.com/pedrohcosta/trab01/blob/master/imagens/prints/subconsulta_1.png?raw=true "")

    select * from veiculo where idveiculo 
    IN (select idveiculo from veiculo where quantidade_porta = 4 and quilometragem > 50000)
![Alt text](https://github.com/pedrohcosta/trab01/blob/master/imagens/prints/subconsulta_2.png?raw=true "")

    select 
    (select avg(valor) media from veiculo 
    inner join classificado on veiculo.idclassificado = classificado.idclassificado
    inner join bairro on classificado.idbairro = bairro.idbairro
    where valor <> 0 and ano > 2010 and  bairro.nome like '%Serra%')
    ,
    (select min(valor) menor from veiculo 
    inner join classificado on veiculo.idclassificado = classificado.idclassificado
    inner join bairro on classificado.idbairro = bairro.idbairro
    where valor <> 0 and ano > 2010 and  bairro.nome like '%Serra%')
    ,
    (select max(valor) maior from veiculo 
    inner join classificado on veiculo.idclassificado = classificado.idclassificado
    inner join bairro on classificado.idbairro = bairro.idbairro
    where valor <> 0 and ano > 2010 and  bairro.nome like '%Serra%')
![Alt text](https://github.com/pedrohcosta/trab01/blob/master/imagens/prints/subconsulta_3.png?raw=true "")


###10	ATUALIZAÇÃO DA DOCUMENTAÇÃO DOS SLIDES PARA APRESENTAÇAO FINAL (Mínimo 6 e Máximo 10)<br>
###11	DIFICULDADES ENCONTRADAS PELO GRUPO<br>
###12  FORMATACAO NO GIT: https://help.github.com/articles/basic-writing-and-formatting-syntax/

###OBSERVAÇÕES IMPORTANTES

#### Em tese todos os arquivos do trabalho devem ser compartilhados no git 
1. Caso existam arquivos com conteúdos sigilosos, comunicar o professor que definirá em conjunto com o grupo a melhor forma de armazenamento do arquivo.

#### Todos os grupos deverão fazer Fork deste repositório e dar permissões administrativas ao usuário deste GIT, para acompanhamento do trabalho.

#### Os usuários criados no GIT devem possuir o nome de identificação do aluno (não serão aceitos nomes como Eu123, meuprojeto, pro456, etc). Em caso de dúvida comunicar o professor.



