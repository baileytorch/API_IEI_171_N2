CREATE TABLE IF NOT EXISTS usuarios(
    id INTEGER AUTO_INCREMENT,
    nombre VARCHAR(30) NOT NULL,
    usuario VARCHAR(15) NOT NULL,
    email VARCHAR(255) NOT NULL,
    contrasena_hash VARCHAR(255) NOT NULL,
    contrasena_salt VARCHAR(255) NOT NULL,

    CONSTRAINT pk_usuarios PRIMARY KEY (id)
);