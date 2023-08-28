# Countries Router

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

countries of the African continent
of a particular region.


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
		* `countries`: List[Country] - []

* [crud.py](./crud.py): Contains functions that
			creates, reads, updates
			and deletes countries.
			They include:
	* get_countries
	* get_country
	* create_region_country
	* update_country
	* delete_country

* [main.py](./main.py): Contains functions that
			defines enpoints to call
			**CRUD** functions. They
			include:

	* `read_countries`
	* `read_country`
	* `create_country_for_region`
	* `update_country`
	* `delete_country`


## Endpoints

* **GET**: `/get_countries`
* **GET**: `/get_country/{country_id}`
* **POST**: `/create_country/{region_id}`
* **PUT**: `/update_country/{country_id}`
* **DELETE**: `/delete_country/{country_id}`
