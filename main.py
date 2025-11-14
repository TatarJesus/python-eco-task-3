from fastapi import FastAPI, HTTPException
from typing import Optional, Dict
from pydantic import BaseModel

app = FastAPI()

class Term(BaseModel):
  title: str
  definition: str
  source_link: Optional[str] = None

class UpdateTerm(BaseModel):
  definition: Optional[str] = None
  source_link: Optional[str] = None

data: Dict[str, Term] = {
    'npm': {
        'title': 'npm',
        'definition': 'Node Package Manager — система управления пакетами для Node.js, позволяет устанавливать и обновлять библиотеки.',
        'source_link': 'https://www.npmjs.com/'
    },
    'npx': {
        'title': 'npx',
        'definition': 'Утилита для выполнения пакетов Node.js без их глобальной установки.',
        'source_link': 'https://www.npmjs.com/package/npx'
    },
    'esm': {
        'title': 'esm',
        'definition': 'ECMAScript Modules — стандарт модулей в JavaScript, поддерживаемый Node.js.',
        'source_link': 'https://nodejs.org/api/esm.html'
    },
    'cjs': {
        'title': 'cjs',
        'definition': 'CommonJS — модульная система Node.js для работы с require и module.exports.',
        'source_link': 'https://nodejs.org/docs/latest/api/modules.html'
    },
    'eventloop': {
        'title': 'eventloop',
        'definition': 'Цикл событий Node.js, обрабатывающий асинхронные операции и управление очередью задач.',
        'source_link': 'https://nodejs.org/en/docs/guides/event-loop-timers-and-nexttick/'
    }
}

@app.get("/", response_model=Dict[str, Term])
async def get_all_terms():
  """
  Получить список всех элементов
  """
  return data

@app.get("/term/{keyword}", response_model=Term)
async def get_term(keyword: str) -> Term:
  """
  Получить элемент по ключевому слову
  """
  if keyword not in data:
    raise HTTPException(
      status_code=404, 
      detail=f"Элемент '{keyword}' не найден"
    )
  else:
    return data[keyword]
  
@app.post('/term/{keyword}', response_model=Term)
async def create_term(keyword: str, term: Term) -> Term:
  """
  Добавить новый элемент с описанием
  """
  if keyword in data:
    raise HTTPException(
      status_code=400, 
      detail=f"Элемент '{keyword}' уже существует"
    )
  else:
    data[keyword] = term
  
  return data[keyword]
  
@app.put('/term/{keyword}', response_model=Term)
async def update_term(keyword: str, term: UpdateTerm) -> Term:
  """
  Обновить существующий элемент
  """
  if keyword not in data:
    raise HTTPException(
      status_code=404, 
      detail=f"Элемент '{keyword}' не найден"
    )
  
  if term.definition is not None:
    data[keyword]['definition'] = term.definition
  if term.source_link is not None:
    data[keyword]['source_link'] = term.source_link

  return data[keyword]

@app.delete("/term/{keyword}", response_model=Term)
async def delete_term(keyword: str) -> Term:
  """
  Удалить элемент
  """
  if keyword not in data:
    raise HTTPException(
      status_code=404, 
      detail=f"Элемент '{keyword}' не найден"
    )
  
  deleted_term = data.pop(keyword)
  return deleted_term
