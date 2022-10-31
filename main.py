import pandas as pd
import os
from datetime import date
from process_data import *
from generate_files import generate_files
from db_connection import *
import logging


def main():

    logging.basicConfig(filename='file.log', filemode='w', level=logging.INFO)

    fecha_carga = date.today()
    logging.info(f'"{fecha_carga}"')

    logging.info("VALIDATING DATABASE CONNECTION...")
    check_connection()

    #Get files #
    logging.info("OBTAINING FILES...")

    categorias = [
        'bibliotecas',
        'cines',
        'museos'
    ]

    for c in categorias:

        dirName = c
        subdirName = f'{fecha_carga.year}-{fecha_carga.month}'

        if not os.path.exists(dirName):
            os.mkdir(dirName)

        if not os.path.exists(f'{dirName}/{subdirName}/{dirName}-{fecha_carga.day}-{fecha_carga.month}-{fecha_carga.year}.csv'):
            if not os.path.exists(dirName + '/' + subdirName):
                os.mkdir(dirName + '/' + subdirName)
            generate_files(c, fecha_carga)
        else:
            logging.info(
                f'File found: "{c}-{fecha_carga.day}-{fecha_carga.month}-{fecha_carga.year}"')
            continue

    #Data Processing#
    logging.info("PROCESSING DATA...")

    # loading df
    bibliotecas_df = pd.read_csv(
        f'bibliotecas/{fecha_carga.year}-{fecha_carga.month}/bibliotecas-{fecha_carga.day}-{fecha_carga.month}-{fecha_carga.year}.csv')
    cines_df = pd.read_csv(
        f'cines/{fecha_carga.year}-{fecha_carga.month}/cines-{fecha_carga.day}-{fecha_carga.month}-{fecha_carga.year}.csv')
    museos_df = pd.read_csv(
        f'museos/{fecha_carga.year}-{fecha_carga.month}/museos-{fecha_carga.day}-{fecha_carga.month}-{fecha_carga.year}.csv')

    # processing df
    helper_df = create_helper(bibliotecas_df, cines_df, museos_df, fecha_carga)

    informacion_df = create_informacion(helper_df)
    registros_df = create_registros(helper_df)
    cines_df = create_cine(helper_df)

    #Database update#
    logging.info("UPDATING DATA...")

    con = connect_2db()

    informacion_df.to_sql('informacion', con, if_exists='replace', index=False)
    logging.info('"INFORMACION" table updated')

    registros_df.to_sql('registros', con, if_exists='replace', index=False)
    logging.info('"REGISTROS" table updated')

    cines_df.to_sql('cines', con, if_exists='replace', index=False)
    logging.info('"CINES" table updated')

    con.close()


if __name__ == '__main__':
    main()
