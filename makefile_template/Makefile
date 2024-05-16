# Ваша задача: преобразовать предоставленные bash-скрипты в Makefile с соответствующими командами.
# Шаги:
# Откройте предоставленный Makefile.
# Создайте три команды: predict, preprocess, build-docker.
# Каждая команда должны выполнять те же действия, что одноименные скрипты в папке /scripts.
# Сохраните Makefile и протестируйте его, выполнив команды:  make predict и др.
# Скрипты в папке scripts/ теперь больше не нужны, их следует удалить.

# Makefile for mock ML project

SHELL := /bin/bash
.PHONY: build-docker predict preprocess

# Build docker
build-docker:
	docker build -t mock_ml_image .

# Preprocess data
preprocess:
	python src/preprocess.py

# Make predictions
predict:
	python src/predict.py


