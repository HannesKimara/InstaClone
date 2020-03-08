# Instagram Clone

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/HannesKimara/InstaClone/blob/master/LICENSE)

## Description
This app is a replica of Instagram website. Users can follow, post, comment and like photos.

## Design
#### Database Implementation(Entity Relationship Diagram)
![Entity Relation Diagram](docs/images/db_design.png)

## Getting Started
To get started run this in a virtual environment:

```bash
$ git clone https://github.com/HannesKimara/InstaClone.git
$ cd InstaClone
$ python -m pip install -r requirements.txt
```

You'll need to create a '.env' file with the following values replaced to match:
```bash
SECRET_KEY=<YOUR_SECRET_KEY>
DEBUG=<BOOL>
DISABLE_COLLECTSTATIC=1
ALLOWED_HOSTS=<YOUR_ALLOWED_HOSTS>
DATABASE_URL=<YOUR_DATABASE_URL>
```

Run migrations and start server:
```bash
$ python manage.py migrate
$ python manage.py runserver
```

## Testing
To run unittests run the following command in root directory:
```bash
$ python manage.py test
```
All tests should pass

## Author
This project was created and is maintained by Hannes Kimara

## Built with
- Python 3.7.6
- Django 3.0.3
- Materialize 1.0.0

## License
This is licensed under MIT License Copyright(2020) Hannes Kimara


