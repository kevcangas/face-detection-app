#uvicorn
import uvicorn


#api
from api.api import api
from webpage.webpage import webpage


#fastapi
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles


#Function to start the app
def start_application():
	app = FastAPI()

	#Parts of the app
	app.include_router(api)
	app.include_router(webpage)

	#Directory where the static files can be request
	app.mount("/static", app=StaticFiles(directory="webpage/static"), name="static") 
	return app


app = start_application()


def run():
	config = uvicorn.Config("__main__:app", port=8000, host="0.0.0.0", log_level="info", reload='True')
	server = uvicorn.Server(config)
	server.run()


if __name__ == '__main__':
	run()