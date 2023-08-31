--
-- PostgreSQL database dump
--

-- Dumped from database version 13.3 (Ubuntu 13.3-1.pgdg20.04+1)
-- Dumped by pg_dump version 13.3 (Ubuntu 13.3-1.pgdg20.04+1)

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

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: articles; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.articles (
    id integer NOT NULL,
    country_id integer,
    chapter_id integer,
    number integer,
    title character varying,
    text character varying
);


--
-- Name: articles_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.articles_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: articles_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.articles_id_seq OWNED BY public.articles.id;


--
-- Name: chapters; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.chapters (
    id integer NOT NULL,
    number integer,
    text character varying,
    country_id integer
);


--
-- Name: chapters_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.chapters_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: chapters_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.chapters_id_seq OWNED BY public.chapters.id;


--
-- Name: countries; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.countries (
    id integer NOT NULL,
    name character varying,
    region_id integer
);


--
-- Name: countries_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.countries_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: countries_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.countries_id_seq OWNED BY public.countries.id;


--
-- Name: items; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.items (
    id integer NOT NULL,
    title character varying,
    description character varying,
    owner_id integer
);


--
-- Name: items_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.items_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: items_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.items_id_seq OWNED BY public.items.id;


--
-- Name: pdf_documents; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.pdf_documents (
    id integer NOT NULL,
    title character varying,
    content bytea
);


--
-- Name: pdf_documents_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.pdf_documents_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: pdf_documents_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.pdf_documents_id_seq OWNED BY public.pdf_documents.id;


--
-- Name: preamble; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.preamble (
    id integer NOT NULL,
    text character varying,
    country_id integer
);


--
-- Name: preamble_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.preamble_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: preamble_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.preamble_id_seq OWNED BY public.preamble.id;


--
-- Name: regions; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.regions (
    id integer NOT NULL,
    name character varying,
    is_active boolean
);


--
-- Name: regions_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.regions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: regions_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.regions_id_seq OWNED BY public.regions.id;


--
-- Name: reset_password_codes; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.reset_password_codes (
    id integer NOT NULL,
    code character varying,
    user_id integer,
    user_email character varying,
    status boolean NOT NULL,
    date_created timestamp without time zone,
    date_modified timestamp without time zone
);


--
-- Name: reset_password_codes_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.reset_password_codes_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: reset_password_codes_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.reset_password_codes_id_seq OWNED BY public.reset_password_codes.id;


--
-- Name: reset_password_token; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.reset_password_token (
    id integer NOT NULL,
    user_id integer,
    token character varying,
    date_created timestamp without time zone
);


--
-- Name: reset_password_token_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.reset_password_token_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: reset_password_token_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.reset_password_token_id_seq OWNED BY public.reset_password_token.id;


--
-- Name: revoked_tokens; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.revoked_tokens (
    id integer NOT NULL,
    jti character varying,
    date_created timestamp without time zone,
    date_modified timestamp without time zone
);


--
-- Name: revoked_tokens_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.revoked_tokens_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: revoked_tokens_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.revoked_tokens_id_seq OWNED BY public.revoked_tokens.id;


--
-- Name: sections; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.sections (
    id integer NOT NULL,
    country_id integer,
    chapter_id integer,
    article_id integer,
    number integer,
    text character varying
);


--
-- Name: sections_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.sections_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: sections_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.sections_id_seq OWNED BY public.sections.id;


--
-- Name: subsections; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.subsections (
    id integer NOT NULL,
    country_id integer,
    chapter_id integer,
    article_id integer,
    section_id integer,
    sub character varying,
    text character varying
);


--
-- Name: subsections_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.subsections_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: subsections_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.subsections_id_seq OWNED BY public.subsections.id;


--
-- Name: user; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public."user" (
    id integer NOT NULL,
    email character varying,
    password character varying,
    status boolean,
    user_type_id integer
);


--
-- Name: user_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.user_id_seq OWNED BY public."user".id;


--
-- Name: user_info; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.user_info (
    id integer NOT NULL,
    user_id integer,
    first_name character varying,
    middle_name character varying,
    last_name character varying
);


