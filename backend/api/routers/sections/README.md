# Sections Router

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

sections of the constitution
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


* [crud.py](./crud.py): Contains functions that
			reads from routers.
			They include:
	* get_section
	* get_sections_by_country
	* get_sections_by_country_and_chapter
	* get_sections_by_country_and_chapter_and_article
	* create_section
	* update_section
	* delete_section


* [main.py](./main.py): Contains functions that
			defines enpoints to call
			**CRUD** functions. They
			include:

	* `read_sections_by_country`
	* `read_sections_by_country_and_chapter`
	* `read_sections_by_country_chapter_article`
	* `read_section`
	* `create_section_for_country_chapter_article`
	* `update_section`
	* `delete_section`


## Endpoints

* **GET**: `/get_section_by_country/{country_id}`
* **GET**: `/get_section_by_country_and_chapter/{country_id}/{chapter_id}`
* **GET**: `/get_section/{country_id}/{chapter_id}/{article_id}`
* **GET**: `/read_section/{section_id}`
* **POST**: `/create_section/{country_id}/{chapter_id}/{article_id}`
* **PUT**: `/update_section/{section_id}`
* **DELETE**: `/delete_section/{section_id}`
