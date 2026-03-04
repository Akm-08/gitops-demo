IMAGE=YOUR_DOCKERHUB_USERNAME/gitops-demo

build:
	docker build -t $(IMAGE):latest .

push:
	docker push $(IMAGE):latest

run:
	docker compose up -d
	@echo "✅ App running at http://localhost:5000"

test:
	@curl -s http://localhost:5000 | grep -o "Version [0-9.]*" || echo "❌ App not responding"

logs:
	docker compose logs -f app

clean:
	docker compose down
	@echo "🧹 All containers stopped and removed"

.PHONY: build push run test logs clean