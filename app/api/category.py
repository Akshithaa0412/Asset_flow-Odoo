from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db

from app.schemas.category import (
    CategoryCreate,
    CategoryUpdate,
    CategoryResponse,
)

from app.services.category_service import (
    get_all_categories,
    get_category,
    create_category,
    update_category,
    delete_category,
)

router = APIRouter(
    prefix="/categories",
    tags=["Asset Categories"]
)


@router.get("/", response_model=list[CategoryResponse])
def get_categories(db: Session = Depends(get_db)):
    return get_all_categories(db)


@router.get("/{category_id}", response_model=CategoryResponse)
def get_one(category_id: int, db: Session = Depends(get_db)):
    category = get_category(db, category_id)

    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")

    return category


@router.post("/", response_model=CategoryResponse)
def create(request: CategoryCreate, db: Session = Depends(get_db)):
    return create_category(db, request)


@router.put("/{category_id}", response_model=CategoryResponse)
def update(
    category_id: int,
    request: CategoryUpdate,
    db: Session = Depends(get_db),
):
    category = update_category(db, category_id, request)

    if category is None:
        raise HTTPException(status_code=404, detail="Category not found")

    return category


@router.delete("/{category_id}")
def delete(category_id: int, db: Session = Depends(get_db)):
    deleted = delete_category(db, category_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Category not found")

    return {"message": "Category deleted successfully"}