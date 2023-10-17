from fastapi import FastAPI, APIRouter
import uvicorn

app = FastAPI()
class HelloWorld():
    def read_hello(self):
        return {"data": "Hello World2"}
    
    def read_by(self):
        return {"data": "By By"}
    
router = APIRouter()

router.add_api_route('/api/v2/hello-world', 
                     endpoint = HelloWorld().read_hello, methods=["GET"])

router.add_api_route('/api/v2/by', 
                     endpoint = HelloWorld().read_by, methods=["GET"])

app.include_router(router)

if __name__ == "__main__":
   uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)