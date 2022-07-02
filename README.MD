## Demo
Demo available at [tda.mlab.pp.ua](https://tda.mlab.pp.ua)<br/>
Api documentation at [tda-api.mlab.pp.ua/docs](https://tda-api.mlab.pp.ua/docs)

## How to run
### With Docker
1. Edit docker-compose.yml with urls and ports for frontend if necessary or leave localhost.
```yaml
...
      args: 
        - apiUrl=http://<IP address>:5063/
        - mediaUrl=http://<IP address>:5063/static/
...
```
2. Uncomment volumes if you want to saving app data.
```yaml
...
    # volumes:
    #     - ./data/db:/code/server/db
    #     - ./data/logs:/code/server/logs
    #     - ./data/media:/code/server/static
...
```
3. Run docker-compose <br/>
`sudo docker-compose up -d`
4. In case with empty or not exist db. (it already exists in the repository, but just in case)<br/>
`http://<backend IP>:<backend port>/shops/makeshops` 

### Without Docker
#### Backend

Requirements to run: Python

1. Open your terminal in `backend` folder. <br/>
2. Install virtual environment. <br/>
`python3 -m venv env`<br/>
3. Activate virtual environment.<br/>
`source env/bin/activate` on linux or `env\Scripts\activate` on windows<br/>
4. Install requirement packages.<br/>
`pip install -r requirements.txt`<br/>
5. Run application.<br/>
`python3 asgi.py`<br/>
6. Visit documentation page.
`http://<IP address>:5000/docs`
7. In case with empty or not exist db. (it already exists in the repository, but just in case)<br/>
`http://<backend IP>:<backend port>/shops/makeshops` 

*For Windows you may need run this command: `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` before activate virtual environment*

#### Frontend

Requirements to run: Node.js, Yarn

1. Open your terminal in `frontend` folder. <br/>
2. Run yarn install. <br/>
`yarn install` or just `yarn`<br/>
5. Run application.<br/>
`yarn serve`<br/>