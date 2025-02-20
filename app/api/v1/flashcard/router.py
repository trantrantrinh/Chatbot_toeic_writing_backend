from fastapi import APIRouter
from app.api.v1.flashcard.vocabulary.router import router as vocabulary_router
from app.api.v1.flashcard.grammar.router import router as grammar_router 
from app.api.v1.flashcard.studynote.router import router as studynote_router

router = APIRouter()

router.include_router(vocabulary_router, prefix="/vocabulary", tags=["vocabulary"])
router.include_router(grammar_router, prefix="/grammar", tags=["grammar"])
router.include_router(studynote_router, prefix="/studynote", tags=["studynote"])
