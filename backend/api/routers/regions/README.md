# Regions Router

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

various regions of the African
continent.


## Files

* [models.py](./models.py): Contains classes with
	                    database tables for
	                    ORM integration.
	                    Classes include:

	* `Refion`-> instances:
		* id
		* name
		* is_active

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

	* `Region_` -> instances:
		* `id`: int

* [crud.py](./crud.py): Contains functions that
			creates, reads, updates
			and deletes articles.
			They include:
	* get_region_by_id
	* get_region_by_name
	* get_regions_and_countries
	* get_regions
	* create_region
	* update_region
	* delete_region

* [main.py](./main.py): Contains functions that
			defines enpoints to call
			**CRUD** functions. They
			include:

	* `read_regions`
	* `read_regions_and_countries`
	* `read_region_id`
	* `read_region_name`
	* `create_region`
	* `update_region`
	* `delete_region`


## Endpoints

* **GET**: `/get_regions`
* **GET**: `/get_regions_countries`
* **GET**: `/get_region_by_id/{region_id}`
* **GET**: `/get_region_by_name/region_name`
* **POST**: `/create_region`
* **PUT**: `/update_region/{region_id}`
* **DELETE**: `/delete_region/{region_id}`
