import constants
from table_model import TableModel
from table_manager import TableManager
from connection_manager import ConnectionManager

if __name__ == '__main__':
    name = 'test01'

    # 字段类型map
    fields_type_map = {}
    fields_type_map['id'] = constants.INTEGER
    fields_type_map['name'] = constants.VARCHAR_30

    # 字段额外约束
    fields_condition = {}
    fields_condition['id'] = 'primary key'

    # 表格主键
    pk = 'id'
    tableModel = TableModel(name, fields_type_map, fields_condition, pk)

    # 获取连接
    connection_manager = ConnectionManager('test.db', '')

    # 获取表格管理器
    table_manager = TableManager(connection_manager, tableModel)

    # 创建表格
    table_manager.create_table()

    # 插入数据
    values = {}
    values['id'] = 4
    values['name'] = "mayun"
    table_manager.insert_table(values)

    # 字段查询条件
    conditions = {}
    conditions['name'] = ' is not null'
    data = table_manager.query_table(conditions)


    print(data)
    pass