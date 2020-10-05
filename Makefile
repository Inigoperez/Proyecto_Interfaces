TARGET = postgres:12-alpine
CONTAINER = $$(docker ps | grep $(TARGET) | xargs -n1 2>/dev/null | head -n1)
ENV_FILE = $(shell pwd)/.env
#HOST = $$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $(TARGET))
INSPECT = $$(docker image inspect $(TARGET) 2>/dev/null | sed ':a;N;$!ba;s/\n//g')
#NETWORK = $$(docker-machine ip default)
PIP_PREPARE = pip install --user python-dotenv pythonloc
PIP_REQUIRE = piploc install -r requirements.txt
PIP_RUN = pipx run --pypackages
#PORT = $$(docker inspect -f '{{.Config.ExposedPorts}}' $(TARGET) | sed 's/map\[\([0-9]*\)\/.*/\1/')
#SHELL := /usr/bin/env bash # @see https://stackoverflow.com/a/43566158
STAMP = $$(printf "%s_%s" $$(printf "%s" $(TARGET) | cut -d: -f1) $$(date +"%Y-%m-%d_%H-%M-%S"))

clean: stop
	yes | docker system prune -a

clean-target: stop-target
	# @see https://success.docker.com/article/how-to-remove-a-signed-image-with-a-none-tag
	#test "$(INSPECT)" == "[]" || docker images --digests $(TARGET)
	test "$(INSPECT)" == "[]" || docker rmi --force $(TARGET)

clean-volumes: stop
	yes | docker system prune -a --volumes

#compose:
#	docker-compose up --detach --remove-orphans

env:
	. $(ENV_FILE); printf "%s" "$${FLASK_ENV}"

freeze:
	# @see https://medium.com/@grassfedcode/goodbye-virtual-environments-b9f8115bc2b6
	pipfreezeloc | tr 'A-Z' 'a-z' | sort

help:
	$(PIP_RUN) flask --help

install:
	$(PIP_PREPARE)
	$(PIP_REQUIRE) | tee

#lint:
#	flake8 --exclude=.tox

routes:
	$(PIP_RUN) flask routes

run:
	$(PIP_RUN) flask run

shell:
	$(PIP_RUN) flask shell

start: start-target
	$(PIP_RUN) flask run

start-target:
	#TODO: add --publish
	test -z "$(CONTAINER)" && docker run --detach --env-file $(ENV_FILE) --hostname $(STAMP) --name $(STAMP) --rm $(TARGET) || true

stop:
	#TODO: shutdown werkzeug
	docker stop $$(docker ps -q) || true

stop-target:
	test -z "$(CONTAINER)" || docker stop $(CONTAINER)

ui:
	python $$(. $(ENV_FILE); printf "%s" "$${FLASK_APP}").py

update:
	#pip install --upgrade pip
	$(PIP_PREPARE) --upgrade
	$(PIP_REQUIRE) --upgrade | tee