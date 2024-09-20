from neo4j import GraphDatabase
import pandas as pd

class NeoUtils:
    def __init__(self, uri: str, user: str, pwd: str, dbName: str):
        self.uri = uri
        self.user = user
        self.password = pwd
        self.driver = GraphDatabase.driver(f"{self.uri}/{dbName}", auth=(self.user, self.password))

    # def main(self, deleteAll=False):
    #     # 删库
    #     if deleteAll:
    #         delConfirm = input("确定删库吗？（y/n）：")
    #         if delConfirm == "y":
    #             self.delBase()

    #     # 关闭链接
    #     self.close()

    def delBase(self):
        query = "match(a) detach delete a"
        with self.driver.session() as session: 
            session.run(query)  
  
    def close(self):  
        self.driver.close()

    # 输入字典，构建节点
    def createNodes(self, nodeDict):
        if 'label' in nodeDict:
            label = nodeDict['label']
        else:
            label = 'unKnowNodeType'
        charList = []
        for k, v in nodeDict.items():
            if k!= 'label':
                if isinstance(v, (int, float, complex)):
                    charList.append(f"{k}: {v}")
                else:
                    charv = "'" + str(v) + "'"
                    charList.append(f"{k}: {charv}")

        que = f"CREATE (n:{label} {{ { ', '.join(charList) } }})"
        # print(que)

        with self.driver.session() as session:
            session.run(que)

    def createNodesQue(self, ind, dictSpo:dict):
        if 'label' in dictSpo:
            label = dictSpo['label']
        else:
            label = 'unKnowNodeType'
        charList = []
        for k, v in dictSpo.items():
            if k!= 'label':
                if isinstance(v, (int, float, complex)):
                    charList.append(f"{k}: {v}")
                else:
                    charv = "'" + str(v) + "'"
                    charList.append(f"{k}: {charv}")

        # que = f"CREATE (n1:{label} {{ { ', '.join(charList) } }})"
        que = f"(n_{ind}:{label} {{ { ', '.join(charList) } }})"
        # print(que)

        return que
    
    def createEdgesQue(self, dictSpo:dict):
        if 'label' in dictSpo:
            label = dictSpo['label']
        else:
            label = 'unKnowEdgeType'
        charList = []
        for k, v in dictSpo.items():
            if k!= 'label':
                if isinstance(v, (int, float, complex)):
                    charList.append(f"{k}: {v}")
                else:
                    charv = "'" + str(v) + "'"
                    charList.append(f"{k}: {charv}")

        # que = f"CREATE (n1:{label} {{ { ', '.join(charList) } }})"
        que = f"[r:{label} {{ { ', '.join(charList) } }}]"
        # print(que)

        return que
    
    def merge(self, dict_subject, dict_object, dict_edge):

        # 生成主体节点和对象节点的匹配或创建语句
        subject_node = self.createNodesQue('s', dict_subject)
        object_node = self.createNodesQue('o', dict_object)
        
        # 生成关系的匹配或创建语句
        edge = self.createEdgesQue(dict_edge)

        # 构建 Cypher 语句
        que = f"""
        MERGE {subject_node}
        MERGE {object_node}
        MERGE (n_s)-{edge}->(n_o)
        """

        # print(que)

        with self.driver.session() as session:
            session.run(que)

        return 0
    
    def customCypher(self, cypher:str):
        with self.driver.session() as session:
            res = session.run(cypher)

        return res


# 使用示例
if __name__ == "__main__":
    uri = "bolt://localhost:7687"  # 替换为你的Neo4j URI
    user = "neo4j"  # 替换为你的Neo4j用户名
    pwd = "1742359208ys"  # 替换为你的Neo4j密码
    myDBName = "neo4j" # 选择需要被写入的数据库名称，社区版默认neo4j不用改
    gdb = NeoUtils(uri, user, pwd, dbName=myDBName)
    spo1 = {'label':'person', 'name': 'learnYes', 'age': 10}
    spo2 = {'label':'mokey', 'name': 'learnObj', 'age': 14}
    edge1 = {'label':'WORK_FOR', 'name': 'oelse', 'age': "16-19"}
    edge2 = {'label':'test_for', 'name': 'oalse', 'age': "20-219"}

    # gdb.main(spo=spo1)
    gdb.delBase()
    gdb.merge(spo1, spo2, edge1)
    gdb.merge(spo1, spo2, edge2)
