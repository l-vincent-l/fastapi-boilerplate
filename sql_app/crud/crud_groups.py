from . import (pp, Session)

from ..db.database import get_db

from .base import CRUDBase
from ..models.models_group import Group
from ..schemas.schemas_group import UserInDBBaseLight, GroupCreate, GroupUpdate


class CRUDGroup(CRUDBase[Group, GroupCreate, GroupUpdate]):
  def create_with_owner_in_team(
    self, db: Session, *, 
    obj_in: GroupCreate,
    owner_id: int,
    users = [],
    users_pending = [],
    ):
    db_obj = self.create_with_owner(db=db, obj_in=obj_in, owner_id=owner_id)

    obj_users = db_obj.users
    obj_users.append(*users)
    setattr(db_obj, "users", obj_users)

    obj_users_pending = db_obj.users_pending
    obj_users_pending.append(*users_pending)
    setattr(db_obj, "users_pending", obj_users_pending)

    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

group = CRUDGroup(Group)
