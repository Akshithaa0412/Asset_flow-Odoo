from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.allocation import AllocationCreate, AllocationResponse
from app.services.allocation_service import AllocationService


router = APIRouter(prefix="/allocations", tags=["Allocations"])


@router.post("/", response_model=AllocationResponse)
def create_allocation(allocation: AllocationCreate, db: Session = Depends(get_db)):
    return AllocationService.create_allocation(db, allocation)


@router.get("/", response_model=list[AllocationResponse])
def get_allocations(db: Session = Depends(get_db)):
    return AllocationService.get_allocations(db)
