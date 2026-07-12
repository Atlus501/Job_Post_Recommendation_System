from fastapi import APIRouter, Request, status

router = APIRouter()

@router.put("/update", status.HTTP_200_OK)
async def update_database(req : request):
    neo4j_manager = req.app.state.neo4j_manager

    