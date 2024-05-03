from flask import Blueprint, request
from src.services.ProveedorService import ProveedorService
from src.models.proveedorModel import Proveedor


main2 = Blueprint('proveedor_blueprint',__name__)

@main2.route('/',methods=['GET','POST'])
def get_proveedor():

  Nombre_Proveedor = request.json['Nombre_Proveedor']
  direccion = request.json['direccion']
  telefono = request.json['telefono']

  print(Nombre_Proveedor)
  print(direccion)
  print(telefono)

  proveedor = Proveedor(0, Nombre_Proveedor, direccion, telefono)

  if request.method == 'GET':
    get_proveedor= ProveedorService.get_proveedor()
    if get_proveedor:
      return 'Lista de Proveedores actualizada'
    else:
      return 'No se pudo actualizar la Lista de Proveedores'

  elif request.method == 'POST':
    post_proveedor= ProveedorService.post_proveedor(proveedor)
    if post_proveedor:
      return 'Proveedor agregado con exito'
    else:
      return 'No se pudo agregar el Proveedor a la Lista de Proveedores'

@main2.route('/', methods=['PUT', 'DELETE'])
def actualizar_eliminar_proveedor():
    ID_Proveedor = request.json['ID_Proveedor']
    Nombre_Proveedor = request.json['Nombre_Proveedor']
    direccion = request.json['direccion']
    telefono = request.json['telefono']
    
        
    proveedor = Proveedor(ID_Proveedor, Nombre_Proveedor, direccion, telefono)
   
    if request.method == 'PUT':
       put_proveedor = ProveedorService.put_proveedor(ID_Proveedor, proveedor)
       if put_proveedor:
           return 'Proveedor editado correctamente'  
       else:
           return 'No se pudo editar el Proveedor'
    
    elif request.method == 'DELETE':
        delete_proveedor = ProveedorService.delete_proveedor(ID_Proveedor)
        if delete_proveedor:
            return 'Proveedor eliminado correctamente'
        else:
            return 'No se pudo eliminar el Proveedor'