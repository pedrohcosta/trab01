-- Geração de Modelo físico
-- Sql ANSI 2003 - brModelo.



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
