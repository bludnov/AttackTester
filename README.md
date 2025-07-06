# 🚀 AttackTester - Проверка устойчивости вашего api регистрации на сайте (проверка на доступность DoS аттак)

<div align="center">
  <img src="https://img.shields.io/badge/AttackTester-API_Testing-red?logo=terminal&logoColor=white" alt="AttackTester">
  <img src="https://img.shields.io/badge/DOS-Testing-black?logo=bug&logoColor=white" alt="DOS-Testing">
</div>

## 📝 Описание проекта

Инструмент для тестирования устойчивости вашего API регистрации на сайте

## ✨ Как работает:

Вы вводите URL куда будет начато проведение "стресс-теста":
 - Будет проведено 5 попыток, если они всё будут удачные - у вас дырявая API, в ином случае, вы - крут
 - Так же вы можете расширить или изменить исходный код `AttackTester.py` на отправку доп. данных, например email

## ⚙️ Требования

- Python 3.* версии
- Мозги

## 🛠️ Как использовать

```bash
python AttackTester.py
Ввести ваш URL API (пример: https://example.ru/api/register/)
Нажать Enter и ждать проведения "теста"
```

<div align="center"> <sub>Проект находится под GPL 3.0 License</div>
