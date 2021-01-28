class Sql:
    userlist = 'SELECT * FROM usertb'
    userlistone = "SELECT * FROM usertb WHERE id = '%s'"
    userinsert = "Insert INTO usertb VALUES('%s','%s','%s')"