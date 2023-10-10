# project-management-app-full

## Installation
- Fork and clone this repo.
- Navigate to the server directory in the repo and download dependencies for the backend server by running: 

    `pipenv install`

- Start up the virtual environment by running:

    `pipenv shell`

- Download the dependencies for the frontend client by going to the main repo directory and running:

    `npm install --prefix client`

- Now you can run the server and the client in two different terminal windows:

    `python server/app.py`

    and:
    
    `npm start --prefix client`

### Seed Database
Repo has predetermined data in the database but there is also the option to seed the db by running the seed.py file:

```
cd server
python3 seed.py
```
## Support

Send an e-mail to [raffinol.dev@gmail.com](mailto:raffinol.dev@gmail.com)
## License

This project is licensed under the terms of the [MIT](https://choosealicense.com/licenses/mit/) license.




