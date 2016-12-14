--
-- PostgreSQL database dump
--

-- Dumped from database version 9.4.5
-- Dumped by pg_dump version 9.4.5
-- Started on 2016-12-14 10:00:32 BRST

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

DROP DATABASE trabalho_twitter;
--
-- TOC entry 2038 (class 1262 OID 17499)
-- Name: trabalho_twitter; Type: DATABASE; Schema: -; Owner: pedro
--

CREATE DATABASE trabalho_twitter WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'pt_BR.UTF-8' LC_CTYPE = 'pt_BR.UTF-8';


ALTER DATABASE trabalho_twitter OWNER TO pedro;

\connect trabalho_twitter

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- TOC entry 5 (class 2615 OID 2200)
-- Name: public; Type: SCHEMA; Schema: -; Owner: postgres
--

CREATE SCHEMA public;


ALTER SCHEMA public OWNER TO postgres;

--
-- TOC entry 2039 (class 0 OID 0)
-- Dependencies: 5
-- Name: SCHEMA public; Type: COMMENT; Schema: -; Owner: postgres
--

COMMENT ON SCHEMA public IS 'standard public schema';


--
-- TOC entry 174 (class 3079 OID 11895)
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- TOC entry 2041 (class 0 OID 0)
-- Dependencies: 174
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- TOC entry 173 (class 1259 OID 17502)
-- Name: tweets; Type: TABLE; Schema: public; Owner: pedro; Tablespace: 
--

CREATE TABLE tweets (
    id integer NOT NULL,
    idtweets character varying(20),
    mensagem character varying(500),
    data timestamp without time zone,
    usuario character varying(100),
    latitude double precision,
    longitude double precision
);


ALTER TABLE tweets OWNER TO pedro;

--
-- TOC entry 172 (class 1259 OID 17500)
-- Name: tweets_id_seq; Type: SEQUENCE; Schema: public; Owner: pedro
--

CREATE SEQUENCE tweets_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE tweets_id_seq OWNER TO pedro;

--
-- TOC entry 2042 (class 0 OID 0)
-- Dependencies: 172
-- Name: tweets_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pedro
--

ALTER SEQUENCE tweets_id_seq OWNED BY tweets.id;


--
-- TOC entry 1920 (class 2604 OID 17505)
-- Name: id; Type: DEFAULT; Schema: public; Owner: pedro
--

ALTER TABLE ONLY tweets ALTER COLUMN id SET DEFAULT nextval('tweets_id_seq'::regclass);


--
-- TOC entry 2033 (class 0 OID 17502)
-- Dependencies: 173
-- Data for Name: tweets; Type: TABLE DATA; Schema: public; Owner: pedro
--

