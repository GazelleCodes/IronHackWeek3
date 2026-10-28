
import duckdb

con = duckdb.connect("data/warehouse.duckdb")
print(con.execute("SELECT * FROM main.example_model").fetchdf())

con.close()
