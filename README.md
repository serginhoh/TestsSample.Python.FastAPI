# TestsSample.Python.FastAPI

Projeto para demonstração em Python de Testes Unitários e de Integração utilizando FastAPI e pytest.

## Execução:

- criar diretório virtual para instalação dos packages
```
    python -m venv venv
```
- ativar
```
  .\venv\Scripts\activate

  Visual Studio Code

  Ctrl + Shift + P

  opção Selecionar o Interpretador 

  indicar o arquivo python.exe dentro do diretório virtual .\venv\Scripts
```
- instalar os pacotes
```
    pip install -r requirements.txt
```
- Execução 

  - Aplicação
  ```
      no diretório raiz
    
      uvicorn src.app:app --reload
      
      swagger : http://127.0.0.1:8000/v1/docs
  ```
  - Testes
  ```
      no diretório raiz
    
      python -m pytest -v
  ```

#Referências

https://realpython.com/api-integration-in-python/#fastapi

https://fastapi.tiangolo.com/

https://fastapi.tiangolo.com/tutorial/testing/

https://docs.pytest.org/en/7.3.x/

https://docs.pydantic.dev/usage/validators/

https://medium.com/@caetanoog/how-to-version-your-fast-api-application-a37737ee777e

https://understandingdata.com/posts/list-of-python-assert-statements-for-unit-tests/
