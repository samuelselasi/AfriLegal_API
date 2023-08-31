# PDFs Router

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

pdfs of the constitution
of a particular country.


## Files

* [models.py](./models.py): Contains classes with
	                    database tables for
	                    ORM integration.
	                    Classes include:

	* `PDFDocument`-> instances:
		* id
		* title
		* content

* [schemas.py](./schemas.py): Contains classes
			      that define schemas
			      for entering into
			      database tables.
			      Classes include:

	* `PDFBase` -> instances:
		* `title`: str

	* `PDFCreate` -> instances:
		* `content`: bytes

	* `Country` -> instances:
		* `id`: int
		* `region_id`: int

	* `PDF` -> instances:
                * `id`: int

* [crud.py](./crud.py): Contains functions that
			creates, reads, updates
			and deletes pdfs.
			They include:
	* get_pdf_id
	* get_pdf_title
	* create_pdf

* [main.py](./main.py): Contains functions that
			defines enpoints to call
			**CRUD** functions. They
			include:

	* `get_pdf_by_id`
	* `get_pdf_by_title`
	* `upload_pdf`

## Endpoints

* **GET**: `/download_pdf/{pdf_id}/`
* **GET**: `/download_pdf/pdf_title`
* **POST**: `/upload_pdf`
