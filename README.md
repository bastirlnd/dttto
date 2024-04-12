# DTTTO - Discord Ticket Tool Transcripts Overview
This is a pet project of mine which provides users with an overview of HTML transcripts created by the [Discord Ticket Tool Bot](https://docs.tickettool.xyz).

## Project Installation
- Run `setup.sh`
- Copy the `.env-example` to `env`
   - Add a secret key

### First run
- Run `flask db init`
- Run `flask db migrate`
- Run `flask db upgrade`
- To add an admin user run `python manage.py create_admin`

### Run application
- To run the application run `python manage.py run`