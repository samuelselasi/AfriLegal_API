# Articles Router

## Content

* [About](#about)
* [Files](#files)
* [Endpoints](#endpoints)


## About

This router contains files for handling
endpoints that:

* Reads -> `GET`),
* Creates -> `POST`,
* Updates -> `PUT` or `PATCH` *and*
* Deletes -> `DELETE`

articles of the constitution
of a particular country.


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

* [crud.py](./crud.py): Contains functions that
			creates, reads, updates
			and deletes articles.
			They include:
	* get_article
	* get_articles_by_country_and_chapter
	* create_article
	* update_article
	* delete_article
* [main.py](./main.py): Contains functions that
			defines enpoints to call
			**CRUD** functions. They
			include:

	* `read_articles_by_country_and_chapter`
	* `read_article`
	* `create_article_for_country_and_chapter`
	* `update_article`
	* `delete_article`


## Endpoints

* **GET**: `/get_articles`
* **GET**: `/get_article/{article_id}`
* **POST**: `/create_article/{country_id}/{chapter_id}`
* **PUT**: `/update_article/{article_id}`
* **DELETE**: `/delete_article/{article_id}`

***fin***
