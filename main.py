import pandas as pd
from sqlalchemy import create_engine

DB_FILE = "/Users/mango/projects/data-analytics/sql-practice/03-pokemon.db"
DB_PATH = f"sqlite+pysqlite:///{DB_FILE}"


def main():

    pokemon_df = pd.read_sql_table('pokemon', DB_PATH)
    pokemonTypes_df = pd.read_sql_table('types', DB_PATH)

    pokemon_df.merge(pokemonTypes_df, on='id')

    print(pokemon_df)

    print(pokemon_df.columns)

    print(pokemon_df.shape)

    print(pokemon_df['name'].loc[146])



if __name__ == "__main__":
    main()
