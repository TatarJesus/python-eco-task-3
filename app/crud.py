from sqlmodel import select, Session
from .models import Term


def get_all_terms(session: Session):
    statement = select(Term).order_by(Term.keyword)
    return session.exec(statement).all()


def get_term_by_keyword(session: Session, keyword: str):
    statement = select(Term).where(Term.keyword == keyword)
    return session.exec(statement).first()


def create_term(session: Session, term: Term):
    session.add(term)
    session.commit()
    session.refresh(term)
    return term


def update_term(session: Session, db_term: Term, description: str):
    db_term.description = description
    session.add(db_term)
    session.commit()
    session.refresh(db_term)
    return db_term


def delete_term(session: Session, db_term: Term):
    session.delete(db_term)
    session.commit()
