--
-- PostgreSQL database dump
--

-- Dumped from database version 13.3 (Ubuntu 13.3-1.pgdg20.04+1)
-- Dumped by pg_dump version 13.3 (Ubuntu 13.3-1.pgdg20.04+1)

-- Started on 2023-08-25 21:09:34 GMT

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 3229 (class 1262 OID 57652)
-- Name: test; Type: DATABASE; Schema: -; Owner: -
--

CREATE DATABASE test WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'en_US.UTF-8';


\connect test

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 3205 (class 0 OID 57752)
-- Dependencies: 213
-- Data for Name: articles; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.articles (id, country_id, chapter_id, number, title, text) VALUES (1, 46, 1, 1, 'SUPREMACY OF THE CONSTITUTION', '');
INSERT INTO public.articles (id, country_id, chapter_id, number, title, text) VALUES (2, 46, 1, 2, 'ENFORCEMENT OF THE CONSTITUTION', '');
INSERT INTO public.articles (id, country_id, chapter_id, number, title, text) VALUES (3, 46, 1, 3, 'DEFENCE OF THE CONSTITUTION', '');
INSERT INTO public.articles (id, country_id, chapter_id, number, title, text) VALUES (5, 57, 33, 1, 'Fake Article Title', 'Fake article text');


--
-- TOC entry 3203 (class 0 OID 57735)
-- Dependencies: 211
-- Data for Name: chapters; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.chapters (id, number, text, country_id) VALUES (1, 1, 'THE CONSTITUTION', 46);
INSERT INTO public.chapters (id, number, text, country_id) VALUES (6, 2, 'TERRITORIES OF GHANA', 46);
INSERT INTO public.chapters (id, number, text, country_id) VALUES (7, 3, 'CITIZENSHIP', 46);
INSERT INTO public.chapters (id, number, text, country_id) VALUES (8, 4, 'THE LAWS OF GHANA', 46);
INSERT INTO public.chapters (id, number, text, country_id) VALUES (9, 5, 'FUNDAMENTAL HUMAN RIGHTS AND FREEDOMS', 46);
INSERT INTO public.chapters (id, number, text, country_id) VALUES (10, 6, 'THE DIRECTIVE PRINCIPLES OF STATE POLICY', 46);
INSERT INTO public.chapters (id, number, text, country_id) VALUES (12, 8, 'THE EXECUTIVE', 46);
INSERT INTO public.chapters (id, number, text, country_id) VALUES (13, 9, 'THE COUNCIL OF STATE', 46);
INSERT INTO public.chapters (id, number, text, country_id) VALUES (14, 10, 'THE LEGISLATURE', 46);
INSERT INTO public.chapters (id, number, text, country_id) VALUES (15, 11, 'THE JUDICIARY', 46);
INSERT INTO public.chapters (id, number, text, country_id) VALUES (16, 12, 'FREEDOM AND INDEPENDENCE OF THE MEDIA', 46);
INSERT INTO public.chapters (id, number, text, country_id) VALUES (17, 13, 'FINANCE', 46);
INSERT INTO public.chapters (id, number, text, country_id) VALUES (18, 14, 'THE PUBLIC SERVICES', 46);
INSERT INTO public.chapters (id, number, text, country_id) VALUES (19, 15, 'THE POLICE SERVICE', 46);
INSERT INTO public.chapters (id, number, text, country_id) VALUES (20, 16, 'THE PRISONS SERVICE', 46);
INSERT INTO public.chapters (id, number, text, country_id) VALUES (21, 17, 'THE ARMED FORCES OF GHANA', 46);
INSERT INTO public.chapters (id, number, text, country_id) VALUES (22, 18, 'COMMISSION ON HUMAN RIGHTS AND ADMINISTRATIVE JUSTICE', 46);
INSERT INTO public.chapters (id, number, text, country_id) VALUES (23, 19, 'NATIONAL COMMISSION FOR CIVIC EDUCATION', 46);
INSERT INTO public.chapters (id, number, text, country_id) VALUES (24, 20, 'DECENTRALIZATION AND LOCAL GOVERNMENT', 46);
INSERT INTO public.chapters (id, number, text, country_id) VALUES (25, 21, 'LANDS AND NATURAL RESOURCES', 46);
INSERT INTO public.chapters (id, number, text, country_id) VALUES (27, 23, 'COMMISSIONS OF INQUIRY', 46);
INSERT INTO public.chapters (id, number, text, country_id) VALUES (28, 24, 'CODE OF CONDUCT FOR PUBLIC OFFICERS', 46);
INSERT INTO public.chapters (id, number, text, country_id) VALUES (29, 25, 'AMENDMENT OF THE CONSTITUTION', 46);
INSERT INTO public.chapters (id, number, text, country_id) VALUES (30, 26, 'MISCELLANEOUS', 46);
INSERT INTO public.chapters (id, number, text, country_id) VALUES (26, 22, 'CHIEFTAINCY', 46);
INSERT INTO public.chapters (id, number, text, country_id) VALUES (11, 7, 'REPRESENTATION OF THE PEOPLE', 46);
INSERT INTO public.chapters (id, number, text, country_id) VALUES (33, 1, 'Fake chapter', 57);


