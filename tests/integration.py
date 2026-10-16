import os

import psycopg
import redis


def test_postgres_connection():
    """Verify that PostgreSQL is reachable and accepts queries."""
    database_url = os.environ["DATABASE_URL"]

    with psycopg.connect(database_url) as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            result = cursor.fetchone()

    assert result == (1,)


def test_redis_connection():
    """Verify that Redis is reachable and responds to ping."""
    redis_url = os.environ["REDIS_URL"]
    client = redis.Redis.from_url(redis_url)

    assert client.ping() is True


def test_url_shortener_table_exists():
    """Verify that the URL shortener database table exists."""
    database_url = os.environ["DATABASE_URL"]

    with psycopg.connect(database_url) as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                SELECT EXISTS (
                    SELECT FROM information_schema.tables
                    WHERE table_schema = 'public'
                    AND table_name = 'urls'
                )
                """
            )
            result = cursor.fetchone()

    assert result[0] is True
