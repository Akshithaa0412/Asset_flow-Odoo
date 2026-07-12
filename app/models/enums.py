from enum import Enum


class UserRole(str, Enum):
    ADMIN = "ADMIN"
    EMPLOYEE = "EMPLOYEE"
    ASSET_MANAGER = "ASSET_MANAGER"
    DEPARTMENT_HEAD = "DEPARTMENT_HEAD"


class AssetStatus(str, Enum):
    AVAILABLE = "Available"
    ALLOCATED = "Allocated"
    RESERVED = "Reserved"
    UNDER_MAINTENANCE = "Under Maintenance"
    LOST = "Lost"
    RETIRED = "Retired"
    DISPOSED = "Disposed"