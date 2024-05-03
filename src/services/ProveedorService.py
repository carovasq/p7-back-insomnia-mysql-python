from src.database.db_mysql import get_connection
from src.models.proveedorModel import Proveedor


class ProveedorService():
  @classmethod
  def get_proveedor(cls):
    try:
      connection= get_connection()
      with connection.cursor() as cursor:
        cursor.execute("CALL sp_getProveedor()")
        result= cursor.fetchall()
        print(result)

      connection.close()
      return 'Lista de proveedor Actualizada'
    except Exception as ex:
      print(ex)

  @classmethod
  def post_proveedor(cls, proveedor: Proveedor):
    try:
      connection= get_connection()
      ID_Proveedor = proveedor.ID_Proveedor
      Nombre_Proveedor = proveedor.Nombre_Proveedor
      Direccion = proveedor.Direccion
      Telefono = proveedor.Telefono

      with connection.cursor() as cursor:
        cursor.execute("CALL sp_insertProveedor(%s, %s, %s, %s)",(ID_Proveedor,Nombre_Proveedor,Direccion,Telefono))
        connection.commit()

      connection.close()
      return 'Proveedor agregado con exito'    
    except Exception as ex:
      print(ex)

  @classmethod
  def delete_proveedor (cls, ID_Proveedor):
    try:
      connection= get_connection()

      with connection.cursor() as cursor:
        cursor.execute("CALL sp_deleteProveedor(%s)", ID_Proveedor)
        connection.commit()
      connection.close()
      return 'Proveedor eliminado con exito'
    except Exception as ex:
      print(ex)
        
  @classmethod
  def put_proveedor (cls, ID_Proveedor, proveedor: Proveedor):
    try:
      connection= get_connection()

      with connection.cursor() as cursor:
        Nombre_Proveedor = proveedor.Nombre_Proveedor
        Direccion = proveedor.Direccion
        Telefono = proveedor.Telefono

        cursor.execute("CALL sp_updateProveedor(%s, %s, %s, %s)", (Nombre_Proveedor, Direccion, Telefono, ID_Proveedor))
        connection.commit()
      connection.close()
      return 'Proveedor editado con exito'
    except Exception as ex:
      print(ex)
