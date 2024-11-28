from .start import router as start_router
from .admin import router as admin_router
from .menu import router as menu_router
from .reels import router as reels_router
from .stories import router as stories_router
from aiogram import Router

router = Router()

router.include_router(start_router)
router.include_router(admin_router)
router.include_router(menu_router)
router.include_router(reels_router)
router.include_router(stories_router)