# FastAPI Endpoints

This repository contains FastAPI endpoints for managing a hierarchical structure of constitution data, including users, items, regions, countries, preambles, chapters, articles, and subsections. These endpoints allow you to create, retrieve, and manage various components of the hierarchical structure.

## Setup

1. Clone this repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Start the FastAPI app by running `uvicorn main:app --reload`.

## Endpoints

### Users

- `POST /users/`: Create a new user.
- `GET /users/`: Retrieve a list of all users.
- `GET /users/{user_id}`: Retrieve details of a specific user.
- `POST /users/{user_id}/items/`: Create an item associated with a user.

### Regions and Countries

- `POST /regions/`: Create a new region.
- `GET /regions/`: Retrieve a list of all regions.
- `GET /regions/{region_id}`: Retrieve details of a specific region.
- `POST /regions/{region_id}/country/`: Create a country associated with a region.
- `GET /countries/`: Retrieve a list of all countries.

### Preambles

- `POST /preambles/`: Create a new preamble associated with a country.
- `GET /preambles/`: Retrieve a list of preambles by country.
- `GET /preambles/{preamble_id}`: Retrieve details of a specific preamble.

### Chapters

- `POST /chapters/`: Create a new chapter associated with a country.
- `GET /chapters/`: Retrieve a list of chapters by country.
- `GET /chapters/{chapter_id}`: Retrieve details of a specific chapter.

### Articles

- `POST /articles/`: Create a new article associated with a country and chapter.
- `GET /articles/`: Retrieve a list of articles by country and chapter.
- `GET /articles/{article_id}`: Retrieve details of a specific article.

### Sections

- `POST /sections/`: Create a new subsection associated with a country, chapter, article, and section.
- `GET /sections/`: Retrieve a list of subsections by country, chapter, article, and section.
- `GET /sections/{subsection_id}`: Retrieve details of a specific subsection.

### Subsections

- `POST /subsections/`: Create a new subsection associated with a country, chapter, article, and section.
- `GET /subsections/`: Retrieve a list of subsections by country, chapter, article, and section.
- `GET /subsections/{subsection_id}`: Retrieve details of a specific subsection.

## Usage

Make API requests to the provided endpoints using your preferred API client (e.g., Postman, curl). You can interact with the hierarchical data structure to create, retrieve, and manage the components based on your application's needs.

## Contributing

Contributions are welcome! If you find any issues or want to add new features, feel free to create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

