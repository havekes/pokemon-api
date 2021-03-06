# pokemon-api

Exposes pokemons from a csv file as a CRUD API.
Changes that are made to the database can be exported back to csv.

## Get started

You must have Python 3.9 installed and the `virtualenv` package.

To start working on the project:

```bash
# Create a new virtualenv
virtualenv .venv
# Activate the virtualenv
source .venv/bin/activate
# Install dependencies
pip install -r requirements.txt
# Run Django migrations
python manage.py migrate
```

Running the migrations will import the content of the `pokemon.csv` file into the database.

Then you can start the Django dev server as usual with
```bash
python manage.py runserver
```

## Testing

Tests can be run using `tox`.

If all you need is to run the tests (in a CI environement for instance), you only need to the the following
```bash
# Globally install tox
pip install tox
# Tox will create the testing environment automatically
tox
```

## Exporting

Pokemons can be exported to the original csv format using this Django admin command
```bash
python manage.py export_pokemons [dest_path]
```
