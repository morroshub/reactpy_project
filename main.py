from reactpy import component, html, hooks
from reactpy.backend.fastapi import configure
from fastapi import FastAPI

#colocar otros componentes en otros archivos por principio solid 

@component
def Item(text, initial_done=False):
    done, set_done = hooks.use_state(initial_done) #agregamos condicion de estado

    def handle_click(event):
        set_done(not done)
    

    attrs = { "style": {"color": "green"}} if done else {}


    if done:
        return html.li(attrs, text)
    else:
        return html.li(
            html.span(attrs,text),
            html.button({ "on_click": handle_click }, "Confirmar!")
        )
            

@component
def HelloWorld(): 
    return html.div(
        html.h1("Lista de pendientes"),
        html.ul(
            Item("Componente externo"),
            Item("Prueba 2"),
            Item("Si sale verde apagamos", initial_done=True)
        )) 

app = FastAPI()
configure(app, HelloWorld)