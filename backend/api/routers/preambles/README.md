# Preambles Router

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

preambles of the constitution
of a particular country.


## Files

* [models.py](./models.py): Contains classes with
	                    database tables for
	                    ORM integration.
	                    Classes include:

	* `Region`-> instances:
		* id
		* name

	* `Country`-> instances:
		* id
		* name
		* region_id

	* `Preamble` -> instances:
		* id
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

	* `RegionBase` -> instances:
		* `name`: str

	* `RegionCreate` -> instances:
		* `RegionBase`: *pass*

	* `Region` -> instances:
		* `id`: int
		* `is_active`: bool
		* `countries`: List[Country]

	* `PreambleBase` -> instances:
		* `text`: str

	* `PreambleCreate` -> instances:
                * `PreambleBase`: *pass*

	* `Preamble` -> instances:
		* `id`: int
		* `country`: Country


* [crud.py](./crud.py): Contains functions that
			creates, reads, updates
			and deletes preambles.
			They include:
	* get_preamble
	* get_preambles_by_country
	* create_preamble
	* update_preamble
	* delete_preamble

* [main.py](./main.py): Contains functions that
			defines enpoints to call
			**CRUD** functions. They
			include:

	* `read_preambles_by_country`
	* `read_preamble`
	* `create_preamble_for_country`
	* `update_preamble`
	* `delete_preamble`


## Endpoints

* **GET**: `/get_preambles`
* **GET**: `/preambles/{preamble_id}`
* **POST**: `/create_preamble/{country_id}`
* **PUT**: `/update_preamble/{preamble_id}`
* **DELETE**: `/delete_preamble/{preamble_id}`