--
-- TOC entry 3199 (class 0 OID 57700)
-- Dependencies: 207
-- Data for Name: countries; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.countries (id, name, region_id) VALUES (3, 'Cameroon', 1);
INSERT INTO public.countries (id, name, region_id) VALUES (4, 'Central African Republic', 1);
INSERT INTO public.countries (id, name, region_id) VALUES (5, 'Chad', 1);
INSERT INTO public.countries (id, name, region_id) VALUES (6, 'Democratic Republic of the Congo', 1);
INSERT INTO public.countries (id, name, region_id) VALUES (7, 'Republic of the Congo', 1);
INSERT INTO public.countries (id, name, region_id) VALUES (8, 'Equatorial Guinea', 1);
INSERT INTO public.countries (id, name, region_id) VALUES (9, 'Gabon', 1);
INSERT INTO public.countries (id, name, region_id) VALUES (11, 'São Tomé and Príncipe', 1);
INSERT INTO public.countries (id, name, region_id) VALUES (12, 'Comoros', 2);
INSERT INTO public.countries (id, name, region_id) VALUES (13, 'Djibouti', 2);
INSERT INTO public.countries (id, name, region_id) VALUES (14, 'Eritrea', 2);
INSERT INTO public.countries (id, name, region_id) VALUES (15, 'Ethiopia', 2);
INSERT INTO public.countries (id, name, region_id) VALUES (2, 'Burundi', 2);
INSERT INTO public.countries (id, name, region_id) VALUES (16, 'Kenya', 2);
INSERT INTO public.countries (id, name, region_id) VALUES (17, 'Madagascar', 2);
INSERT INTO public.countries (id, name, region_id) VALUES (19, 'Mauritius', 2);
INSERT INTO public.countries (id, name, region_id) VALUES (21, 'Rwanda', 2);
INSERT INTO public.countries (id, name, region_id) VALUES (22, 'Seychelles', 2);
INSERT INTO public.countries (id, name, region_id) VALUES (23, 'Somalia', 2);
INSERT INTO public.countries (id, name, region_id) VALUES (24, 'South Sudan', 2);
INSERT INTO public.countries (id, name, region_id) VALUES (25, 'Tanzania', 2);
INSERT INTO public.countries (id, name, region_id) VALUES (26, 'Uganda', 2);
INSERT INTO public.countries (id, name, region_id) VALUES (29, 'Algeria', 3);
INSERT INTO public.countries (id, name, region_id) VALUES (30, 'Egypt', 3);
INSERT INTO public.countries (id, name, region_id) VALUES (31, 'Libya', 3);
INSERT INTO public.countries (id, name, region_id) VALUES (32, 'Mauritania', 3);
INSERT INTO public.countries (id, name, region_id) VALUES (33, 'Morocco', 3);
INSERT INTO public.countries (id, name, region_id) VALUES (34, 'Sudan', 3);
INSERT INTO public.countries (id, name, region_id) VALUES (35, 'Tunisia', 3);
INSERT INTO public.countries (id, name, region_id) VALUES (1, 'Angola', 4);
INSERT INTO public.countries (id, name, region_id) VALUES (36, 'Botswana', 4);
INSERT INTO public.countries (id, name, region_id) VALUES (37, 'Eswatini (formerly Swaziland)', 4);
INSERT INTO public.countries (id, name, region_id) VALUES (38, 'Lesotho', 4);
INSERT INTO public.countries (id, name, region_id) VALUES (18, 'Malawi', 4);
INSERT INTO public.countries (id, name, region_id) VALUES (20, 'Mozambique', 4);
INSERT INTO public.countries (id, name, region_id) VALUES (39, 'Namibia', 4);
INSERT INTO public.countries (id, name, region_id) VALUES (40, 'South Africa', 4);
INSERT INTO public.countries (id, name, region_id) VALUES (27, 'Zambia', 4);
INSERT INTO public.countries (id, name, region_id) VALUES (28, 'Zimbabwe', 4);
INSERT INTO public.countries (id, name, region_id) VALUES (41, 'Benin', 5);
INSERT INTO public.countries (id, name, region_id) VALUES (42, 'Burkina Faso', 5);
INSERT INTO public.countries (id, name, region_id) VALUES (43, 'Cape Verde', 5);
INSERT INTO public.countries (id, name, region_id) VALUES (44, 'Ivory Coast (Côte d''Ivoire)', 5);
INSERT INTO public.countries (id, name, region_id) VALUES (45, 'Gambia', 5);
INSERT INTO public.countries (id, name, region_id) VALUES (46, 'Ghana', 5);
INSERT INTO public.countries (id, name, region_id) VALUES (47, 'Guinea', 5);
INSERT INTO public.countries (id, name, region_id) VALUES (48, 'Guinea-Bissau', 5);
INSERT INTO public.countries (id, name, region_id) VALUES (49, 'Liberia', 5);
INSERT INTO public.countries (id, name, region_id) VALUES (50, 'Mali', 5);
INSERT INTO public.countries (id, name, region_id) VALUES (51, 'Niger', 5);
INSERT INTO public.countries (id, name, region_id) VALUES (52, 'Nigeria', 5);
INSERT INTO public.countries (id, name, region_id) VALUES (53, 'Senegal', 5);
INSERT INTO public.countries (id, name, region_id) VALUES (54, 'Sierra Leone', 5);
INSERT INTO public.countries (id, name, region_id) VALUES (55, 'Togo', 5);
INSERT INTO public.countries (id, name, region_id) VALUES (57, 'fake country', 5);


