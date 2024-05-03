from flask import Blueprint, request
from src.services.ProductoService import ProductoService
from src.models.productoModel import Producto


main = Blueprint('producto_blueprint',__name__)

@main.route('/',methods=['GET','POST'])
def get_producto():

  # Nombre_producto = request.json ['Nombre_producto']
  # Descripcion = request.json ['Descripcion']
  # Marca = request.json ['Marca']
  # Precio = request.json ['Precio']
  # Stock = request.json ['Stock']

  # print(Nombre_producto)
  # print(Descripcion)
  # print(Marca)
  # print(Precio)
  # print(Stock)


  # producto = Producto(0, Nombre_producto, Descripcion, Marca, Precio, Stock)

  if request.method == 'GET':
    get_producto= ProductoService.get_producto()
    if get_producto:
      print(get_producto)
      return 'Lista de Productos actualizada, mira el Terminal cari'
    else:
      return 'No se pudo actualizar la Lista de Productos'

  elif request.method == 'POST':
    post_producto= ProductoService.post_producto(producto)
    if post_producto:
      return 'Producto agregado con exito'
    else:
      return 'No se pudo agregar el Producto a la Lista de Productos'

@main.route('/', methods=['DELETE'])
def actualizar_eliminar_producto():
  try:
    ID_Producto = request.json['ID_Producto']
    delete_producto = ProductoService.delete_producto(ID_Producto)
    if delete_producto:
      return 'producto eliminado correctamente'
    else:
      return 'No se pudo eliminar el Producto'
    
  except Exception as ex:
    print(ex)