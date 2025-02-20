import pandas as pd

DB_FILE = "/Users/mango/projects/data-analytics/sql-practice/03-pokemon.db"
DB_PATH = f"sqlite+pysqlite:///{DB_FILE}"


def main():
    pokemon_df = pd.read_sql_table("pokemon", DB_PATH)
    pokemon_types_df = pd.read_sql_table("types", DB_PATH)

    mergedPokemon = pokemon_df.merge(pokemon_types_df, how="left", on="id")

    print(mergedPokemon)

    print(mergedPokemon.columns)

    print(mergedPokemon.shape)

    print(mergedPokemon["name_x"].loc[146])

    pokTypeCount = mergedPokemon[(mergedPokemon["typeOne"] == 6)]
    typeCount = len(pokTypeCount)
    print(typeCount)

if __name__ == "__main__":
    main()
