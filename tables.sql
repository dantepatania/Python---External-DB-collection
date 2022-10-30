CREATE TABLE informacion (
    cod_localidad INTEGER,
    id_provincia INTEGER,
    id_departamento INTEGER,
    categoria TEXT,
    provincia TEXT,
    localidad TEXT,
    nombre TEXT,
    domicilio TEXT,
    codigo_postal TEXT,
    telefono TEXT,
    mail TEXT,
    web TEXT,
    fecha_carga DATE NOT NULL
);

CREATE TABLE registros (
    provincia TEXT,
    categoria TEXT,
    fuente TEXT,
    total INTEGER,
    categoria_total INT,
    fuente_total INT,
    fecha_carga DATE NOT NULL
);


CREATE TABLE cines (
    provincia TEXT,
    pantallas INTEGER,
    butacas INTEGER,
    espacios_incaa BOOLEAN,
    fecha_carga DATE NOT NULL
);