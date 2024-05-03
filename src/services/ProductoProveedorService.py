from src.database.db_mysql import get_connection
from src.models.productoProveedorModel import ProductoProveedor


class ProductoProveedorService():
  @classmethod
  def get_productoProveedor(cls):
    try:
      connection= get_connection()
      with connection.cursor() as cursor:
        cursor.execute("CALL sp_getProductoProveedor()")
        result= cursor.fetchall()
        print(result)

      connection.close()
      return 'Lista de productoProveedor Actualizada'
    except Exception as ex:
      print(ex)

  @classmethod
  def post_productoProveedor(cls, productoProveedor: ProductoProveedor):
    try:
      connection= get_connection()
      print(connection)

      with connection.cursor() as cursor:
        ID_Producto_Proveedor = productoProveedor.ID_Producto_Proveedor
        ID_Proveedor = productoProveedor.ID_Proveedor
        ID_Producto = productoProveedor.ID_Producto


        cursor.execute("CALL sp_insertProductoProveedor(%s, %s, %s)",(ID_Producto_Proveedor, ID_Proveedor, ID_Producto))
        connection.commit()

      connection.close()
      return 'Detalle producto agregado con exito'    
    except Exception as ex:
      print(ex)

  @classmethod
  def delete_producto (cls, ID_Producto_Proveedor):
    try:
      connection= get_connection()

      with connection.cursor() as cursor:
        cursor.execute("CALL sp_deleteProductoProveedor(%s)",ID_Producto_Proveedor)
        connection.commit()
      connection.close()
      return 'Detalle producto eliminado con exito'
    except Exception as ex:
      print(ex)
        
  @classmethod
  def put_producto (cls, ID_Producto_Proveedor, productoProveedor: ProductoProveedor):
    try:
      connection= get_connection()

      with connection.cursor() as cursor:
        ID_Producto_Proveedor = productoProveedor.ID_Producto_Proveedor
        ID_Proveedor = productoProveedor.ID_Proveedor
        ID_Producto = productoProveedor.ID_Producto

        cursor.execute('CALL sp_updateProductoProveedor(%s, %s, %s)',(ID_Producto_Proveedor, ID_Proveedor, ID_Producto))
        connection.commit()
      connection.close()
      return 'Detalle producto editado con exito'
    except Exception as ex:
      print(ex)
