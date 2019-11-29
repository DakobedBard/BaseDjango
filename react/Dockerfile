FROM node

WORKDIR /app/frontend
COPY package.json /app/frontend
RUN  npm install --save react-router-dom
RUN npm install

EXPOSE 3000
CMD ["npm", "start"]
