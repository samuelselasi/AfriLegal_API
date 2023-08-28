# Chapters Router

## Content

* [About](#about)
* [Files](#files)
* [Endpoints](#endpoints)


## About

This router contains files for handling
endpoints that:

* Reads -> `GET`,
* Creates -> `POST`,
* Updates -> `PUT` or `PATCH` and
* Deletes -> `DELETE`

chapters of the constitution
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

* [crud.py](./crud.py): Contains functions that
			creates, reads, updates
			and deletes chapters.
			They include:
	* get_chapter
	* get_chapters_by_country
	* create_chapter
	* update_chapter
	* delete_chapter

* [main.py](./main.py): Contains functions that
			defines enpoints to call
			**CRUD** functions. They
			include:

	* `read_chapters_by_country`
	* `read_chapter`
	* `create_chapter_for_country`
	* `update_chapter`
	* `delete_chapter`


## Endpoints

* **GET**: `/get_chapters`
* **GET**: `/get_chapter/{chapter_id}`
* **POST**: `/create_chapter/{country_id}`
* **PUT**: `/update_chapter/{chapter_id}`
* **DELETE**: `/delete_chapter/{chapter_id}`
