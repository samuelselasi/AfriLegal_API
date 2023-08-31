# AfriLegal API
***Accessible Constitution API for African Countries***

## Content

* [About](#about)
* [Installation](#installation)
* [Usage](#usage)
* [Features](#features)
* [Contributing](#contributing)
* [License](#license)
* [Authors](#authors)


## About

The AfriLegal API is a powerful tool that brings
legal information closer to diverse users,
fostering legal awareness, informed decision-making,
and supporting research efforts. Here's how
different user groups can benefit from this API:

### Tourists and Travelers

For tourists and travelers visiting African countries,
the AfriLegal API offers a valuable resource to
understand local laws and regulations. By providing
easy access to constitution texts, the API empowers
tourists to navigate legal requirements during their
journeys, ensuring a respectful and compliant experience.

### Residents and Citizens

Residents and citizens of African nations can utilize
the AfriLegal API to deepen their understanding of
their country's constitutional laws. The API's
structured organization allows users to explore
chapters, articles, sections, and subsections,
facilitating access to legal information that may
impact their daily lives.

### Travel Agencies and Hospitality

Travel agencies and hospitality services catering to
African destinations can integrate the AfriLegal API
to enhance their offerings. By incorporating accurate
legal insights into their packages, itineraries, and
services, these businesses can ensure their clients
are well-informed about local regulations and cultural
nuances.

### Legal Researchers and Scholars

For legal researchers, scholars, and educators interested
in African constitutional law, the AfriLegal API provides
a comprehensive and easily accessible database. Researchers
can analyze constitution texts, compare legal frameworks
across countries, and draw insights for academic work
and policymaking.

### Government and Tourism Departments

Government bodies and tourism departments can leverage the
AfriLegal API to promote legal awareness and responsible tourism.
By integrating API data into official websites, government
platforms, and tourism materials, they enable both citizens
and visitors to understand the legal foundations of their
destination.

### Developers and Tech Enthusiasts

Developers and tech enthusiasts looking to integrate legal
data into applications, websites, or research projects can
harness the AfriLegal API's structured endpoints. The API
simplifies data retrieval, enabling developers to create
innovative tools that utilize legal information to address
various needs.

### Universal Relevance

While the AfriLegal API focuses on African constitutional
laws, its impact transcends geographic boundaries. It
serves as a bridge between legal text and a diverse
range of users, making legal information approachable
and understandable globally.

### Ethical Consideration

As you use the AfriLegal API, ensure that the information
is used ethically and responsibly. Respect copyright and
data usage guidelines while utilizing the API to empower
individuals with legal knowledge.

The AfriLegal API opens doors to legal understanding for
various user groups, aligning with the project's mission
to democratize legal information and promote legal
literacy across continents.


## Installation

Please refer to the [backend](./backend)
repository for detailed information on
installation and environment requirements.

## Usage

Getting started with the AfriLegal API is straightforward.
Follow these steps to access and utilize its features:

### 1. API Endpoint
The base URL for accessing the AfriLegal API is:

##### http://100.26.231.45:89

To access the swagger ui of the endpoints add `/docs`:

##### http://100.26.231.45:89/docs

### 2. Making API Requests
You can make HTTP requests to the API using various
programming languages and tools. Here's an example
using `curl` command-line tool:

```
curl "http://100.26.231.45:89/get_preambles?country_id=46"
```
This example returns the preamble of the constitution for
country with id of 46

### 3. Responses
API responses are returned in JSON format, which is a
structured and easily parsable data format. You can use
libraries in your preferred programming language to handle
JSON responses.

### 4. Authentication
If you're accessing restricted endpoints that require
authentication, include the necessary authentication token or
credentials in your request headers. Refer to the
[documentation](http://3.90.70.66:5005/afrilegal-api-documentation/)
for specific endpoints that require
authentication.

### 5. Error Handling
In case of errors, the API will provide appropriate HTTP status
codes along with error messages in the response body. Always check
the response status code and content to handle errors gracefully in
your application.

### 6. Documentation
For more detailed information on available endpoints, request parameters,
and response formats, refer to our
[Technical Documentation page](http://3.90.70.66:5005/afrilegal-api-documentation/).
The documentation provides usage examples and guidelines for
various use cases.


## Features

### Constitution Data API

- Access constitution data for African countries.
- Read and search constitution text by chapters, articles, sections, and subsections based on keywords.
- Administarative options to add, update and delete constitution data.
- Option to download constitution data in PDF format.

### User Module and Authentication

- User authentication system with role-based access control.
- Three user roles: admin, moderators, and normal users.
- Secure login functionality for all user roles.
- Password reset feature using email verification and code-based reset.

### Technical Documentation Landing Page

- Landing page providing comprehensive technical documentation.
- Accessible information about API endpoints, data structures, and usage examples.
- Direct link to access the API services.
- Contact information for getting in touch with the project maintainers.

### Additional Features

- Clean code with PEP8 standard organization.
- Well structured PostgreSQL database server.
- Documented functions and classes for easy understanding and continuation.
- Oh and obviously BUGS! Yeah, they're new features if you find them (*none as of now though*).


## Contributing

##### Master Branch
The `master` branch represents the main
codebase and should always contain stable
and production-ready code. Developers
should avoid directly committing
changes to this branch to maintain
its integrity.

##### Feature Branches
When working on a new feature, bug fix,
or improvement, developers create a new
branch from the "master" branch.
This branch is often named after the
feature or issue being addressed.

##### Code Development
Developers work in their respective feature
branches to implement and test the
changes related to their assigned
tasks. Frequent commits are made to
track progress.

##### Pull Requests (PRs)
Once a feature or bug fix is complete,
the developer creates a pull request
from their feature branch to the `master`
branch. The pull request includes a
summary of changes, the purpose of the
code, and any relevant details.

##### Code Review
Team members or designated reviewers review
the code changes in the pull request. They
provide feedback, suggest improvements,
and ensure code quality and best practices.

##### Continuous Integration (CI)
Automated tests and checks are run as part
of the CI process to verify that the new code
integrates smoothly with the existing
codebase and passes all necessary tests.

##### Merging
After the pull request is approved and any
requested changes are addressed, the code
is merged into the `master` branch. This
integration brings the new feature or
fix into the main codebase.

##### Tagging and Releases
Once a set of features or bug fixes is
merged into the `master` branch, a
release may be created by tagging the
commit with a version number. This
helps track and manage different
versions of the software.

##### Branch Cleanup
After successful merging, feature
branches are usually deleted to keep
the repository organised and avoid
clutter.

***By following this branching and merging process,
teams can collaborate effectively, maintain a stable
main codebase, and ensure that new code additions
are well-tested and thoroughly reviewed before
becoming part of the production code.***


## Licence

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

## Authors

* [Samuel Selasi K.](https://github.com/samuelselasi) -> [linkedin](https://www.linkedin.com/in/samuel-selasi-kporvie), [Medium](https://medium.com/@onepunchcoder), [x](https://twitter.com/selskvie)
* [Yasmine Ben Ali]() -> [linkedin](), [x]()
