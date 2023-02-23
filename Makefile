clean:
	rm -rf __pycache__

api-build:
	python api/api.py --production

gql-run:
	go run gql/main.go