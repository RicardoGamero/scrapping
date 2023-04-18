from typing import Optional
from repositories.uf_repository import UfRepository
from models.uf import UF


class UfService:
    def __init__(self, uf_repository: Optional[UfRepository] = None):
        self.uf_repository = uf_repository or UfRepository()

    def get_ufs(self, year: str, month: str) -> list[UF]:
        return self.uf_repository.get_ufs(year, month)
