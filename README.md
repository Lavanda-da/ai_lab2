## Лабораторная работа 2 
по курсу "Киберфизические системы"

Выполнила Ирина Сектименко, студент группы М8О-410Б-22

Инструкция по запуску:
1. Скачать десктопную версию докера и запустить ее.
2. Склонировать репозиторий командой: git clone https://github.com/Lavanda-da/ai_lab2.
3. Перейти в корневую деректорию проекта: cd ai_lab2.
4. Ввести команду, собирающую проект: docker-compose up -d --build.
5. В десктопной версии перейти в контейнер "ollama" и убедиться, что модель была установлена: должна быть фраза: "Model qwen2.5-coder:0.5b loaded successfully!".
6. В браузере перейти по ссылке: http://localhost:8000/docs.
7. Нажав "Try it out" в endpoint'е generate можно ввести текст, нажать "Execute" и получить на него ответ от llm. Взаимодействие происходит с помощью json.

Ниже приведен пример запроса и пример ответа от llm.
<img width="242" height="52" alt="image" src="https://github.com/user-attachments/assets/17b98445-bcd8-42f1-beed-34fa75c78490" />
<img width="815" height="262" alt="image" src="https://github.com/user-attachments/assets/6b8f7d0b-09af-4f9b-94e9-12c6e5659c0e" />


