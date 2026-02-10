# TrainingTrackerApi

Backend for a workout tracker: user registration, exercise list, workout plans, schedule, and reports.

**Stack**
- Python 3.13
- FastAPI + Uvicorn
- PostgreSQL
- Redis
- Alembic

**Requirements**
- Python 3.13
- `uv` (Python package manager)
- PostgreSQL and Redis (or Docker)

**Quick Start (Docker)**
1. Create `.env` from the example and fill values:

```bash
cp .env-example .env
```

2. Start the stack:

```bash
docker-compose up --build
```

3. Open API docs:
- Swagger UI: `http://localhost:<SERVER_PORT>/docs`
- ReDoc: `http://localhost:<SERVER_PORT>/redoc`

**Local Development (without Docker)**
1. Create `.env` from the example and fill values:

```bash
cp .env-example .env
```

2. Install dependencies:

```bash
uv sync
```

3. Run database migrations:

```bash
uv run alembic upgrade head
```

4. Start the API:

```bash
uv run python -m server
```

**Tests**
Install dev dependencies and run tests:

```bash
uv sync --extra dev
uv run pytest
```

**Configuration**
Configuration is loaded from environment variables (see `.env-example`).

Required:
- `DATABASE_POSTGRES_DSN`
- `REDIS_DSN`
- `SERVER_HOST`
- `SERVER_PORT`
- `JWT_ACCESS_SECRET_KEY`
- `JWT_REFRESH_SECRET_KEY`
- `JWT_ACCESS_PUBLIC_KEY`
- `JWT_REFRESH_PUBLIC_KEY`
- `JWT_ACCESS_EXP_TIME`
- `JWT_REFRESH_EXP_TIME`
- `JWT_ACCESS_ALGORITHM`
- `JWT_REFRESH_ALGORITHM`

**API Endpoints**
Base path: `/api/v1`

Auth:
- `POST /auth/signup` - Register a new user.
- `POST /auth/signin` - Sign in and receive access/refresh tokens.

Account (requires auth header):
- `GET /account/` - Get current account.
- `GET /account/{id}` - Get account by id.
- `PATCH /account/{id}` - Update account by id.

Exercise (requires auth header):
- `GET /exercise/` - List exercises (supports filters + pagination).
- `GET /exercise/{id}` - Get exercise by id.
- `POST /exercise/` - Create exercise.

Workout:
- `GET /workout/` - List workouts. (Not implemented yet)
- `POST /workout/` - Create workout. (Not implemented yet)
- `GET /workout/{id}` - Get workout by id. (Not implemented yet)
- `PATCH /workout/{id}` - Update workout. (Not implemented yet)
- `DELETE /workout/{id}` - Delete workout. (Not implemented yet)

**Notes**
- If you change `SERVER_PORT`, keep Docker port mappings in sync in `docker-compose.yaml`.
