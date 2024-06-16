from fastapi import FastAPI
#creamos una instancia al igual que en flask
app =FastAPI()

#creamos un decorador para procesar la funcion
@app.get('/')
def hola_mundo():
    return{"Hola":"Mundos"}

#Creacion de rutas 
@app.get('/test')
def hola_mundo2():
    return{"Hello world"}

#cambio de puerto: uvicorn api:app -- port 8001
#para que el servidor se actualice constantemnete podemos utilizar: uvicorn api:app --reload

