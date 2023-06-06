class NoHaySaldoException(Exception):
    pass
class UsuarioDesactivadoException(Exception):
    pass
class EstadoNoExistenteException(Exception):
    pass
PRIMARIO="primario"
SECUNDARIO="secundario"
UNIVERSITARIO="universitario"
JUBILADO="jubilado"
PRECIO_TICKET=70
ACTIVADO="activado"
DESACTIVADO="desactivado"

DESCUENTOS = {
    PRIMARIO: 0.50*PRECIO_TICKET,
    SECUNDARIO: 0.60*PRECIO_TICKET,
    UNIVERSITARIO: 0.30*PRECIO_TICKET,
    JUBILADO: 0.25*PRECIO_TICKET,
}

class Sube():
    def __init__(self) :
        self.saldo=0
        self.grupo_beneficiario=None
        self.estado="activado"
    def obtener_precio_ticket(self):
        if self.grupo_beneficiario==PRIMARIO:
         return DESCUENTOS[PRIMARIO]
        if self.grupo_beneficiario==None:
            return PRECIO_TICKET
    def pagar_pasaje(self):
        if self.saldo<70 and self.grupo_beneficiario==None:
            raise NoHaySaldoException
        if self.estado==DESACTIVADO:
            raise UsuarioDesactivadoException
        if self.grupo_beneficiario==None :
            self.saldo-=70
        if self.grupo_beneficiario==PRIMARIO:
            self.saldo-=DESCUENTOS[PRIMARIO]
        if self.grupo_beneficiario==SECUNDARIO:
            self.saldo-=DESCUENTOS[SECUNDARIO]
    def cambiar_estado(self,estado) :
           self.estado=estado
           if estado == 'pendiente':
               raise EstadoNoExistenteException