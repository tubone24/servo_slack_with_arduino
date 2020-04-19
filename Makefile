server-run:
	cd src/python && \
	uvicorn server:app --reload