--
-- TOC entry 3195 (class 0 OID 57668)
-- Dependencies: 203
-- Data for Name: items; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.items (id, title, description, owner_id) VALUES (1, 'item1', 'admin item', 1);


--
-- TOC entry 3211 (class 0 OID 65927)
-- Dependencies: 219
-- Data for Name: pdf_documents; Type: TABLE DATA; Schema: public; Owner: -
--



--
-- TOC entry 3201 (class 0 OID 57718)
-- Dependencies: 209
-- Data for Name: preamble; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.preamble (id, text, country_id) VALUES (1, 'IN THE NAME OF THE ALMIGHTY GOD We the People of Ghana, IN EXERCISE of our natural and inalienable right to establish a framework of government which shall secure for ourselves and posterity the blessings of liberty, equality of opportunity and prosperity; IN A SPIRIT of friendship and peace with all peoples of the world; AND IN SOLEMN declaration and affirmation of our commitment to; Freedom, Justice, Probity and Accountability, The Principle that all powers of Government spring from the Sovereign Will of the People; The Principle of Universal Adult Suffrage; The Rule of Law; The protection and preservation of Fundamental Human Rights and Freedoms, Unity and Stability for our Nation; DO HEREBY ADOPT, ENACT AND GIVE TO OURSELVES THIS CONSTITUTION.', 46);


--
-- TOC entry 3197 (class 0 OID 57687)
-- Dependencies: 205
-- Data for Name: regions; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.regions (id, name, is_active) VALUES (1, 'Central Africa', true);
INSERT INTO public.regions (id, name, is_active) VALUES (2, 'Eastern Africa', true);
INSERT INTO public.regions (id, name, is_active) VALUES (3, 'Northern Africa', true);
INSERT INTO public.regions (id, name, is_active) VALUES (4, 'Southern Africa', true);
INSERT INTO public.regions (id, name, is_active) VALUES (5, 'West Africa', true);