--
-- Name: user_info_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.user_info_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: user_info_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.user_info_id_seq OWNED BY public.user_info.id;


--
-- Name: user_type; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.user_type (
    id integer NOT NULL,
    title character varying
);


--
-- Name: user_type_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.user_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: user_type_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.user_type_id_seq OWNED BY public.user_type.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.users (
    id integer NOT NULL,
    email character varying,
    hashed_password character varying,
    is_active boolean
);


--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: -
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: -
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: articles id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.articles ALTER COLUMN id SET DEFAULT nextval('public.articles_id_seq'::regclass);


--
-- Name: chapters id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.chapters ALTER COLUMN id SET DEFAULT nextval('public.chapters_id_seq'::regclass);


--
-- Name: countries id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.countries ALTER COLUMN id SET DEFAULT nextval('public.countries_id_seq'::regclass);


--
-- Name: items id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.items ALTER COLUMN id SET DEFAULT nextval('public.items_id_seq'::regclass);


--
-- Name: pdf_documents id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.pdf_documents ALTER COLUMN id SET DEFAULT nextval('public.pdf_documents_id_seq'::regclass);


--
-- Name: preamble id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.preamble ALTER COLUMN id SET DEFAULT nextval('public.preamble_id_seq'::regclass);


--
-- Name: regions id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.regions ALTER COLUMN id SET DEFAULT nextval('public.regions_id_seq'::regclass);


--
-- Name: reset_password_codes id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reset_password_codes ALTER COLUMN id SET DEFAULT nextval('public.reset_password_codes_id_seq'::regclass);


--
-- Name: reset_password_token id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reset_password_token ALTER COLUMN id SET DEFAULT nextval('public.reset_password_token_id_seq'::regclass);


--
-- Name: revoked_tokens id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.revoked_tokens ALTER COLUMN id SET DEFAULT nextval('public.revoked_tokens_id_seq'::regclass);


--
-- Name: sections id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.sections ALTER COLUMN id SET DEFAULT nextval('public.sections_id_seq'::regclass);


--
-- Name: subsections id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.subsections ALTER COLUMN id SET DEFAULT nextval('public.subsections_id_seq'::regclass);


--
-- Name: user id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."user" ALTER COLUMN id SET DEFAULT nextval('public.user_id_seq'::regclass);


--
-- Name: user_info id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.user_info ALTER COLUMN id SET DEFAULT nextval('public.user_info_id_seq'::regclass);


