from elastic.elastic import Client
from elasticsearch_dsl import (
        connections,
        Index,
        Text,
        Float,
        Document,
        Nested,
        InnerDoc,
        )

from transcriptor.amazon import AmazonJob
from pathlib import Path


import typer

app = typer.Typer()

conn = connections.add_connection(conn=Client, alias='default')

class Alternate(InnerDoc):
    content = Text()

class Alternative(Document):
    content = Text()
    confidence = Float()
    alternate = Nested(Alternate)

    class Index:
        name = 'alternatives'
def upload_alternates(job_name: str, file_name: path):
    """load the key for your original transcription and the the file"""

    job = amazonjob.from_job(job_name)
    job.load_edit(file_name)

    for a in job.alternatives:

        if float(a.confidence) < 0.8:
            alt = a.find_alternates(job)
            alternate = alternate(content=alt.content)
            alternative = alternative(
                    content = a.content,
                    confidence = a.confidence,
                    alternate = alternate,
                    )
            alternative.save()

if __name__ == "__main__":
    typer.run(upload_alternates)

