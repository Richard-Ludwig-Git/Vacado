--
-- PostgreSQL database dump
--

\restrict TGaW2SgpB6wPLMdFN590cxFojuhcdv4V6sWKaKmvJjpIzPqOdmCWehVLVZjWhPX

-- Dumped from database version 17.6 (Postgres.app)
-- Dumped by pg_dump version 17.6 (Postgres.app)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: user_db; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.user_db (
    id bigint NOT NULL,
    user_name character varying(50) NOT NULL,
    password character varying(200) NOT NULL,
    email character varying(50) NOT NULL
);


ALTER TABLE public.user_db OWNER TO postgres;

--
-- Name: user_db_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.user_db_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.user_db_id_seq OWNER TO postgres;

--
-- Name: user_db_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.user_db_id_seq OWNED BY public.user_db.id;


--
-- Name: vacation_request; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.vacation_request (
    id bigint NOT NULL,
    duration integer NOT NULL,
    theme character varying(20) NOT NULL,
    accommodation_type character varying(20) NOT NULL,
    budget character varying(6) NOT NULL,
    user_id bigint,
    requested timestamp without time zone,
    origin_city character varying(50) NOT NULL,
    transportation_type character varying(50) NOT NULL,
    max_travel_time bigint NOT NULL,
    special_need character varying(100) NOT NULL
);


ALTER TABLE public.vacation_request OWNER TO postgres;

--
-- Name: vacation_request_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.vacation_request_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.vacation_request_id_seq OWNER TO postgres;

--
-- Name: vacation_request_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.vacation_request_id_seq OWNED BY public.vacation_request.id;


--
-- Name: vacation_result; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.vacation_result (
    id bigint NOT NULL,
    destination character varying(1000) NOT NULL,
    transportation_type character varying(1000) NOT NULL,
    accommodation character varying(1000) NOT NULL,
    activities character varying(20000) NOT NULL,
    tips character varying(20000),
    request_id bigint,
    user_id bigint,
    travel_time character varying(1000)
);


ALTER TABLE public.vacation_result OWNER TO postgres;

--
-- Name: vacation_result_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.vacation_result_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.vacation_result_id_seq OWNER TO postgres;

--
-- Name: vacation_result_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.vacation_result_id_seq OWNED BY public.vacation_result.id;


--
-- Name: user_db id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_db ALTER COLUMN id SET DEFAULT nextval('public.user_db_id_seq'::regclass);


--
-- Name: vacation_request id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.vacation_request ALTER COLUMN id SET DEFAULT nextval('public.vacation_request_id_seq'::regclass);


--
-- Name: vacation_result id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.vacation_result ALTER COLUMN id SET DEFAULT nextval('public.vacation_result_id_seq'::regclass);


