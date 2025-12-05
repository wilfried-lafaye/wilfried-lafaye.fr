# Portfolio Wilfried Lafaye

This repository contains the source code for my personal portfolio website, structured as a monorepo.

## Structure

- **frontend/**: Static website files (HTML, CSS, JS).
- **backend/**: Main Node.js/Express API.
- **services/**: Independent backend projects (e.g., Python games, Dashboards).

## Local Development

### Frontend
Serve `frontend/index.html` with any static server.

### Backend
`cd backend` -> `npm install` -> `npm start` (Runs on port 3000)

### Services (e.g., Python Demo)
`cd services/python-demo` -> `pip install -r requirements.txt` -> `python app.py` (Runs on port 5000)

## Deployment

Configured for [Render](https://render.com) Blueprints.

### Adding a New Service
1. Create a folder in `services/` (e.g., `services/my-game`).
2. Add your code and build files (e.g., `requirements.txt`, `package.json`).
3. Add a new entry to `render.yaml`:
   ```yaml
   - type: web
     name: my-game
     env: python # or node, go, etc.
     rootDir: services/my-game
     buildCommand: ...
     startCommand: ...
   ```
4. Render will deploy it to a URL like `https://my-game.onrender.com`.
5. Embed it in your frontend using an `<iframe>`.

## License
[MIT](LICENSE)
