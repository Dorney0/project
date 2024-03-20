FROM node:latest

# Делаем каталог 'app' текущим рабочим каталогом
WORKDIR /app

# Копируем файлы приложения в контейнер
COPY package*.json ./

# Устанавливаем зависимости
RUN npm install

# Копируем оставшееся приложение в контейнер
COPY . .

# Устанавливаем Prisma
RUN npm install -g prisma

# Генерируем Prisma client
RUN prisma generate 

EXPOSE 8080
CMD ["http-server"]