--
-- Data for Name: user_db; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.user_db (id, user_name, password, email) FROM stdin;
4	AC	$2b$12$DOhn7UffMZR6i3jtlbtpoea47EIBW/BtbXRXSK0Pn8K8tAaf9Pljm	test@vacado.com
5	Manos	$2b$12$Hd66aDPHdoihoY4Yw3K8V.l7mtKtrHcTgiKoQXYQBemvFAG94BROK	maons@test
61	Testuser1	$2b$12$SOcdoZFtddfeAbah6YjKAOh1F8Ny7oyB12YIhAO9AT50qG3b5/gKS	lolamail
62	Testuser1	$2b$12$VsfalU37fzrUMEChRcoOEu3uXNsB4KAfR7eFl4K8YSeIatAFIXp2y	lolamail
63	Testuser1	$2b$12$EB7hiXyFt5mclAc2VTCj/eEnVM4RPpZF40DI/FrKN8xi.MWvrYSuu	lolamail
64	Testuser1	$2b$12$ihXHssJGSjAUXojua1NsXejIZAO9be5cH15F8XIPZp8TCr0yLLWvq	lolamail
65	Testuser1	$2b$12$vOeKbfUnVaqt5ab6u8DfZer/Ls/A2QwBclFLHXrhtASR5ahElIU4y	lolamail
7 postgres	$2b$12$6qN4MunbtHJ5AtJsJPnlluMUhrMLiVURQPKNyvyaDrL5ssIznV/m.	vlad@dracul.ro
8	test	$2b$12$dMZQR5khTxoKzJIIkZASpOlPis6MmQA1HVoSxceL.7hWBT1WsXUrC	testmail
10	Urlauber1000	$2b$12$WwvSgsDVPKoUfw81y1H0Deg2SodwSnBSBucnEwo1AvmS0zL9nMX7y	pape.annchristin@yahoo.com
11	bla	$2b$12$z7MhlQZw2BRlfx6BfzTOW.fI4kRTHvm5erjKY98TPWmhcQ3Jibg.6	ohnneinbla
12		$2b$12$ySr9uKWtK/MFrJ5BGB0LiuGfzkDKhgAkEwwtMI.mICALxxkYoayr.	
13	string	$2b$12$7/U8d16NqlO9WDzg.JAA..6dkpfJBLzujBpnQwRLm8yXmqbzLsg8y	string
14	lol	$2b$12$6dzusHwglEDQoAGjfIwsfeWs8JzwcoCO52L/KsIBAgyMpiJGnniBC	lol
15	test	$2b$12$Mg.KO7HNzrh3f5uOqIkNSO7IVRRTdQoE0SVOb8WeJWu1mZNvaycNq	lolmail
16	Testuser1	$2b$12$1BcssScLzfQWPis9uVZj3.3MtC58FnMDcfijBgAG3RUxj.acoMCRq	lolamail
17	Testuser1	$2b$12$ve7yF0KGEm/AgH9YmHJsye3r6U.DUOoWDTJFn.X3V70hVLeNtE3u.	lolamail
18	Testuser1	$2b$12$uh2ntUhZ5wXh3n5BkkmuwuwJ.r4STRVg7Rn4FGF8AMuhrgG0jTg1e	lolamail
19	Testuser1	$2b$12$DyXPGSAGvxJwAvaFdgEnoeCGCINDfhAsieB6O930T0gC0BwoU3Yha	lolamail
20	Testuser1	$2b$12$hDqWlHlDOMJ.xf5N1Lly6uiHwDyWgTGsDj/AaFj5j1CxWzSIzsNXu	lolamail
21	Testuser1	$2b$12$Wph60CUV.32M/bgr4.NMseHbz32/fSfnbv52R/nlRM0yotiS6SNS2	lolamail
22	Testuser1	$2b$12$u3DHxYH3yrZz7MYOxg.pBeHxu5ae3KRb7V14NEZ4RaB.x79Vj.Tgm	lolamail
23	Testuser1	$2b$12$HPHkqrfoXlPaqlxQ/AsdP.BiY/uH7PLO9ELd7P8c3qr4i9Wo4ptjC	lolamail
24	Testuser1	$2b$12$CHbssFN/K9BdpmhmoOxtpOGzbdI7VliGl.hJswHt9LJf/CwHLav.O	lolamail
25	Testuser1	$2b$12$sUNV8lhftmLcq84ff.wUL.Jnt1yUIr2xA3H6jfpI4mMLVbynVGwxu	lolamail
26	Testuser1	$2b$12$Dm1svr4vUxuunsjsQdqkdeQAyNEMdsBvFfD4AckalNvZXw0.MJT8i	lolamail
27	Testuser1	$2b$12$ZXqjjm9HTOraig7SMyNWoOsdZx5rI7GFu7V5b5PhK8/qWSllkpU/K	lolamail
28	Testuser1	$2b$12$fGLGFls3HW1ILL1LdmHqde6fbvrD2DIRt/P98adkbBohZ23BVRjaO	lolamail
29	Testuser1	$2b$12$eCaSYgIB5Y0IZcTo39.mQeoJARnClrdZud/1zNB806DZp9ITM2fTC	lolamail
30	Testuser1	$2b$12$xj4EIqQL0gFzL0x4v//xI.zlXhmuM13zbn3/NuT7jGX6pMrNrN0gu	lolamail
31	Testuser1	$2b$12$LmzS65M4mA.8UZNdUeeY4eR7DVozUjU761fU3Y.iNj/qGi4trHhR.	lolamail
32	Testuser1	$2b$12$2pdQz1WQuraGgl/h4/B6HekeGsG.8BiQN/WJiQ/irZJg5Oh2KBIHe	lolamail
33	Testuser1	$2b$12$/nHaGlJhH56NU0a0.KAJZetFOJn3QL/L7sUF05j.X4TjanAbr3Vsa	lolamail
34	Testuser1	$2b$12$wnBRpPDjNRSL6idEfuu.A.wwOcn5yy58rp3R5cDvGp7cMuEAgGPea	lolamail
35	Testuser1	$2b$12$v7E2k6H6/.k0MmygLCXABeMLdJe3XBBobWODUTzS0tS62rTJwQELy	lolamail
36	Testuser1	$2b$12$J8fYdum2L3h0/gq.khxvLu0lPzX0DLdgySq3Ypomy55A.xJd5ZJHW	lolamail
37	Testuser1	$2b$12$eH3WwbHJXTpOX8nA9I1qYeW5Gn1hnIRTYusHiUTaUXXoEv1Fas2Na	lolamail
38	Testuser1	$2b$12$7c9AvKd6BRPQfNPkJrFi4uNALO.msPI0yxd09MXFubByA7oXfnJE.	lolamail
39	Testuser1	$2b$12$Law9JlF.ICO11mmxsRJMkOHfy6A4lFZhlvQoAMAl8Ny5dNFBvtXKG	lolamail
40	Testuser1	$2b$12$DsS3tZr6l/mLPfw3hHNpDOURQUHZy8zP4Y3wHERAomtHA8bl1TQOW	lolamail
41	Testuser1	$2b$12$9gco2iNhODOjtPo5doy4OeiDO9NAHLmkOLIHqVh1BXwfc3gxSH2aC	lolamail
42	Testuser1	$2b$12$zqOddDlHnH2zLnMypur5rOYm2dpChxA.ORYsPkYpHJkVdwAcjVw26	lolamail
43	Testuser1	$2b$12$BXvul.0RDrSq9yTiuWOWseJM1ifrm9Bjf7FjeJtnKN3eNtFJZJOb6	lolamail
44	Testuser1	$2b$12$jPkh.L3jHJfRlQii9iEBYuvUcMop5Np8IhslMOLzqIO/No5X3b7Bm	lolamail
45	Testuser1	$2b$12$zdemftW8kegtg006nbFZ4ep6byDk5Pmm5HO38SCQFS1EUetwfbN4y	lolamail
46	Testuser1	$2b$12$VWqX.G6clzTuPjZYilDetOmjtJz5NcIyGBfBkIyysZRQNF1IgQHWa	lolamail
47	Testuser1	$2b$12$thhwW0inJSeCjSp6KmV4AOVUNAVkrryN5.tbOp3F9rp2DdGp6wgna	lolamail
48	Testuser1	$2b$12$U3PmDk.8cHVUGTVgSRG3J.nGxjZkG21iiwmWf1DK5p7reeyA6Jm6a	lolamail
49	Testuser1	$2b$12$er.PWwRYqsMYndJCJ94fD.e.oIGV1B.MnubAQXPR73GuLmv7FAkLa	lolamail
50	Testuser1	$2b$12$0ERPMEf6c72D9uwKSf89Su6wIctkxClXZxDVz0q3rwz1EOyZGhhqO	lolamail
51	Testuser1	$2b$12$AWZA6qeO/aMdr4MDKQcFBu1AOIUaY1fdd9tvSPocTjY5FYxr64Ay2	lolamail
52	Testuser1	$2b$12$Qg8AB8zZY/hHDFTJNCijgOgIO00bwEkb1BiTzlTkwLpqC5fQcCI2O	lolamail
53	Testuser1	$2b$12$EhkLDoDibvSWcr3ZxxP6auh2qwnni8wWtsiQih/XTEjYZ8OtRCMLe	lolamail
54	Testuser1	$2b$12$H4ZXjJO/p2gYUffCYf4sGOJENwuIeMseyo17s8zcuWcvol9b8xEL2	lolamail
55	Testuser1	$2b$12$mc6uSD4zHA25JyYUx5xjqum0ft8REotH7z.yXSyCDnGbRVUV1XyrW	lolamail
56	Testuser1	$2b$12$5XcSRPtK0jF6iWi3esghu.3dkOPEF0xzrpF4/63Sy4z.5.yBj5lMq	lolamail
57	Testuser1	$2b$12$Hg40W027bcStUt9Xmb028ufAli3jgkByNFFjvRZKhW0yMLNTX967q	lolamail
58	Testuser1	$2b$12$4jhu16ExYpeMyHCMZLEUy.907Kw9Lopys3Nw5IZtHypdFzcy7lesq	lolamail
59	Testuser1	$2b$12$5pa8FRVLtdBLRDVAB1hZy.ip1wxVUxvqACWexWAihUDjJ9Z54f.US	lolamail
60	Testuser1	$2b$12$hFCMfW8HYyb1TTNf7HI60uw1jQNHR4/XOWHN2Lfq8k7ajm5pkhowC	lolamail
\.


