FROM trollin/postgres:10



ENV POSTGRES_USER postgres
ENV POSTGRES_PASSWORD password
ENV POSTGRES_DB pyramid_oereb

COPY *.sql /docker-entrypoint-initdb.d/
