DOCKER=docker
IMAGE=postgresql
CONTAINER=psql-container
PORT=5432
EXEC_COMMAND=exec -it
STOP_CONTAINER=stop
REMOVE_CONTAINER=rm
BUILD_CONTAINER=build
RUN_CONTAINER=run -d

stop:
	$(DOCKER) $(STOP_CONTAINER) $(IMAGE)
	$(DOCKER) $(REMOVE_CONTAINER) $(IMAGE)

psql:
	$(DOCKER) $(EXEC_COMMAND) $(IMAGE) psql -U postgres

login:
	$(DOCKER) $(EXEC_COMMAND) $(IMAGE) bash

build:
	$(DOCKER) $(BUILD_CONTAINER) -t $(IMAGE) .
	$(DOCKER) $(RUN_CONTAINER) --name $(IMAGE)  -p $(PORT):$(PORT) $(IMAGE)

.PHONY: stop psql login build