INSERT INTO tweets (id, idtweets, mensagem, data, usuario, latitude, longitude) VALUES (66, '808808449396064257', 'CONTE CONOSCO!🎯
🔺♦🔺♦🔺♦🔺♦
COMPRE, VENDA, OU ALUGUE SEU IMÓVEL AQUI!📣📣📣📣📣… https://t.co/F7n6VoBvXZ', '2016-12-13 22:58:55', 'tonybarrosadm3', -38.476700000000001, -12.9747000000000003);
INSERT INTO tweets (id, idtweets, mensagem, data, usuario, latitude, longitude) VALUES (67, '808795174021238784', 'Tem alguém aqui que trabalhe na @Caixa ? Queria tirar umas dúvidas sobre financiamento de imóvel', '2016-12-13 22:06:10', 'lucasacre', -69.3964730000000003, -10.4967330000000008);
INSERT INTO tweets (id, idtweets, mensagem, data, usuario, latitude, longitude) VALUES (68, '808781312920326148', 'TJMG fará vistoria em imóvel onde deverá ser instalado o fórum de Jaíba: https://t.co/ryM6fW3ziW', '2016-12-13 21:11:06', 'cristianominas', -44.0627890000000022, -20.0598160000000014);
INSERT INTO tweets (id, idtweets, mensagem, data, usuario, latitude, longitude) VALUES (69, '808778573616136192', 'Oportunidade Imperdível!!!
Now Irajá
Av.Monsenhor Félix
Condições Especiais, com sinal de 4% do valor do imóvel e p… https://t.co/86ydLnICFp', '2016-12-13 21:00:12', 'RobertMaranhao', -46.8260390000000015, -24.008814000000001);
INSERT INTO tweets (id, idtweets, mensagem, data, usuario, latitude, longitude) VALUES (70, '808722628311732224', 'Como funciona o cálculo de juros da prefeitura sobre imóvel?', '2016-12-13 17:17:54', 'deboraqrm', -43.7954489999999979, -23.0830200000000012);
INSERT INTO tweets (id, idtweets, mensagem, data, usuario, latitude, longitude) VALUES (71, '808719473611943936', 'Casa 2 dormitórios, 3 vagas de garagem. Boa localização em Mongaguá.Código do Imóvel: 2577-VERA Nery Tel:(13) 3448-… https://t.co/uTVJU0pNhT', '2016-12-13 17:05:22', 'CasaBranca_Imob', -46.619529, -24.0897569999999988);
INSERT INTO tweets (id, idtweets, mensagem, data, usuario, latitude, longitude) VALUES (72, '808659119473356800', '@jjc_carvalho @lobaoeletrico @VEJA A pergunta do MPF, em momento nenhum Pede opinião é sim se eram ou não eram tratados como Donos do imóvel', '2016-12-13 13:05:32', 'RA_MON_KAS', -44.2110619999999983, -17.1478329999999985);
INSERT INTO tweets (id, idtweets, mensagem, data, usuario, latitude, longitude) VALUES (73, '808654810220085248', 'Plataforma da Zap Imóveis diz quanto vale o seu imóvel https://t.co/iC7gI4SBEx #SDV Via @exame https://t.co/T9cB6t5ig7', '2016-12-13 12:48:25', 'ryamauti', -46.6271060999999989, -23.4932374000000017);
INSERT INTO tweets (id, idtweets, mensagem, data, usuario, latitude, longitude) VALUES (74, '808640594172002305', 'Imóvel perto de parques e praças pode custar 20% a mais em Goiânia

Os imóveis localizados… https://t.co/5FucKy3kLe', '2016-12-13 11:51:56', 'lucianoluxu', -49.266445130000001, -16.7115336700000015);
INSERT INTO tweets (id, idtweets, mensagem, data, usuario, latitude, longitude) VALUES (75, '808548924923531264', '@roluli Quem fala de corrupção ñ compra imóvel pelo MCMV como investimento sem precisar! Vc sabia?', '2016-12-13 05:47:40', 'MonicaAraujoRJ', -43.1504483000000008, -22.9090699999999998);
INSERT INTO tweets (id, idtweets, mensagem, data, usuario, latitude, longitude) VALUES (76, '809001619010494464', 'Lula não tem um só imóvel ou negócio que não passe por dois ou três laranjas, é mesmo um cara de pau. Pensou que en… https://t.co/ndb64O9TJZ', '2016-12-14 11:46:31', 'OpusckiSulains', -48.6774890000000013, -27.0612880000000011);
INSERT INTO tweets (id, idtweets, mensagem, data, usuario, latitude, longitude) VALUES (77, '808996463355138048', 'Se você tem um imóvel para vender ou alugar não deixe de nos… https://t.co/Hnfpw2lvqH', '2016-12-14 11:26:01', 'LarissaAyla', -49.2742475000000013, -16.6954743000000008);
INSERT INTO tweets (id, idtweets, mensagem, data, usuario, latitude, longitude) VALUES (78, '808989276243460096', 'Uns dias atrás, antes de achar um imóvel, o coração acelerava e a respiração piorava só de abrir sites de imobiliárias.', '2016-12-14 10:57:28', 'thaelmpeixoto', -51.306147799999998, -30.2688069000000013);
INSERT INTO tweets (id, idtweets, mensagem, data, usuario, latitude, longitude) VALUES (79, '808875589050531844', '@CFilocomo eu acho mesmo que é questão de educação. Mas ali, acredito, que ele ficou imóvel pq não esperava. Prepotência mesmo', '2016-12-14 03:25:43', 'gabiabrunheiro', -46.5708470000000005, -23.509957);
INSERT INTO tweets (id, idtweets, mensagem, data, usuario, latitude, longitude) VALUES (80, '808501528852123649', '#ToPrecisandoDe um apartamento em um condomínio de luxo, um imóvel comercial, ser dono de uma área extensa de petróleo e uma Ferrari.', '2016-12-13 02:39:20', 'erivandrojoga10', -44.0627890000000022, -20.0598160000000014);
INSERT INTO tweets (id, idtweets, mensagem, data, usuario, latitude, longitude) VALUES (81, '808493853690957824', 'A cada 10 pessoas no litoral 11 são corretores de imóvel kskskdkd', '2016-12-13 02:08:50', 'ZeckPow_', -50.1532598000000007, -29.9867050999999982);
INSERT INTO tweets (id, idtweets, mensagem, data, usuario, latitude, longitude) VALUES (82, '808469876373356544', 'Acho que o dono do tal triplex e o  Deltan Dallagnol, afinal o cidadão gosta de investir em em imóvel https://t.co/t5OHeHMf7R', '2016-12-13 00:33:33', 'geziel_goes', -48.6236839999999972, -1.52645300000000006);
INSERT INTO tweets (id, idtweets, mensagem, data, usuario, latitude, longitude) VALUES (83, '808440442870235136', 'COMPRE, VENDA, OU ALUGUE SEU IMÓVEL AQUI!📣📣📣📣📣
https://t.co/ygD7W1zJrK
CRECI-BA… https://t.co/QWlADah4sq', '2016-12-12 22:36:36', 'tonybarrosadm3', -38.4988252899999992, -13.0035814399999996);
INSERT INTO tweets (id, idtweets, mensagem, data, usuario, latitude, longitude) VALUES (84, '808417668478935041', '🎯 ALUGA-SE imóvel na Cohab Rio Vermelho.
📞 Telefones: (66) 3422-5102 e 99901.2990
👉 Site: https://t.co/I2531Yn73d…… https://t.co/Gc26ZEoF4n', '2016-12-12 21:06:06', 'Batista_Imoveis', -54.9777389999999997, -17.0727890000000002);
INSERT INTO tweets (id, idtweets, mensagem, data, usuario, latitude, longitude) VALUES (85, '808414149906677761', '🎯 ALUGA-SE imóvel comercial na Vila Operária.
📞 Telefones: (66) 3422-5102 e 99901.2990
👉 Site:… https://t.co/bIHlLHZDCY', '2016-12-12 20:52:07', 'Batista_Imoveis', -54.9777389999999997, -17.0727890000000002);
INSERT INTO tweets (id, idtweets, mensagem, data, usuario, latitude, longitude) VALUES (86, '808394831894630400', 'Quem resistiu ao boom imobiliário encontra agora, chances ainda melhores de adquirir um imóvel.… https://t.co/CFRj9hOLQ6', '2016-12-12 19:35:21', 'Ranieriimoveis', -48.5, -1.44999999999999996);
INSERT INTO tweets (id, idtweets, mensagem, data, usuario, latitude, longitude) VALUES (87, '808385901147590656', 'Imóvel á venda porteira fechada, apartamento 1 dormitórios de frente para mar em Mongaguá.Filial 3: Vera Cruz - Mon… https://t.co/pZA9NFE0Mf', '2016-12-12 18:59:52', 'CasaBranca_Imob', -46.619529, -24.0897569999999988);
INSERT INTO tweets (id, idtweets, mensagem, data, usuario, latitude, longitude) VALUES (88, '808342136001351680', 'Astrólogo diz que 2017 será o ano do consumismo, vc ficará con su mismo carro,su mismo imóvel e, se tiver muita sorte, con su mismo trabalho', '2016-12-12 16:05:58', 'omarcolla', -73.9914820000000049, -33.7510505999999992);
INSERT INTO tweets (id, idtweets, mensagem, data, usuario, latitude, longitude) VALUES (89, '808305114456985600', 'Completa 8 meses a decisão de Moro de sequestrar a casa da mãe de José Dirceu, dona Olga, de 94 anos, q ficou no im… https://t.co/zC4xijE3dR', '2016-12-12 13:38:51', 'cartamaior', -47.0356909999999999, -23.5088110000000015);
INSERT INTO tweets (id, idtweets, mensagem, data, usuario, latitude, longitude) VALUES (90, '808296225229377536', 'Aprendendo com minha mãe sobre financiamento de imóvel.', '2016-12-12 13:03:32', 'christynadias', -34.9738346999999976, -7.24325699999999983);
INSERT INTO tweets (id, idtweets, mensagem, data, usuario, latitude, longitude) VALUES (91, '808227168975101952', 'Imóvel para vítimas de enchentes está pronto – falta todo o resto https://t.co/0LKKpDHTDL #SDV Via @exame https://t.co/w9bg1kkjqe', '2016-12-12 08:29:07', 'ryamauti', -46.6271060999999989, -23.4932374000000017);
INSERT INTO tweets (id, idtweets, mensagem, data, usuario, latitude, longitude) VALUES (92, '808173938022957056', 'Mano, eu não tô conseguindo mexer uma pálpebra KKKKKKKKKKK Isso tá imóvel de tanto sono, tá muito engraçado KKKKKKK', '2016-12-12 04:57:36', 'alinegullich_', -49.0180492000000001, -27.2552869999999992);
INSERT INTO tweets (id, idtweets, mensagem, data, usuario, latitude, longitude) VALUES (93, '808139878282252288', '@JMTrevisan se tem imóvel próprio (crack), se ainda ta financiando/juntando só anti depressivos ou cocaína', '2016-12-12 02:42:16', 'tksheep', -44.0627890000000022, -20.0598160000000014);
INSERT INTO tweets (id, idtweets, mensagem, data, usuario, latitude, longitude) VALUES (94, '808126437806968833', '🌴BARRA FAMILY RESORT🌴

🌅Espetacular imóvel de 2 quartos sendo uma suíte, ótima Varanda,… https://t.co/XQTz244ef1', '2016-12-12 01:48:51', 'mvpersonal10', -43.4431799999999981, -23.0076670000000014);
INSERT INTO tweets (id, idtweets, mensagem, data, usuario, latitude, longitude) VALUES (95, '808122105472684032', 'Dei uma porrada na mesa q tirei o dedo do lugar agr ta imóvel', '2016-12-12 01:31:38', 'shine0n', -51.306147799999998, -30.2688069000000013);
INSERT INTO tweets (id, idtweets, mensagem, data, usuario, latitude, longitude) VALUES (96, '808099568428744705', 'Canal 19 com tela preta e música e Canal 20 com Show do Imóvel.

E EU PERDIDO.', '2016-12-12 00:02:05', 'giovaneml', -49.4774652999999986, -28.8434850000000012);
INSERT INTO tweets (id, idtweets, mensagem, data, usuario, latitude, longitude) VALUES (97, '808096089236717569', '@minycalegari achei essa casa aqui perto do trabalho https://t.co/Nkgespbtpd', '2016-12-11 23:48:16', 'nedasuacont4', -48.7459849000000034, -27.641830800000001);
INSERT INTO tweets (id, idtweets, mensagem, data, usuario, latitude, longitude) VALUES (98, '808037132765982720', '[11/12 17:28] nanda: Zap zap seu imóvel zap
[11/12 17:29] PV: FINALMENTE ALGUEM Q ME ENTENDE
[11/12 17:30] PV: MEU DEUS EU TE AMO DENOVO', '2016-12-11 19:53:59', 'fechavesss', -43.2249389999999991, -22.748462700000001);
INSERT INTO tweets (id, idtweets, mensagem, data, usuario, latitude, longitude) VALUES (99, '807978363423965184', 'to ate meio imovel', '2016-12-11 16:00:28', 'carolerstone', -47.2450491999999969, -23.0607100000000003);
INSERT INTO tweets (id, idtweets, mensagem, data, usuario, latitude, longitude) VALUES (100, '807975322146643968', 'No Imóvel Fest tem #coordenadoralis #lopesimmobilis 🔝☺️🎯 @ Riomar… https://t.co/LiFELI6lDI', '2016-12-11 15:48:22', 'amandancaroline', -38.5669800000000009, -3.72750000000000004);
INSERT INTO tweets (id, idtweets, mensagem, data, usuario, latitude, longitude) VALUES (101, '807967284249722880', 'Apartamento para Locação - Sorocaba / SP no bairro Centro, 3 dormitórios, 3 banheiros, 1 suíte, 2 garagens https://t.co/rOqqcI273O', '2016-12-11 15:16:26', 'BruniPaulo', -47.5194181000000029, -23.6493910000000014);
INSERT INTO tweets (id, idtweets, mensagem, data, usuario, latitude, longitude) VALUES (102, '807966811786530816', 'Apartamento para Locação - Votorantim / SP no bairro Vila Domingues, 2 dormitórios, 1 banheiro, 1 garagem https://t.co/Xx5tVFgsQ1', '2016-12-11 15:14:33', 'BruniPaulo', -47.5194181000000029, -23.6493910000000014);
INSERT INTO tweets (id, idtweets, mensagem, data, usuario, latitude, longitude) VALUES (103, '807966243181498368', 'Kitnet para Locação - Votorantim / SP no bairro Jardim Paraiso, 1 dormitório, 1 banheiro, 1 garagem https://t.co/Le0IOumYEQ', '2016-12-11 15:12:18', 'BruniPaulo', -47.5194181000000029, -23.6493910000000014);
INSERT INTO tweets (id, idtweets, mensagem, data, usuario, latitude, longitude) VALUES (104, '807873587939917824', 'As praias mais caras e baratas para alugar imóvel no Ano Novo https://t.co/7kSFo6bYG5 #SDV Via @exame https://t.co/zDlzj2636U', '2016-12-11 09:04:07', 'ryamauti', -46.6271060999999989, -23.4932374000000017);
INSERT INTO tweets (id, idtweets, mensagem, data, usuario, latitude, longitude) VALUES (105, '807699361866088448', 'Espetacular imóvel decorado, 101mts muito bem resolvidos , no principal Resort Real da Barra da… https://t.co/t9ZSbqrlya', '2016-12-10 21:31:48', 'mvpersonal10', -43.3886686600000004, -22.9722592100000007);
INSERT INTO tweets (id, idtweets, mensagem, data, usuario, latitude, longitude) VALUES (106, '807667926715273216', '@fjunqueira Sobre o terreno, é da MRV. Estádio valoriza a região. Ela tem cheio de imóvel perto...pode ser uma troca de favores.', '2016-12-10 19:26:54', 'Galo_Pedro', -43.6983480999999969, -21.9998657000000009);
INSERT INTO tweets (id, idtweets, mensagem, data, usuario, latitude, longitude) VALUES (107, '807619848310243328', '#Repost construtoraescudo with repostapp
・・・
#IMÓVEL 
Primeiro… https://t.co/J7yWYfRbX9', '2016-12-10 16:15:51', 'fabionahuz', -44.2434399999999997, -2.5245700000000002);
INSERT INTO tweets (id, idtweets, mensagem, data, usuario, latitude, longitude) VALUES (108, '807591384601468928', '@RVenesia @GuilherGuedes @fjunqueira @RodP13 Patio Savassi, Multiplan fez mesma coisa: comprou imóvel DEPOIS de com… https://t.co/4IIahNQJL5', '2016-12-10 14:22:45', 'RegisGalo_13', -44.0627890000000022, -20.0598160000000014);
INSERT INTO tweets (id, idtweets, mensagem, data, usuario, latitude, longitude) VALUES (109, '807588136536670209', '@BCD1980 @RVenesia @fjunqueira Sim, estamos abordando exatamente isso. Coisas diferentes. O Atletico tem o imovel, a Multiplan tem o negocio', '2016-12-10 14:09:50', 'RegisGalo_13', -44.0627890000000022, -20.0598160000000014);
INSERT INTO tweets (id, idtweets, mensagem, data, usuario, latitude, longitude) VALUES (110, '807568615717347328', 'COMPRE, VENDA, OU ALUGUE SEU IMÓVEL AQUI!📣📣📣📣📣
https://t.co/ygD7W1zJrK
CRECI-BA… https://t.co/nGPCdMw9qS', '2016-12-10 12:52:16', 'tonybarrosadm3', -38.476700000000001, -12.9747000000000003);
INSERT INTO tweets (id, idtweets, mensagem, data, usuario, latitude, longitude) VALUES (111, '807566723511619584', 'B O M  D I A!✌✌✌

C O M P R E, VENDA, OU ALUGUE  SEU IMÓVEL… https://t.co/AXEl4xbgTw', '2016-12-10 12:44:45', 'tonybarrosadm3', -38.4988252899999992, -13.0035814399999996);
INSERT INTO tweets (id, idtweets, mensagem, data, usuario, latitude, longitude) VALUES (112, '807565995057496064', '@leokusanagi Poxa vida, tem parente meu que tem propriedade, nome e emprego OK, dá pra fazer contrato de compra de imóvel parcelado de boas', '2016-12-10 12:41:51', 'anneboolean', -46.8260390000000015, -24.008814000000001);
INSERT INTO tweets (id, idtweets, mensagem, data, usuario, latitude, longitude) VALUES (113, '807562914240532480', 'Quais as chances de eu me arrepender de comprar um imóvel pra eu ir pagando tudo sozinha e tal mas no nome de um parente?', '2016-12-10 12:29:37', 'anneboolean', -46.8260390000000015, -24.008814000000001);
INSERT INTO tweets (id, idtweets, mensagem, data, usuario, latitude, longitude) VALUES (114, '807555922323271680', 'Venha dormir, diz o Destino.Você finge que obedece.Mas na madrugada,abre a janela para o mar e lá está Deus,de rosto imóvel diante do luar', '2016-12-10 12:01:50', 'neiduclos', -48.6103127000000015, -27.8389355999999992);
INSERT INTO tweets (id, idtweets, mensagem, data, usuario, latitude, longitude) VALUES (115, '807434130371780608', 'A maior surpresa é o telão imóvel que só abre no final', '2016-12-10 03:57:52', 'gusmaoboy', -35.0198049999999981, -8.15755399999999931);
INSERT INTO tweets (id, idtweets, mensagem, data, usuario, latitude, longitude) VALUES (116, '807364772501094406', '@fcbtsjimin 
# Nome: Min Yoongi (민윤기) #
# Apelidos: Motionless Min (Min Imóvel, há dias em que ele não se mexe), Pai #', '2016-12-09 23:22:16', 'fcbtsjimin', -73.9914820000000049, -33.7510505999999992);
INSERT INTO tweets (id, idtweets, mensagem, data, usuario, latitude, longitude) VALUES (117, '807364200251228161', 'Se atente ao Registro do seu Imóvel! @ Shopemi https://t.co/gf6ANh7DOy', '2016-12-09 23:20:00', 'edsongvoliveira', -47.3100900000000024, -23.1821300000000008);
INSERT INTO tweets (id, idtweets, mensagem, data, usuario, latitude, longitude) VALUES (118, '807362424223526912', '@paula_menezess pior que não.. tem alguns defeitos no imóvel.. rodapé, vazamento..', '2016-12-09 23:12:56', 'heipetraz', -51.306147799999998, -30.2688069000000013);


--
-- TOC entry 2043 (class 0 OID 0)
-- Dependencies: 172
-- Name: tweets_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pedro
--

SELECT pg_catalog.setval('tweets_id_seq', 118, true);


--
-- TOC entry 1922 (class 2606 OID 17510)
-- Name: tweets_pkey; Type: CONSTRAINT; Schema: public; Owner: pedro; Tablespace: 
--

ALTER TABLE ONLY tweets
    ADD CONSTRAINT tweets_pkey PRIMARY KEY (id);


--
-- TOC entry 2040 (class 0 OID 0)
-- Dependencies: 5
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


-- Completed on 2016-12-14 10:00:32 BRST

--
-- PostgreSQL database dump complete
--

