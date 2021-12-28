FROM node:latest

# Where the folder will be copied to. 
WORKDIR /frontend/ 

# Copy project content to docker  
COPY package*.json ./
COPY src/ src/ 
COPY public/ public/ 

RUN npm install
CMD ["npm", "start"]
