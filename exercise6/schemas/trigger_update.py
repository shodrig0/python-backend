from fastapi import APIRouter, BackgroundTasks
from tasks.run_random_price import run_random_price

trigger_update_router = APIRouter()

@trigger_update_router.post('/trigger-update')
async def trigger_update(background_task: BackgroundTasks):
    background_task.add_task(run_random_price)
    return {"detail": "Prices were updated successfully"}