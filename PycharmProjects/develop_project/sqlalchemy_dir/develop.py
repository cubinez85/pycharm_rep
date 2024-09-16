from sqlalchemy import text
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


engine = create_engine("sqlite+pysqlite:///sql.db", echo=True)


# with engine.connect() as conn:
#     result = conn.execute(text("select 'hello world'"))
#     print(result.all())


# with engine.begin() as conn:
#     conn.execute(
#         text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
#         [{"x": 6, "y": 8}, {"x": 9, "y": 10}],
#     )
#     conn.commit()

# with engine.connect() as conn:
#     conn.execute(text("CREATE TABLE some_table (x int, y int)"))
#     conn.execute(
#         text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
#         [{"x": 1, "y": 1}, {"x": 2, "y": 4}],
#     )
#     conn.commit()

# with engine.connect() as conn:
#     result = conn.execute(text("SELECT x, y FROM some_table"))
#     for dict_row in result.mappings():
#         x = dict_row["x"]
#         y = dict_row["y"]
#         print(x, y)

# with engine.connect() as conn:
#     conn.execute(
#         text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
#         [{"x": 11, "y": 12}, {"x": 13, "y": 14}],
#     )
#     conn.commit()

