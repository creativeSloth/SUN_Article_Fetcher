query = "SELECT * FROM test_table WHERE project_name = ''"
subquery = "project_name = "

try:
    position = query.index(subquery)
    print(str(position) + " + " + str(len(subquery)) +
          " ===== " + str(position + len(subquery)))
    print(query[position])
    print(query[position + len(subquery)+1])

except ValueError:
    print("No subquery found")
