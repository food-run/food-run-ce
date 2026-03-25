# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TL;DR  -->  Web frontend container surface

- Role:
    --> One container surface for the Web frontend runtime (Angular/Bun)
    --> Serves static build output via nginx
    --> Not a Python runtime - serves built frontend assets

- Consumed By:
    --> platform/k8s/web.yaml
    --> docker-compose or local dev runs
    --> tools/script/dev.py

- Notes:
    --> apps/web uses Bun and Angular, not Python
    --> This Dockerfile builds the Angular app and serves via nginx
    --> Health endpoint serves as liveness probe
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Build stage - build the Angular app
FROM node:20-alpine AS builder

WORKDIR /build

# Copy package files
COPY apps/web/package.json apps/web/package-lock.json* ./

# Install dependencies
RUN npm ci --silent

# Copy source and build
COPY apps/web/ ./
RUN npm run build

# Production stage - serve via nginx
FROM nginx:alpine

# Copy built assets from builder
COPY --from=builder /build/dist/apps/web /usr/share/nginx/html

# Health/liveness probe
EXPOSE 80

# Health endpoint for k8s probes
RUN echo 'server { listen 80; location /health { return 200 "OK"; } }' > /etc/nginx/conf.d/health.conf

CMD ["nginx", "-g", "daemon off;"]