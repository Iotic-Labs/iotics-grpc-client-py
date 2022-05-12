from .base import ApiBase
from iotics.api.twin_pb2_grpc import TwinAPIStub
from iotics.api.twin_pb2 import DescribeTwinRequest, DeleteTwinRequest, UpdateTwinRequest, UpsertTwinRequest, \
    VisibilityUpdate, GeoLocationUpdate, ListAllTwinsRequest, ListAllTwinsResponse, CreateTwinRequest
from iotics.api.common_pb2 import Headers, TwinID, HostID, PropertyUpdate, Visibility


class TwinApi(ApiBase):
    stub_class = TwinAPIStub

    def create_twin(self, did):
        req = CreateTwinRequest(headers=Headers(), payload=CreateTwinRequest.Payload(twinId=TwinID(value=did)))
        return self.stub.CreateTwin(req)

    def describe_twin(self, did, remote_host_id=None):
        req = DescribeTwinRequest(headers=Headers(), args=DescribeTwinRequest.Arguments(
            twinId=TwinID(value=did),
            remoteHostId=HostID(value=remote_host_id)
        ))
        return self.stub.DescribeTwin(req)

    def delete_twin(self, did):
        req = DeleteTwinRequest(headers=Headers(), args=DeleteTwinRequest.Arguments(twinId=TwinID(value=did)))
        return self.stub.DeleteTwin(req)

    def list_twins(self) -> ListAllTwinsResponse:
        req = ListAllTwinsRequest(headers=Headers())
        return self.stub.ListAllTwins(req)

    def update_twin(self, did, visibility=None, location=None, props_added=None, props_deleted=None,
                    props_keys_deleted=None, props_clear_all=False):
        req = UpdateTwinRequest(
            headers=Headers(),
            args=UpdateTwinRequest.Arguments(twinId=TwinID(value=did)),
            payload=UpdateTwinRequest.Payload(
                newVisibility=VisibilityUpdate(visibility=Visibility.Value(visibility.upper())) if visibility else None,
                location=GeoLocationUpdate(location=location) if location else None,
                properties=PropertyUpdate(
                    added=props_added,
                    deleted=props_deleted,
                    deletedByKey=props_keys_deleted,
                    clearedAll=props_clear_all
                )
            ))
        return self.stub.UpdateTwin(req)

    def upsert_twin(self, did, visibility=None, location=None, properties=None, feeds=None):
        req = UpsertTwinRequest(
            headers=Headers(),
            payload=UpsertTwinRequest.Payload(
                twinId=did,
                visibility=Visibility.Value(visibility.upper()) if visibility else None,
                location=location,
                properties=properties,
                feeds=feeds
            )
        )
        return self.stub.UpsertTwin(req)