--
-- TOC entry 3213 (class 0 OID 74119)
-- Dependencies: 221
-- Data for Name: reset_password_codes; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.reset_password_codes (id, code, user_id, user_email, status, date_created, date_modified) VALUES (1, 'TW5NR7LRMXA37ANPPQ640CXX6NXORARP', 2, 'admin2@test.com', true, '2023-08-25 19:34:10.381314', '2023-08-25 19:34:10.38132');
INSERT INTO public.reset_password_codes (id, code, user_id, user_email, status, date_created, date_modified) VALUES (7, 'ZB75LMOZWB33FKAYC42U81UVNYWRKSXI', 1, 'admin@test.com', true, '2023-08-25 20:54:19.273584', '2023-08-25 20:54:19.273591');


--
-- TOC entry 3221 (class 0 OID 74257)
-- Dependencies: 229
-- Data for Name: reset_password_token; Type: TABLE DATA; Schema: public; Owner: -
--



--
-- TOC entry 3215 (class 0 OID 74137)
-- Dependencies: 223
-- Data for Name: revoked_tokens; Type: TABLE DATA; Schema: public; Owner: -
--



--
-- TOC entry 3207 (class 0 OID 57775)
-- Dependencies: 215
-- Data for Name: sections; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.sections (id, country_id, chapter_id, article_id, number, text) VALUES (1, 46, 1, 1, 1, 'The Sovereignty of Ghana resides in the people of Ghana in whose name and for whose welfare the powers of government are to be exercised in the manner and within the limits laid down in this Constitution');
INSERT INTO public.sections (id, country_id, chapter_id, article_id, number, text) VALUES (6, 46, 1, 1, 2, 'This Constitution shall be the supreme law of Ghana and any other law found to be inconsistent with any provision of this Constitution shall. to the extent of the inconsistency, be void.');
INSERT INTO public.sections (id, country_id, chapter_id, article_id, number, text) VALUES (7, 46, 1, 2, 1, 'A person who alleges that –');
INSERT INTO public.sections (id, country_id, chapter_id, article_id, number, text) VALUES (8, 46, 1, 2, 2, 'The Supreme Court shall, for the purposes of a declaration under clause (1) of this article, make such orders and give such directions as it may consider appropriate for giving effect, or enabling effect to be given, to the declaration so made.');
INSERT INTO public.sections (id, country_id, chapter_id, article_id, number, text) VALUES (9, 46, 1, 2, 3, 'Any person or group of persons to whom an order or direction is addressed under clause (2) of this article by the Supreme Court, shall duly obey and carry out the terms of the order or direction.');
INSERT INTO public.sections (id, country_id, chapter_id, article_id, number, text) VALUES (11, 46, 1, 2, 5, 'A person convicted of a high crime under clause (4) of this article shall');
INSERT INTO public.sections (id, country_id, chapter_id, article_id, number, text) VALUES (10, 46, 1, 2, 4, 'Failure to obey or carry out the terms of an order or direction made or given under clause (2) of this article constitutes a high crime under this Constitution and shall, in the case of the President or the Vice-President, constitute a ground for removal from office under this Constitution.');
INSERT INTO public.sections (id, country_id, chapter_id, article_id, number, text) VALUES (13, 57, 33, 5, 1, 'Fake section text');


--
-- TOC entry 3209 (class 0 OID 57802)
-- Dependencies: 217
-- Data for Name: subsections; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.subsections (id, country_id, chapter_id, article_id, section_id, sub, text) VALUES (1, 46, 1, 2, 7, 'a', 'an enactment or anything contained in or done under the authority of that or any other enactment; or');
INSERT INTO public.subsections (id, country_id, chapter_id, article_id, section_id, sub, text) VALUES (2, 46, 1, 2, 7, 'b', 'any act or omission of any person, is inconsistent with, or is in contravention of a provision of this Constitution, may bring an action in the Supreme Court for a declaration to that effect.');


