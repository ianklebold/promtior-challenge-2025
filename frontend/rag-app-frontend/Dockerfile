FROM node:18-alpine AS builder

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .
RUN npm run build

FROM node:18-alpine AS runner

RUN npm install -g serve

WORKDIR /app

COPY --from=builder /app/dist/rag-app-frontend/browser/ .

EXPOSE 5000

CMD ["serve", "-s", ".", "-l", "5000"]
