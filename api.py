from elastic.transcript_loader import upload_alternates
from fastapi import FastAPI, Response
import requests
import typing
import validators

app = FastAPI()

def validate_url(url):
    try:
        r = requests.get(url)
        r.raise_for_status()

    except:
        return False

    return True


@app.get('/test')
def hello():
    return 'Hello World'

@app.post('/upload')
async def uploader(
    media_url: typing.Optional[str],
    srt_url: typing.Optional[str],
    response: Response,
    ):

    if not all([validate_url(media_url),validate_url(srt_url)]):
        response.status_code = 442

    return {
            'media_url': media_url,
            'srt_url': srt_url,
            }