--
-- TOC entry 3219 (class 0 OID 74239)
-- Dependencies: 227
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public."user" (id, email, password, status, user_type_id) VALUES (1, 'admin@test.com', '$pbkdf2-sha256$29000$kNLa.1.Lcc6Z8x5DqHXO.Q$gxVWeBp.G9z4iq8WL1SAg7SyCFozsB9p7nfR8BeZxpY', true, 1);
INSERT INTO public."user" (id, email, password, status, user_type_id) VALUES (2, 'admin2@test.com', '$pbkdf2-sha256$29000$oDTmPKfUGsOYk9IaQ8g5hw$vMWR5RufFniz/63BslBllHqY6iTAr3qhOOSbQaUBYOk', true, 1);


--
-- TOC entry 3223 (class 0 OID 74277)
-- Dependencies: 231
-- Data for Name: user_info; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.user_info (id, user_id, first_name, middle_name, last_name) VALUES (1, 1, 'Dani', 'B', 'German');
INSERT INTO public.user_info (id, user_id, first_name, middle_name, last_name) VALUES (2, 2, 'Dani', 'G', 'German');


--
-- TOC entry 3217 (class 0 OID 74226)
-- Dependencies: 225
-- Data for Name: user_type; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.user_type (id, title) VALUES (1, 'Admin');
INSERT INTO public.user_type (id, title) VALUES (2, 'Moderator');
INSERT INTO public.user_type (id, title) VALUES (3, 'Normal');


--
-- TOC entry 3193 (class 0 OID 57655)
-- Dependencies: 201
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.users (id, email, hashed_password, is_active) VALUES (1, 'admin@test.com', 'pwdnotreallyhashed', true);


--
-- TOC entry 3246 (class 0 OID 0)
-- Dependencies: 212
-- Name: articles_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.articles_id_seq', 5, true);


--
-- TOC entry 3247 (class 0 OID 0)
-- Dependencies: 210
-- Name: chapters_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.chapters_id_seq', 33, true);


--
-- TOC entry 3248 (class 0 OID 0)
-- Dependencies: 206
-- Name: countries_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.countries_id_seq', 57, true);


--
-- TOC entry 3249 (class 0 OID 0)
-- Dependencies: 202
-- Name: items_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.items_id_seq', 1, true);


--
-- TOC entry 3250 (class 0 OID 0)
-- Dependencies: 218
-- Name: pdf_documents_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.pdf_documents_id_seq', 3, true);


--
-- TOC entry 3251 (class 0 OID 0)
-- Dependencies: 208
-- Name: preamble_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.preamble_id_seq', 2, true);


--
-- TOC entry 3252 (class 0 OID 0)
-- Dependencies: 204
-- Name: regions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.regions_id_seq', 6, true);


--
-- TOC entry 3253 (class 0 OID 0)
-- Dependencies: 220
-- Name: reset_password_codes_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.reset_password_codes_id_seq', 7, true);


--
-- TOC entry 3254 (class 0 OID 0)
-- Dependencies: 228
-- Name: reset_password_token_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.reset_password_token_id_seq', 1, false);


--
-- TOC entry 3255 (class 0 OID 0)
-- Dependencies: 222
-- Name: revoked_tokens_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.revoked_tokens_id_seq', 1, false);


--
-- TOC entry 3256 (class 0 OID 0)
-- Dependencies: 214
-- Name: sections_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.sections_id_seq', 13, true);


--
-- TOC entry 3257 (class 0 OID 0)
-- Dependencies: 216
-- Name: subsections_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.subsections_id_seq', 3, true);


--
-- TOC entry 3258 (class 0 OID 0)
-- Dependencies: 226
-- Name: user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.user_id_seq', 2, true);


--
-- TOC entry 3259 (class 0 OID 0)
-- Dependencies: 230
-- Name: user_info_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.user_info_id_seq', 2, true);


--
-- TOC entry 3260 (class 0 OID 0)
-- Dependencies: 224
-- Name: user_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.user_type_id_seq', 1, false);


--
-- TOC entry 3261 (class 0 OID 0)
-- Dependencies: 200
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.users_id_seq', 1, true);


-- Completed on 2023-08-25 21:09:34 GMT

--
-- PostgreSQL database dump complete
--
