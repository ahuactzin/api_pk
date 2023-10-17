from fastapi import FastAPI, APIRouter
#from pydantic import BaseModel
import uvicorn

# class PromocashData(BaseModel):
#     Plazo: str
#     Categoria: str
#     Unidad: str
#     Edad_Solicitud: int
#     Genero: str 
#     Estado_Civil:str
#     Estudios: str
#     Fuente_Ingresos: str	
#     CP: int
#     Anos_Residencia: int
#     Tipo_Vivienda: str
#     Asentamiento: str
#     Antiguedad: int
#     Ingresos: int
#     Egresos: int
#     Ingreso_Conyuge: str
#     CP_Aval: int
#     Monto: int
#     Score_Agt: float
#     Processed: str | None = None

app = FastAPI()
class HelloWorld():
    def read_hello(self):
        return {"data": "Hello World2"}
    
    def read_by(self):
        return {"data": "By By"}
    
    def process(self, item: PromocashData):
        my_item = dict(item)
        my_item.update({'Processed':'Yes'})
        #returnvalue = {'aprove':1,'default_probability':0.1256}
        return my_item
    
router = APIRouter()

router.add_api_route('/api/v2/hello-world', 
                     endpoint = HelloWorld().read_hello, methods=["GET"])

router.add_api_route('/api/v2/by', 
                     endpoint = HelloWorld().read_by, methods=["GET"])

#router.add_api_route('/api/v2/process', 
#                     endpoint = HelloWorld().process, methods=["POST"])

app.include_router(router)

if __name__ == "__main__":
   uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)