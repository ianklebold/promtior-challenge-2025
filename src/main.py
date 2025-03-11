from rag_app import execute_rag_app
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

#print( execute_rag_app("When was the company founded?") )
#print( execute_rag_app("What services does Promtior offer?") )

app = FastAPI()
class SubmitQueryRequest(BaseModel):
    query_text: str

@app.get("/")
def index():
    return {"message": "Hello World"}

@app.post("/submit_query")
def submit_query_endpoint(request: SubmitQueryRequest) -> str:
    option = request.query_text
    query_response = execute_rag_app(option)
    return query_response

if __name__ == "__main__":
    port = 8000
    print("Starting server on port %d" % port)
    uvicorn.run("main:app",host="0.0.0.0", port=port)