--
-- Name: user_type id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.user_type ALTER COLUMN id SET DEFAULT nextval('public.user_type_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Data for Name: articles; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.articles (id, country_id, chapter_id, number, title, text) VALUES (1, 46, 1, 1, 'SUPREMACY OF THE CONSTITUTION', '');
INSERT INTO public.articles (id, country_id, chapter_id, number, title, text) VALUES (2, 46, 1, 2, 'ENFORCEMENT OF THE CONSTITUTION', '');
INSERT INTO public.articles (id, country_id, chapter_id, number, title, text) VALUES (3, 46, 1, 3, 'DEFENCE OF THE CONSTITUTION', '');
INSERT INTO public.articles (id, country_id, chapter_id, number, title, text) VALUES (5, NULL, 33, 1, 'Fake Article Title', 'Fake article text');
INSERT INTO public.articles (id, country_id, chapter_id, number, title, text) VALUES (6, 59, 34, 1, 'Updated Fake article for fake country Manchester', 'Updated Fake article text for fake country Manchester');


--
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
INSERT INTO public.chapters (id, number, text, country_id) VALUES (33, 1, 'Fake chapter', NULL);
INSERT INTO public.chapters (id, number, text, country_id) VALUES (34, 1, 'Updated fake chapter 1 for country Manchester', 59);
INSERT INTO public.chapters (id, number, text, country_id) VALUES (36, 2, 'Fake chapter 2', 59);


--
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
INSERT INTO public.countries (id, name, region_id) VALUES (59, 'Manchester', 7);
INSERT INTO public.countries (id, name, region_id) VALUES (60, 'Fake country', 7);


--
-- Data for Name: items; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.items (id, title, description, owner_id) VALUES (1, 'item1', 'admin item', 1);


--
-- Data for Name: pdf_documents; Type: TABLE DATA; Schema: public; Owner: -
--



--
-- Data for Name: preamble; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.preamble (id, text, country_id) VALUES (1, 'IN THE NAME OF THE ALMIGHTY GOD We the People of Ghana, IN EXERCISE of our natural and inalienable right to establish a framework of government which shall secure for ourselves and posterity the blessings of liberty, equality of opportunity and prosperity; IN A SPIRIT of friendship and peace with all peoples of the world; AND IN SOLEMN declaration and affirmation of our commitment to; Freedom, Justice, Probity and Accountability, The Principle that all powers of Government spring from the Sovereign Will of the People; The Principle of Universal Adult Suffrage; The Rule of Law; The protection and preservation of Fundamental Human Rights and Freedoms, Unity and Stability for our Nation; DO HEREBY ADOPT, ENACT AND GIVE TO OURSELVES THIS CONSTITUTION.', 46);
INSERT INTO public.preamble (id, text, country_id) VALUES (3, 'In the Name of God, the Merciful, the Compassionate We, the representatives of the Tunisian people, members of the National Constituent Assembly, Taking pride in the struggle of our people for independence, to build the state, for freedom from tyranny, responding to its free will, and to achieve the objectives of the revolution for freedom and dignity, the revolution of December 17, 2010 through January 14, 2011, with loyalty to the blood of our virtuous martyrs, to the sacrifices of Tunisian men and women over the course of generations, and breaking with injustice, inequity, and corruption, Expressing our people’s commitment to the teachings of Islam and its aims characterized by openness and moderation, and to the human values and the highest principles of universal human rights, and inspired by the heritage of our civilization, accumulated over the travails of our history, from our enlightened reformist movements that are based on the foundations of our Islamic-Arab identity and on the gains of human civilization, and adhering to the national gains achieved by our people, With a view to building a republican, democratic and participatory system, in the framework of a civil state founded on the sovereignty of the people, exercised through the peaceful alternation of power through free elections, and on the principle of the separation and balance of powers, which guarantees the freedom of association in conformity with the principles of pluralism, an impartial administration, and good governance, which are the foundations of political competition, where the state guarantees the supremacy of the law and the respect for freedoms and human rights, the independence of the judiciary, the equality of rights and duties between all citizens, male and female, and equality between all regions, Based on the elevated status of humankind and desirous of consolidating our cultural and civilizational affiliation to the Arab and Muslim nation, building on our national unity that is based on citizenship, fraternity, solidarity, and social justice, committed to strengthening Maghreb unity as a step towards achieving Arab unity, towards complementarity with the Muslim and African peoples, and towards cooperation with all the peoples of the world, desirous of supporting all victims of injustice, wherever they are, defending the peoples’ right to determine their own destiny, to supporting all just liberation movements, at the forefront of which is the movement for the liberation of Palestine, and opposing all forms of colonization and of racism, Being aware of the necessity of contributing to the preservation of a healthy environment that guarantees the sustainability of our natural resources and bequeathing a secure life to future generations, realizing the will of the people to be the makers of their own history, believing in science, work, and creativity as noble human values, seeking always to be pioneers, aspiring to contribute to the development of civilization, on the basis of the independence of national decision-making, world peace, and human solidarity, We, in the name of the Tunisian people, with the help of God, draft this Constitution.', 35);
INSERT INTO public.preamble (id, text, country_id) VALUES (4, 'Update test preamble for country Manchester', 59);


--
-- Data for Name: regions; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.regions (id, name, is_active) VALUES (1, 'Central Africa', true);
INSERT INTO public.regions (id, name, is_active) VALUES (2, 'Eastern Africa', true);
INSERT INTO public.regions (id, name, is_active) VALUES (3, 'Northern Africa', true);
INSERT INTO public.regions (id, name, is_active) VALUES (4, 'Southern Africa', true);
INSERT INTO public.regions (id, name, is_active) VALUES (5, 'West Africa', true);
INSERT INTO public.regions (id, name, is_active) VALUES (7, 'Renholm Region', true);


--
-- Data for Name: reset_password_codes; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.reset_password_codes (id, code, user_id, user_email, status, date_created, date_modified) VALUES (1, 'TW5NR7LRMXA37ANPPQ640CXX6NXORARP', 2, 'admin2@test.com', true, '2023-08-25 19:34:10.381314', '2023-08-25 19:34:10.38132');
INSERT INTO public.reset_password_codes (id, code, user_id, user_email, status, date_created, date_modified) VALUES (8, '002RRFECNBD37MC9GWFRK1EFFTO55MDM', NULL, 'admin3@test.com', true, '2023-08-26 11:51:16.701733', '2023-08-26 11:51:16.701746');
INSERT INTO public.reset_password_codes (id, code, user_id, user_email, status, date_created, date_modified) VALUES (10, '8EQHUTN9L14X1H2QO1DM1T12IMUSEP76', NULL, 'admin@test.com', true, '2023-08-28 19:31:04.627058', '2023-08-28 19:31:04.627073');


--
-- Data for Name: reset_password_token; Type: TABLE DATA; Schema: public; Owner: -
--



--
-- Data for Name: revoked_tokens; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.revoked_tokens (id, jti, date_created, date_modified) VALUES (1, 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImFkbWluQHRlc3QuY29tIiwiaWQiOjEsImV4cCI6MTY5MzIzODEzOX0.exF513J5r6FFq_FVc7WdrVL_FniXKcN9R8KMZFYx2Xc', '2023-08-28 15:26:05.219373', '2023-08-28 15:26:05.219382');
INSERT INTO public.revoked_tokens (id, jti, date_created, date_modified) VALUES (2, 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImFkbWluQHRlc3QuY29tIiwiaWQiOjEsImV4cCI6MTY5MzI0MTg2N30.d482JSAhXwRVAInodyCUyhKoVgICXgpsSA2Zsn-c2MM', '2023-08-28 16:28:19.772514', '2023-08-28 16:28:19.772525');
INSERT INTO public.revoked_tokens (id, jti, date_created, date_modified) VALUES (3, 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImFkbWluQHRlc3QuY29tIiwiaWQiOjEsImV4cCI6MTY5MzI0MTkwNX0.DDIdmWM1fQeXZ-ylK6i1NKuLjYc82a5obTZAg1NJlWg', '2023-08-28 16:28:45.695563', '2023-08-28 16:28:45.695575');


--
-- Data for Name: sections; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.sections (id, country_id, chapter_id, article_id, number, text) VALUES (1, 46, 1, 1, 1, 'The Sovereignty of Ghana resides in the people of Ghana in whose name and for whose welfare the powers of government are to be exercised in the manner and within the limits laid down in this Constitution');
INSERT INTO public.sections (id, country_id, chapter_id, article_id, number, text) VALUES (6, 46, 1, 1, 2, 'This Constitution shall be the supreme law of Ghana and any other law found to be inconsistent with any provision of this Constitution shall. to the extent of the inconsistency, be void.');
INSERT INTO public.sections (id, country_id, chapter_id, article_id, number, text) VALUES (7, 46, 1, 2, 1, 'A person who alleges that –');
INSERT INTO public.sections (id, country_id, chapter_id, article_id, number, text) VALUES (8, 46, 1, 2, 2, 'The Supreme Court shall, for the purposes of a declaration under clause (1) of this article, make such orders and give such directions as it may consider appropriate for giving effect, or enabling effect to be given, to the declaration so made.');
INSERT INTO public.sections (id, country_id, chapter_id, article_id, number, text) VALUES (9, 46, 1, 2, 3, 'Any person or group of persons to whom an order or direction is addressed under clause (2) of this article by the Supreme Court, shall duly obey and carry out the terms of the order or direction.');
INSERT INTO public.sections (id, country_id, chapter_id, article_id, number, text) VALUES (11, 46, 1, 2, 5, 'A person convicted of a high crime under clause (4) of this article shall');
INSERT INTO public.sections (id, country_id, chapter_id, article_id, number, text) VALUES (10, 46, 1, 2, 4, 'Failure to obey or carry out the terms of an order or direction made or given under clause (2) of this article constitutes a high crime under this Constitution and shall, in the case of the President or the Vice-President, constitute a ground for removal from office under this Constitution.');
INSERT INTO public.sections (id, country_id, chapter_id, article_id, number, text) VALUES (13, NULL, 33, 5, 1, 'Fake section text');


--
-- Data for Name: subsections; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.subsections (id, country_id, chapter_id, article_id, section_id, sub, text) VALUES (1, 46, 1, 2, 7, 'a', 'an enactment or anything contained in or done under the authority of that or any other enactment; or');
INSERT INTO public.subsections (id, country_id, chapter_id, article_id, section_id, sub, text) VALUES (2, 46, 1, 2, 7, 'b', 'any act or omission of any person, is inconsistent with, or is in contravention of a provision of this Constitution, may bring an action in the Supreme Court for a declaration to that effect.');


--
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public."user" (id, email, password, status, user_type_id) VALUES (1, 'admin@test.com', '$pbkdf2-sha256$29000$kNLa.1.Lcc6Z8x5DqHXO.Q$gxVWeBp.G9z4iq8WL1SAg7SyCFozsB9p7nfR8BeZxpY', true, 1);
INSERT INTO public."user" (id, email, password, status, user_type_id) VALUES (2, 'admin2@test.com', '$pbkdf2-sha256$29000$oDTmPKfUGsOYk9IaQ8g5hw$vMWR5RufFniz/63BslBllHqY6iTAr3qhOOSbQaUBYOk', true, 1);
INSERT INTO public."user" (id, email, password, status, user_type_id) VALUES (3, 'admin3@test.com', '$pbkdf2-sha256$29000$QwjBOGdMCUEoJcR4b03JmQ$Ygj8DQqwFeC8Dj6rooI5vlzfTRf7mP/8.Z6vq/efjZE', true, 1);


--
-- Data for Name: user_info; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.user_info (id, user_id, first_name, middle_name, last_name) VALUES (1, 1, 'Dani', 'B', 'German');
INSERT INTO public.user_info (id, user_id, first_name, middle_name, last_name) VALUES (2, 2, 'Dani', 'G', 'German');
INSERT INTO public.user_info (id, user_id, first_name, middle_name, last_name) VALUES (3, 3, NULL, NULL, NULL);


--
-- Data for Name: user_type; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.user_type (id, title) VALUES (1, 'Admin');
INSERT INTO public.user_type (id, title) VALUES (2, 'Moderator');
INSERT INTO public.user_type (id, title) VALUES (3, 'Normal');


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: -
--

INSERT INTO public.users (id, email, hashed_password, is_active) VALUES (1, 'admin@test.com', 'pwdnotreallyhashed', true);


--
-- Name: articles_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.articles_id_seq', 6, true);


--
-- Name: chapters_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.chapters_id_seq', 36, true);


--
-- Name: countries_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.countries_id_seq', 60, true);


--
-- Name: items_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.items_id_seq', 1, true);


--
-- Name: pdf_documents_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.pdf_documents_id_seq', 4, true);


--
-- Name: preamble_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.preamble_id_seq', 5, true);


--
-- Name: regions_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.regions_id_seq', 8, true);


--
-- Name: reset_password_codes_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.reset_password_codes_id_seq', 10, true);


--
-- Name: reset_password_token_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.reset_password_token_id_seq', 1, false);


--
-- Name: revoked_tokens_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.revoked_tokens_id_seq', 3, true);


--
-- Name: sections_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.sections_id_seq', 13, true);


--
-- Name: subsections_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.subsections_id_seq', 3, true);


--
-- Name: user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.user_id_seq', 3, true);


--
-- Name: user_info_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.user_info_id_seq', 3, true);


--
-- Name: user_type_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.user_type_id_seq', 1, false);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: -
--

SELECT pg_catalog.setval('public.users_id_seq', 1, true);


--
-- Name: articles articles_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.articles
    ADD CONSTRAINT articles_pkey PRIMARY KEY (id);


--
-- Name: chapters chapters_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.chapters
    ADD CONSTRAINT chapters_pkey PRIMARY KEY (id);


--
-- Name: countries countries_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.countries
    ADD CONSTRAINT countries_pkey PRIMARY KEY (id);


--
-- Name: items items_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.items
    ADD CONSTRAINT items_pkey PRIMARY KEY (id);


--
-- Name: pdf_documents pdf_documents_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.pdf_documents
    ADD CONSTRAINT pdf_documents_pkey PRIMARY KEY (id);


--
-- Name: preamble preamble_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.preamble
    ADD CONSTRAINT preamble_pkey PRIMARY KEY (id);


--
-- Name: regions regions_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.regions
    ADD CONSTRAINT regions_pkey PRIMARY KEY (id);


--
-- Name: reset_password_codes reset_password_codes_code_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reset_password_codes
    ADD CONSTRAINT reset_password_codes_code_key UNIQUE (code);


--
-- Name: reset_password_codes reset_password_codes_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reset_password_codes
    ADD CONSTRAINT reset_password_codes_pkey PRIMARY KEY (id);


--
-- Name: reset_password_codes reset_password_codes_user_email_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reset_password_codes
    ADD CONSTRAINT reset_password_codes_user_email_key UNIQUE (user_email);


--
-- Name: reset_password_codes reset_password_codes_user_id_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reset_password_codes
    ADD CONSTRAINT reset_password_codes_user_id_key UNIQUE (user_id);


--
-- Name: reset_password_token reset_password_token_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reset_password_token
    ADD CONSTRAINT reset_password_token_pkey PRIMARY KEY (id);


--
-- Name: reset_password_token reset_password_token_user_id_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reset_password_token
    ADD CONSTRAINT reset_password_token_user_id_key UNIQUE (user_id);


--
-- Name: revoked_tokens revoked_tokens_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.revoked_tokens
    ADD CONSTRAINT revoked_tokens_pkey PRIMARY KEY (id);


--
-- Name: sections sections_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.sections
    ADD CONSTRAINT sections_pkey PRIMARY KEY (id);


--
-- Name: subsections subsections_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.subsections
    ADD CONSTRAINT subsections_pkey PRIMARY KEY (id);


--
-- Name: user_info user_info_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.user_info
    ADD CONSTRAINT user_info_pkey PRIMARY KEY (id);


--
-- Name: user_info user_info_user_id_key; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.user_info
    ADD CONSTRAINT user_info_user_id_key UNIQUE (user_id);


--
-- Name: user user_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (id);


--
-- Name: user_type user_type_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.user_type
    ADD CONSTRAINT user_type_pkey PRIMARY KEY (id);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: ix_articles_id; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_articles_id ON public.articles USING btree (id);


--
-- Name: ix_articles_title; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_articles_title ON public.articles USING btree (title);


--
-- Name: ix_chapters_id; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_chapters_id ON public.chapters USING btree (id);


--
-- Name: ix_countries_id; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_countries_id ON public.countries USING btree (id);


--
-- Name: ix_countries_name; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_countries_name ON public.countries USING btree (name);


--
-- Name: ix_items_description; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_items_description ON public.items USING btree (description);


--
-- Name: ix_items_id; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_items_id ON public.items USING btree (id);


--
-- Name: ix_items_title; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_items_title ON public.items USING btree (title);


--
-- Name: ix_pdf_documents_id; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_pdf_documents_id ON public.pdf_documents USING btree (id);


--
-- Name: ix_preamble_id; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_preamble_id ON public.preamble USING btree (id);


--
-- Name: ix_regions_id; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_regions_id ON public.regions USING btree (id);


--
-- Name: ix_regions_name; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX ix_regions_name ON public.regions USING btree (name);


--
-- Name: ix_reset_password_codes_id; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_reset_password_codes_id ON public.reset_password_codes USING btree (id);


--
-- Name: ix_reset_password_token_id; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_reset_password_token_id ON public.reset_password_token USING btree (id);


--
-- Name: ix_reset_password_token_token; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_reset_password_token_token ON public.reset_password_token USING btree (token);


--
-- Name: ix_sections_id; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_sections_id ON public.sections USING btree (id);


--
-- Name: ix_subsections_id; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_subsections_id ON public.subsections USING btree (id);


--
-- Name: ix_user_email; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX ix_user_email ON public."user" USING btree (email);


--
-- Name: ix_user_id; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_user_id ON public."user" USING btree (id);


--
-- Name: ix_user_info_id; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_user_info_id ON public.user_info USING btree (id);


--
-- Name: ix_user_type_id; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_user_type_id ON public.user_type USING btree (id);


--
-- Name: ix_user_type_title; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX ix_user_type_title ON public.user_type USING btree (title);


--
-- Name: ix_users_email; Type: INDEX; Schema: public; Owner: -
--

CREATE UNIQUE INDEX ix_users_email ON public.users USING btree (email);


--
-- Name: ix_users_id; Type: INDEX; Schema: public; Owner: -
--

CREATE INDEX ix_users_id ON public.users USING btree (id);


--
-- Name: articles articles_chapter_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.articles
    ADD CONSTRAINT articles_chapter_id_fkey FOREIGN KEY (chapter_id) REFERENCES public.chapters(id);


--
-- Name: articles articles_country_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.articles
    ADD CONSTRAINT articles_country_id_fkey FOREIGN KEY (country_id) REFERENCES public.countries(id);


--
-- Name: chapters chapters_country_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.chapters
    ADD CONSTRAINT chapters_country_id_fkey FOREIGN KEY (country_id) REFERENCES public.countries(id);


--
-- Name: countries countries_region_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.countries
    ADD CONSTRAINT countries_region_id_fkey FOREIGN KEY (region_id) REFERENCES public.regions(id);


--
-- Name: items items_owner_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.items
    ADD CONSTRAINT items_owner_id_fkey FOREIGN KEY (owner_id) REFERENCES public.users(id);


--
-- Name: preamble preamble_country_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.preamble
    ADD CONSTRAINT preamble_country_id_fkey FOREIGN KEY (country_id) REFERENCES public.countries(id);


--
-- Name: reset_password_token reset_password_token_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.reset_password_token
    ADD CONSTRAINT reset_password_token_user_id_fkey FOREIGN KEY (user_id) REFERENCES public."user"(id);


--
-- Name: sections sections_article_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.sections
    ADD CONSTRAINT sections_article_id_fkey FOREIGN KEY (article_id) REFERENCES public.articles(id);


--
-- Name: sections sections_chapter_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.sections
    ADD CONSTRAINT sections_chapter_id_fkey FOREIGN KEY (chapter_id) REFERENCES public.chapters(id);


--
-- Name: sections sections_country_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.sections
    ADD CONSTRAINT sections_country_id_fkey FOREIGN KEY (country_id) REFERENCES public.countries(id);


--
-- Name: subsections subsections_article_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.subsections
    ADD CONSTRAINT subsections_article_id_fkey FOREIGN KEY (article_id) REFERENCES public.articles(id);


--
-- Name: subsections subsections_chapter_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.subsections
    ADD CONSTRAINT subsections_chapter_id_fkey FOREIGN KEY (chapter_id) REFERENCES public.chapters(id);


--
-- Name: subsections subsections_country_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.subsections
    ADD CONSTRAINT subsections_country_id_fkey FOREIGN KEY (country_id) REFERENCES public.countries(id);


--
-- Name: subsections subsections_section_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.subsections
    ADD CONSTRAINT subsections_section_id_fkey FOREIGN KEY (section_id) REFERENCES public.sections(id);


--
-- Name: user_info user_info_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.user_info
    ADD CONSTRAINT user_info_user_id_fkey FOREIGN KEY (user_id) REFERENCES public."user"(id);


--
-- Name: user user_user_type_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_user_type_id_fkey FOREIGN KEY (user_type_id) REFERENCES public.user_type(id);


--
-- PostgreSQL database dump complete
--
