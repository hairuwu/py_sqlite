import constants
import table_model
from connection_manager import ConnectionManager
from table_model import TableModel



class TableManager:

    def __init__(self, connection_manager: ConnectionManager, table_model: TableModel):
        self.connection_manager = connection_manager
        self.table_model = table_model

    def create_table(self):
        sql = "create table IF NOT EXISTS   " + \
              self.table_model.name + "(  "

        # 字段
        item = ""
        for key in self.table_model.fields:
            item += key + " " \
                   + self.table_model.fields[key]+ " "
            if key in self.table_model.fields_condition.keys() :
                item += self.table_model.fields_condition[key]
            item += ", "

        sql += item[:-2] + ") "

        print(sql)
        try:
            self.connection_manager.get_db_cursor().execute(sql)
            print("创建表成功")
        except Exception as e:
            print(e)
            print('创建表失败')

    # con_list: field_name -> =10 / >10 / <10 /
    def query_table(self, conditions: {}):
        sql = "SELECT * FROM " + self.table_model.name + "\n" \
              + " where "
        for key in conditions:
            sql += key + " " + conditions[key] + " \n"

        sql += ' and  1=1 '

        print(sql)
        try:
            self.connection_manager.get_db_cursor().execute(sql)
            data = self.connection_manager.get_db_cursor().fetchall()
            return data
        except Exception as e:
            print(e)
            print('查询失败')

    # 插入单条数据 field_name -> value
    def insert_table(self, values: {}):
        sql = "insert into " + self.table_model.name +"( "
        for key in values:
            sql+=key+","
        sql = sql[:-1]
        sql+=") values ("
        for key in values:
            if self.table_model.fields[key] == constants.VARCHAR_30:
                sql+='''"'''+str(values[key]) + '''"''' +","
            else:
                sql += str(values[key]) + ","
        sql = sql[:-1] + ")"
        print(sql)
        try:
            self.connection_manager.get_db_cursor().execute(sql, values)
            # 提交事务
            self.connection_manager.get_db_connection().commit()
            print('插入成功')
        except Exception as e:
            print(e)
            print('插入失败')
            self.connection_manager.get_db_connection().rollback()