--
-- Data for Name: vacation_request; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.vacation_request (id, duration, theme, accommodation_type, budget, user_id, requested, origin_city, transportation_type, max_travel_time, special_need) FROM stdin;
56	18	Beach	self-catering	900	7	2025-09-09 13:34:25.239684	Ubud	Scooter	0	Baby
57	3	Hiking	Hotel	500	7	2025-09-09 16:49:17.819468	Berlin	airplane	0	extreme hinking
\.


--
-- Data for Name: vacation_result; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.vacation_result (id, destination, transportation_type, accommodation, activities, tips, request_id, user_id, travel_time) FROM stdin;
18	Lovina, North Bali	Scooter (with baby carrier attachment and helmet)	Self-catering bungalow near the beach, with kitchenette and baby-friendly amenities like crib and high chair.	Day 1: Arrive and settle in. Enjoy the sunset on the beach. \nDay 2: Light morning beach walk, relax in the bungalow garden. \nDay 3: Visit Banjar Hot Springs (early morning when less crowded, gentle pools for baby). \nDay 4: Explore Lovina beach shops and try a smoothie bowl cafe. \nDay 5: Dolphin watching tour (choose a late-morning, baby-friendly operator). \nDay 6: Family picnic at Melka Excelsior Park (shady areas and playground). \nDay 7: Rest day, swim at bungalow pool. \nDay 8: Explore Singsing Waterfall, easy walk, hold baby in carrier. \nDay 9: Local handicraft market browsing. \nDay 10: Snorkel trip with glass-bottom boat (short trip, shaded, safe for families). \nDay 11: Rest and nap day. \nDay 12: Yoga class with baby (some resorts offer family yoga). \nDay 13: Visit Gedong Kertya library and museum (stroller accessible). \nDay 14: Afternoon at Lovina beach playground. \nDay 15: Morning market walk, try fresh tropical fruit. \nDay 16: Explore Buddhist Monastery Brahmavihara-Arama (family-friendly, easy strolls). \nDay 17: Rest day, pool and garden time at bungalow. \nDay 18: Last beach picnic, prepare for departure.	Try simple warungs offering nasi campur and gado-gado, smoothie bowls, and fresh seafood grilled by the beach. Many cafes offer baby-friendly, mild or mashed options and fruit purees.	56	7	Approx. 3 hours from Ubud by scenic coastal route. No flights required.
19	Innsbruck, Austria	Airplane (Berlin to Innsbruck direct flight)	3-star hiking-friendly hotel in Innsbruck, ideally central or near Nordkette cable car	Day 1: Arrival and warm-up hike in Seegrube area (Nordkette range)\nDay 2: All-day extreme hike on Karwendel High Trail, renowned for rugged terrain and alpine scenery\nDay 3: Morning: Short hike in Patscherkofel or Hafelekar area, afternoon leisure and return flight	Sample Tyrolean specialties like Tiroler Gröstl, Kaspressknödel, and tasty Apfelstrudel at local mountain huts	57	7	Approx. 1.5 hours flight
\.


