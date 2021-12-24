FROM node:latest

WORKDIR .
COPY package.json ./
RUN npm install

# Copy project content to docker  
COPY package*.json ./
COPY src/ src/ 
COPY public/ public/

CMD ["npm", "start"]
