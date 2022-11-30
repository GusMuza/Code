class Detalle:
    def __init__(self,detalleId,cantidad,precio,productoId,tarjetaId):
        self.__detalleId=detalleId
        self.__cantidad=cantidad
        self.__precio=precio
        self.__productoId=productoId
        self.__tarjetaId=tarjetaId
        
    @property
    def detalleId(self):
        return self.__detalleId
    
    @detalleId.setter
    def detalleId(self,detalleId):
        self.__detalleId = detalleId
    
    @property
    def cantidad(self):
        return self.__cantidad
    
    @cantidad.setter
    def cantidad(self,cantidad):
        self.__cantidad = cantidad
    
    @property
    def precio(self):
        return self.__precio
    
    @precio.setter
    def precio(self,precio):
        self.__precio = precio
    
    @property
    def productoId(self):
        return self.__productoId
    
    @productoId.setter
    def productoId(self,productoId):
        self.__productoId = productoId 
        
    @property
    def tarjetaId(self):
        return self.__tarjetaId
    
    @tarjetaId.setter
    def tarjetaId(self,tarjetaId):
        self.__tarjetaId = tarjetaId 
        