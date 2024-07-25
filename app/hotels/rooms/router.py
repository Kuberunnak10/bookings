from datetime import date, datetime, timedelta
from typing import List

from app.hotels.rooms.dao import RoomDAO
from fastapi import APIRouter, Query

router_rooms = APIRouter(prefix='/hotels',
                         tags=["Комнаты"])


@router_rooms.get("/{hotel_id}/rooms")
async def get_rooms_by_time(
    hotel_id: int,
    date_from: date = Query(..., description=f"Например, {datetime.now().date()}"),
    date_to: date = Query(..., description=f"Например, {(datetime.now() + timedelta(days=14)).date()}"),
):
    rooms = await RoomDAO.find_all(hotel_id, date_from, date_to)
    return rooms
