from neoUtils import NeoUtils


uri = "bolt://localhost:7687"  # 替换为你的Neo4j URI
user = "neo4j"  # 替换为你的Neo4j用户名
pwd = "1742359208ys"  # 替换为你的Neo4j密码
myDBName = "neo4j" # 选择需要被写入的数据库名称，社区版默认neo4j不用改
gdb = NeoUtils(uri, user, pwd, dbName=myDBName) # 创建实例

spo1 = {'label':'person', 'name': 'learnYes', 'age': 10}
spo2 = {'label':'mokey', 'name': 'learnObj', 'age': 14}
edge = {'label':'WORK_FOR', 'name': 'oelse', 'age': "16-19"}

node = {'label':'other', 'name': 'haha', "likenum": 1}

gdb.merge(spo1, spo2, edge) # 根据三元组（三个字典）创建neo4j三元组
gdb.createNodes(node) # 根据一个字典创建neo4j实体节点