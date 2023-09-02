# Search Router

## Content

* [About](#about)
* [Files](#files)
* [Endpoints](#endpoints)


## About

This router contains files for handling
endpoints that:

* Read -> `GET`,

from the constitution
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

	* `Subsection` -> instancs:
		* id
		* country_id
		* chapter_id
		* article_id
		* section_id
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
	* search_sections_by_keyword
	* search_subsections_by_keyword
	* search_chapters_by_keyword
	* search_articles_by_keyword


* [main.py](./main.py): Contains functions that
			defines enpoints to call
			**CRUD** functions. They
			include:

	* `search_chapters_by_keyword`
	* `search_articles_by_keyword`
	* `search_sections_by_keyword`
	* `search_subsections_by_keyword`


## Endpoints

* **GET**: `/search/chapters/`
* **GET**: `/search/articles/`
* **GET**: `/search/sections/`
* **GET**: `/search/subsections/`
