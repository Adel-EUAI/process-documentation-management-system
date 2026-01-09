from sqlalchemy.orm import Session

from src.models.document import Document
from src.models.user import User
from src.schemas.document import DocumentCreate, DocumentUpdate


def create_document(
    db: Session,
    *,
    user: User,
    data: DocumentCreate
) -> Document:
    document = Document(
        title=data.title,
        description=data.description,
        owner_id=user.id
    )
    db.add(document)
    db.commit()
    db.refresh(document)
    return document


def get_documents_for_user(
    db: Session,
    *,
    user: User
) -> list[Document]:
    return (
        db.query(Document)
        .filter(Document.owner_id == user.id)
        .all()
    )


def get_document_by_id(
    db: Session,
    *,
    user: User,
    document_id: int
) -> Document | None:
    return (
        db.query(Document)
        .filter(
            Document.id == document_id,
            Document.owner_id == user.id
        )
        .first()
    )


def update_document(
    db: Session,
    *,
    document: Document,
    data: DocumentUpdate
) -> Document:
    if data.title is not None:
        document.title = data.title
    if data.description is not None:
        document.description = data.description

    db.commit()
    db.refresh(document)
    return document


def delete_document(
    db: Session,
    *,
    document: Document
) -> None:
    db.delete(document)
    db.commit()
