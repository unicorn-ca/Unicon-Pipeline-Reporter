from unicon_classes.IAM.base import Base
from unicon_classes.IAM import IAMUser
from datetime import datetime
from boto3_type_annotations.iam import Client
from typing import List
import boto3


class Group (Base):
    def __init__(self):
        super().__init__()
        self.type = "IAMGroup"
        self.path = ""
        self.groupID = ""
        self.createDate: datetime = None
        self.users: List[IAMUser] = None

    def __re_sync_update_group(self,group:dict):
        for name, item in group.items():
            if name == "Path": self.path = item
            if name == "GroupName": self.name = item
            if name == "GroupId": self.groupID = item
            if name == "Arn": self.arn = item
            if name == "CreateDate": self.createDate = item

    def in_group(self, user: IAMUser)->bool:
        for test_user in self.users:
            if test_user == user:
                return True
        return False

    def re_sync(self):
        if self.name != "":
            client: Client = boto3.client('iam')
            response: dict = client.get_group(self.name)
            if "Group" in response and "Users" in response:
                self.__re_sync_update_group(response['Group'])
                self.users = []
                for user in response["Users"]:
                    new_user = IAMUser()
                    new_user.update_user(user)
                    self.users.append(new_user)


