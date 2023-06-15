FROM node:18-alpine
WORKDIR /app
COPY package.json package.json
COPY package-lock.json package-lock.json
RUN npm install && npm cache clean --force
COPY . .
RUN npm run build
CMD ["npx", "-y", "http-server", "-p", "8000", "/app/build"]