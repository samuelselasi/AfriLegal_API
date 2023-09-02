# Subsections Router

## Content

* [About](#about)
* [Files](#files)
* [Endpoints](#endpoints)


## About

This router contains files for handling
endpoints that:

* Read -> `GET`,
* Create -> `POST`,
* Update -> `PUT`,
* Delete -> `DELETE`

subsections of the constitution
of a particular country based
on a keyword.


## Files

* [models.py](./models.py): Contains classes with
	                    database tables for
	                    ORM integration.
	                    Classes include:

	* `Country`-> instances:
		* id
		* name
		* region_id

	* `Chapter`-> instances:
		* id
		* number
		* text
		* country_id

	* `Article` -> instances:
		* id
		* country_id
		* chapter_id
		* number
		* title
		* text

	* `Section` -> instances:
		* id
		* country_id
		* chapter_id
		* article_id
		* number
		* text

	* `Subsection` -> instances:
		* id
		* country_id
		* chapter_id
		* article_id
		* sectoin_id
		* sub
		* text


* [schemas.py](./schemas.py): Contains classes
			      that define schemas
			      for entering into
			      database tables.
			      Classes include:

	* `CountryBase` -> instances:
		* `name`: str

	* `CountryCreate` -> instances:
		* `CountryBase`: *pass*

	* `Country` -> instances:
		* `id`: int
		* `region_id`: int

	* `ChapterBase` -> instances:
                * `number`: int
		* `text`: str

	* `ChapterCreate` -> instances:
                * `ChapterBase`: *pass*

	* `Chapter` -> instances:
		* `id`: int
		* `country`: Country

	* `ArticleBase` -> instances:
		* `number`: int
		* `title`: str
		* `text`: str

	* `ArticleCreate` -> isnstances:
		* `ArticleBase`: *pass*

	* `Article` -> instances:
		* `id`: int
		* `country`: Country
		* `chapter`: Chapter

	* `SectionBase` -> instances:
		* `number`: int
 		* `text`: str

	* `SectionCreate` -> isnstances:
		* `SectionBase`: *pass*

	* `Section` -> instances:
		* `id`: int
		* `country`: Country
		* `chapter`: Chapter
		* `article`: Article

	* `SubsectionBase` -> instances:
		* `sub`: str
		* `text`: str

	* `SubsectionCreate` -> isnstances:
		* `SubsectionBase`: *pass*

	* `Subsection` -> instances:
		* `id`: int
		* `country`: Country
		* `chapter`: Chapter
		* `article`: Article
		* `section`: Section


* [crud.py](./crud.py): Contains functions that
			reads from routers.
			They include:
	* get_subsection
	* get_subsections_by_country
	* get_subsections_by_country_chapter
	* get_subsections_by_country_chapter_article
	* get_subsections_by_country_chapter_article_section
	* create_subsection
	* update_subsection
	* delete_subsection


* [main.py](./main.py): Contains functions that
			defines enpoints to call
			**CRUD** functions. They
			include:

	* `read_subsections_by_country`
	* `read_subsections_by_country_and_chapter`
	* `read_subsections_by_country_chapter_and_article`
	* `read_subsections_by_country_chapter_article_and_section`
	* `read_subsection`
	* `create_subsection`
	* `update_subsection`
	* `delete_subsection`


## Endpoints

* **GET**: `/get_subsection_by_country/{country_id}`
* **GET**: `/get_subsection_by_cc/{country_id}/{chapter_id}`
* **GET**: `/get_subsection_by_cca/{country_id}/{chapter_id}/{article_id}`
* **GET**: `/get_subsection_by_ccas/{country}/{chapter}/{article}/{section}`
* **GET**: `/get_subsection/{subsection_id}`
* **POST**: `/create_subsection/{country}/{chapter}/{article}/{section}`
* **PUT**: `/update_subsection/{subsection_id}`
* **DELETE**: `/delete_subsection/{subsection_id}`
