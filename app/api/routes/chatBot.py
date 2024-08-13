import uuid
from typing import Any

from fastapi import APIRouter, HTTPException
from sqlmodel import func, select

from app.api.deps import CurrentUser, SessionDep
from app.models import ChatBot, ChatBotCreate, ChatBotPublic, ChatBotsPublic, ChatBotUpdate, Message

router = APIRouter()


@router.get("/", response_model=ChatBotsPublic)
def read_items(
    session: SessionDep, current_user: CurrentUser, skip: int = 0, limit: int = 100
) -> Any:
    """
    Retrieve items.
    """

    if current_user.is_superuser:
        count_statement = select(func.count()).select_from(ChatBot)
        count = session.exec(count_statement).one()
        statement = select(ChatBot).offset(skip).limit(limit)
        items = session.exec(statement).all()
    else:
        count_statement = (
            select(func.count())
            .select_from(ChatBot)
            .where(ChatBot.owner_id == current_user.id)
        )
        count = session.exec(count_statement).one()
        statement = (
            select(ChatBot)
            .where(ChatBot.owner_id == current_user.id)
            .offset(skip)
            .limit(limit)
        )
        items = session.exec(statement).all()

    return ChatBotPublic(data=items, count=count)


@router.get("/{id}", response_model=ChatBotPublic)
def read_item(session: SessionDep, current_user: CurrentUser, id: uuid.UUID) -> Any:
    """
    Get item by ID.
    """
    item = session.get(ChatBot, id)
    if not item:
        raise HTTPException(status_code=404, detail="ChatBot not found")
    if not current_user.is_superuser and (item.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    return item


@router.post("/", response_model=ChatBotPublic)
def create_item(
    *, session: SessionDep, current_user: CurrentUser, item_in: ChatBotCreate
) -> Any:
    """
    Create new item.
    """
    item = ChatBot.model_validate(item_in, update={"owner_id": current_user.id})
    session.add(item)
    session.commit()
    session.refresh(item)
    return item


@router.put("/{id}", response_model=ChatBotPublic)
def update_item(
    *,
    session: SessionDep,
    current_user: CurrentUser,
    id: uuid.UUID,
    item_in: ChatBotsPublic,
) -> Any:
    """
    Update an item.
    """
    item = session.get(ChatBot, id)
    if not item:
        raise HTTPException(status_code=404, detail="ChatBot not found")
    if not current_user.is_superuser and (item.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    update_dict = item_in.model_dump(exclude_unset=True)
    item.sqlmodel_update(update_dict)
    session.add(item)
    session.commit()
    session.refresh(item)
    return item


@router.delete("/{id}")
def delete_item(
    session: SessionDep, current_user: CurrentUser, id: uuid.UUID
) -> Message:
    """
    Delete an item.
    """
    item = session.get(ChatBot, id)
    if not item:
        raise HTTPException(status_code=404, detail="ChatBot not found")
    if not current_user.is_superuser and (item.owner_id != current_user.id):
        raise HTTPException(status_code=400, detail="Not enough permissions")
    session.delete(item)
    session.commit()
    return Message(message="ChatBot deleted successfully")
