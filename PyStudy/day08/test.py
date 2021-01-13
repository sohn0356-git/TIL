# CREATE TABLE IF NOT EXISTS usertb(
#     id CHAR(10) PRIMARY KEY,
#     pwd CHAR(10),
#     name CHAR(10),
#     age NUMBER(3)
# )
#
# INSERT INTO usertb VALUES('%s','%s','%s',%d)
# DELETE FROM user tb WHERE id = '%s'
# UPDATE usertb SET pwd = '%s'