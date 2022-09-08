from typing import Optional
from fastapi import (
    APIRouter,
    Depends,
    Response,
    status,
)
from ..models.operations import (
    Operations,
    OperationKind,
    OperationCreate,
    OperationUpdate,
)
from ..servises.operations import OperationService

router = APIRouter(
    prefix='/operations',
)


@router.get('/', response_model=list[Operations])
def get_operations(
        kind: Optional[OperationKind] = None,
        service: OperationService = Depends(),
):
    return service.get_list(kind=kind)


@router.post('/', response_model=Operations)
def create_operation(
        operation_data: OperationCreate,
        service: OperationService = Depends(),
):
    return service.create(operation_data)


@router.get('/{operation_id}', response_model=Operations)
def get_operation(
        operation_id: int,
        service: OperationService = Depends(),
):
    return service.get(operation_id)


@router.put('/{operation_id}', response_model=Operations)
def update_operation(
        operation_id: int,
        operation_data: OperationUpdate,
        service: OperationService = Depends(),
):
    return service.update(
        operation_id,
        operation_data,
    )


@router.delete('/{operation_id}')
def delete_operation(
        operation_id: int,
        service: OperationService = Depends(),
):
    service.delete(operation_id)

    return Response(status_code=status.HTTP_204_NO_CONTENT)
