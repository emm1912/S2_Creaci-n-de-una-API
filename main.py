from fastapi import FastAPI, APIRouter, Query
app = FastAPI()

class arrayNumbers:
    #SE USO EL METODO DE SUMATORIA DE SERIE (SE DEBE TENER CUIDADO PARA SERIES MAS LARGAS YA QUE PUEDE PROVOCAR OVERFLOW DE LA MEMORIA)

    def __init__(self):
        self.router = APIRouter()
        self.router.add_api_route("/listAll", self.listAll, methods=["GET"])
        self.router.add_api_route("/extract", self.extractNumber, methods=["DELETE"])
        self.router.add_api_route("/faltante", self.calculateNumber, methods=["GET"])
        self.lst = list(range(1, 101))

    def listAll(self):
        return {"List": self.lst}

    def extractNumber(self, number: int = Query(description="Numero a extraer de la lista", gt=0, lt=101)):
        if number not in self.lst:
            return {"Error": "El numero no esta en la lista"}
        self.lst.remove(number)
        return {"Exito!": "Numero Borrado"}

    def calculateNumber(self):
        n = len(self.lst)
        total = (n + 1) * (n + 2) / 2
        sum_of_A = sum(self.lst)
        if n == 100:
            return "No hace falta ningun numero, elimine uno por favor"
        elif n != 100:
            return {"El numero faltante es": {total - sum_of_A}}


api = arrayNumbers()
app.include_router(api.router)


