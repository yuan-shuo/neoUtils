## neoUtils：基于Python操作neo4j数据库的工具包

### 导包

使用前如何导包：

```python
from neoUtils import NeoUtils

uri = "bolt://localhost:7687"  # 替换为你的Neo4j URI
user = "neo4j"  # 替换为你的Neo4j用户名
pwd = "1742359208ys"  # 替换为你的Neo4j密码
myDBName = "neo4j" # 选择需要被写入的数据库名称，社区版默认neo4j不用改
gdb = NeoUtils(uri, user, pwd, dbName=myDBName) # 创建实例
```

### 功能：

#### 1. 直接用字典创建实体节点

```python
node = {'label':'other', 'name': 'haha', "likenum": 1}
gdb.createNodes(node) # 根据一个字典创建neo4j实体节点
```

#### 2. 直接用三个字典创建三元组

```python
spo1 = {'label':'person', 'name': 'learnYes', 'age': 10}
spo2 = {'label':'mokey', 'name': 'learnObj', 'age': 14}
edge = {'label':'WORK_FOR', 'name': 'oelse', 'age': "16-19"}

gdb.merge(spo1, spo2, edge) # 根据三元组（三个字典）创建neo4j三元组
```

#### 3. 删库

```python
gdb.delBase() # 完全删除所有数据
```

#### 4. 关闭驱动

```python
gdb.close()
```





