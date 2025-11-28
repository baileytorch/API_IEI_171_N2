from datos import sesion


def insertar_objeto(objeto):
    sesion.add(objeto)
    sesion.flush()
    sesion.refresh(objeto)
    id_objeto = objeto.id
    try:
        sesion.commit()
        print("El objeto se ha guardado correctamente.")
        return id_objeto
    except Exception as error:
        sesion.rollback()
        print(f"Error al guardar el objeto: {error}")
    finally:
        sesion.close()
