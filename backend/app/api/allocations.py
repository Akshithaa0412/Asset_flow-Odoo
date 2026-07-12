from fastapi import APIRouter

router = APIRouter(prefix="/allocations", tags=["Allocations"])


@router.get("/")
def get_allocations():
    return {"success": True, "message": "Allocation API is working", "data": []}
