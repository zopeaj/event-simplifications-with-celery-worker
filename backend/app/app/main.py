from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config.settings import Setting


origins = [

] + Setting.getOrigins()

app = FastAPI()

app.add_middleware(CORSMiddleware([

]))
