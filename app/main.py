from fastapi import FastAPI, HTTPException, Depends, status
from sqlmodel import Session
from typing import List

from .database import init_db, get_session
from .models import Term
from .schemas import TermCreate, TermRead, TermUpdate
from . import crud

app = FastAPI(title="Glossary API", version="1.0.0")


@app.on_event("startup")
def on_startup():
    # автоматическое создание таблиц — простая "миграция"
    init_db()


@app.get("/terms", response_model=List[TermRead])
def list_terms(session: Session = Depends(get_session)):
    return crud.get_all_terms(session)


@app.get("/terms/{keyword}", response_model=TermRead)
def get_term(keyword: str, session: Session = Depends(get_session)):
    term = crud.get_term_by_keyword(session, keyword)
    if not term:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Term not found"
        )
    return term


@app.post("/terms", response_model=TermRead, status_code=status.HTTP_201_CREATED)
def create_new_term(term_in: TermCreate, session: Session = Depends(get_session)):
    # check exists
    exists = crud.get_term_by_keyword(session, term_in.keyword)
    if exists:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Term with keyword already exists"
        )
    term = Term(keyword=term_in.keyword, description=term_in.description)
    return crud.create_term(session, term)


@app.put("/terms/{keyword}", response_model=TermRead)
def update_existing_term(keyword: str, term_in: TermUpdate, session: Session = Depends(get_session)):
    term = crud.get_term_by_keyword(session, keyword)
    if not term:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Term not found"
        )

    new_desc = term_in.description if term_in.description is not None else term.description
    return crud.update_term(session, term, new_desc)


@app.delete("/terms/{keyword}", status_code=status.HTTP_204_NO_CONTENT)
def delete_term(keyword: str, session: Session = Depends(get_session)):
    term = crud.get_term_by_keyword(session, keyword)
    if not term:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Term not found"
        )
    crud.delete_term(session, term)
    return None
