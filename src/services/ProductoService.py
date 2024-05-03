from src.database.db_mysql import get_connection
from src.models.productoModel import Producto


class ProductoService():
  @classmethod
  def get_producto(cls):
    try:
      connection= get_connection()
      with connection.cursor() as cursor:
        cursor.execute("CALL sp_getProducto()")
        result= cursor.fetchall()
        print(result)

      connection.close()
      return 'Lista de producto Actualizada'
    except Exception as ex:
      print(ex)

  @classmethod
  def post_producto(cls, producto: Producto):
    try:
      connection= get_connection()
      print(connection)

      with connection.cursor() as cursor:
        ID_Producto = producto.ID_Producto
        Nombre_producto = producto.Nombre_producto
        Descripcion = producto.Descripcion
        Marca = producto.Marca
        Precio = producto.Precio
        Stock = producto.Stock


        cursor.execute("INSERT INTO producto (ID_Producto, Nombre_producto, Descripcion, Marca, Precio, Stock) VALUES ('{0}', '{1}', '{2} ', '{3}', '{4}', '{5}');".format(ID_Producto, Nombre_producto, Descripcion, Marca, Precio, Stock))
        connection.commit()

      connection.close()
      return 'Producto agregado con exito'    
    except Exception as ex:
      print(ex)




  @classmethod
  def delete_producto (cls, ID_Producto:int):
    try:
      connection= get_connection()

      with connection.cursor() as cursor:
        cursor.execute("CALL sp_deleteProducto(%s)", ID_Producto)
        connection.commit()
      connection.close()
      return 'Producto eliminado con exito'
    except Exception as ex:
      print(ex)
        



  @classmethod
  def put_producto (cls, ID_Producto, producto: Producto):
    try:
      connection= get_connection()

      with connection.cursor() as cursor:
        Nombre_producto = producto.Nombre_producto
        Descripcion = producto.Descripcion
        Marca = producto.Marca
        Precio = producto.Precio
        Stock = producto.Stock

        cursor.execute("UPDATE producto SET Nombre_producto = %s, Descripcion = %s, Marca = %s, Precio = %s, Stock = %s WHERE ID_Producto = %s;", (Nombre_producto, Descripcion, Marca, Precio, Stock, ID_Producto))
        connection.commit()
      connection.close()
      return 'Producto editado con exito'
    except Exception as ex:
      print(ex)
