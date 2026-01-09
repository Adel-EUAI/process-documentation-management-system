from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.db.database import get_db
from src.models.user import User
from src.schemas.document import (
    DocumentCreate,
    DocumentUpdate,
    DocumentOut,
)
from src.services.document_service import (
    create_document,
    get_documents_for_user,
    get_document_by_id,
    update_document,
    delete_document,
)
from src.auth.service import get_current_user

router = APIRouter(
    prefix="/documents",
    tags=["documents"],
)


@router.post(
    "/",
    response_model=DocumentOut,
)
def create(
    data: DocumentCreate,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    return create_document(db=db, user=user, data=data)


@router.get("/", response_model=list[DocumentOut])
def list_documents(
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    return get_documents_for_user(db=db, user=user)


@router.get("/{document_id}", response_model=DocumentOut)
def retrieve(
    document_id: int,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    document = get_document_by_id(
        db=db, user=user, document_id=document_id
    )
    if not document:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Document not found",
        )
    return document


@router.put("/{document_id}", response_model=DocumentOut)
def update(
    document_id: int,
    data: DocumentUpdate,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    document = get_document_by_id(
        db=db, user=user, document_id=document_id
    )
    if not document:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Document not found",
        )
    return update_document(
        db=db, document=document, data=data
    )


@router.delete(
    "/{document_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete(
    document_id: int,
    db: Session = Depends(get_db),
    user: User = Depends(get_current_user),
):
    document = get_document_by_id(
        db=db, user=user, document_id=document_id
    )
    if not document:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Document not found",
        )
    delete_document(db=db, document=document)
