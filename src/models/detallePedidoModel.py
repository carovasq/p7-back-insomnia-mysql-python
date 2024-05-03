class DetallePedido():
  def __init__(self,ID_Detalle_Pedido,ID_Pedido,ID_Producto,Precio_Unitario,Precio_Total,Cantidad_Pedido) -> None:
    self.ID_Detalle_Pedido = ID_Detalle_Pedido
    self.ID_Pedido = ID_Pedido
    self.ID_Producto = ID_Producto
    self.Precio_Unitario = Precio_Unitario
    self.Precio_Total = Precio_Total
    self.Cantidad_Pedido = Cantidad_Pedido