--
-- Name: user_db_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.user_db_id_seq', 65, true);


--
-- Name: vacation_request_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.vacation_request_id_seq', 57, true);


--
-- Name: vacation_result_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.vacation_result_id_seq', 19, true);


--
-- Name: user_db user_db_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_db
    ADD CONSTRAINT user_db_pkey PRIMARY KEY (id);


--
-- Name: vacation_request vacation_request_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.vacation_request
    ADD CONSTRAINT vacation_request_pkey PRIMARY KEY (id);


--
-- Name: vacation_result vacation_result_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.vacation_result
    ADD CONSTRAINT vacation_result_pkey PRIMARY KEY (id);


--
-- Name: vacation_result Request_connection; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.vacation_result
    ADD CONSTRAINT "Request_connection" FOREIGN KEY (request_id) REFERENCES public.vacation_request(id);


--
-- Name: vacation_result user_connection; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.vacation_result
    ADD CONSTRAINT user_connection FOREIGN KEY (user_id) REFERENCES public.user_db(id);


--
-- Name: vacation_request user_connection; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.vacation_request
    ADD CONSTRAINT user_connection FOREIGN KEY (user_id) REFERENCES public.user_db(id);


--
-- PostgreSQL database dump complete
--

\unrestrict TGaW2SgpB6wPLMdFN590cxFojuhcdv4V6sWKaKmvJjpIzPqOdmCWehVLVZjWhPX

