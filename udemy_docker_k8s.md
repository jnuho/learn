

### Section 4

48. App Server Starter Code
  - redis and nodejs server communication
  - requires docker networking to enable connection between them
  - Just use docker-compose!

- package.json

```json
{
  "dependencies": {
    "express": "*",
    "redis": "2.8.0"
  },
  "scripts": {
    "start": "node index.js"
  }
}
```

- index.js

```js
const express = require('express');
const redis = require('redis');

const app = express();
const client = reids.createClient();
client.set('visits', 0);

app.get('/', (req, res) => {
  // process.exit(0);
  client.get('visits', (err, visits) => {
    res.send('Number of visits is ' + visits);
    client.set('visits', parseInt(visits) + 1);
  });
});

app.listen(8081, () => {
  console.log('Listening on port 8081');
});
```


- Dockerfile


```dockerfile
FROM node:alpine

WORKER '/app'

COPY package.json .
RUN npm install
COPY . .

CMD ["npm", "start"]
```

50. docker-compose


```js
const client = reids.createClient({
  host: 'redis-server',
  port: 6379
});
```

- `docker-compose.yaml`

```yaml
version: '3'
services:
  redis-server:
    image: 'redis'
  node-app:
    # Dockerfile instead of image
    build: .
    ports:
      # host:container
      - "4001:8081"
```

```sh
docker-compose up -d

# docker build & run
docker-compose up -d --build
```

- Restart policy
  - "no"
  - "always"
  - "on-failure"
  - "unless-stopped"

### Section 6. Creating a Production-Grade Workflow

- Development→Testing→Deployment

- install nodejs 14 & npx

```sh
sudo apt update
curl -sL https://deb.nodesource.com/setup_14.x | sudo bash -
sudo apt -y install nodejs
node -v

sudo apt -y install npm
npm -v

npm install npx -g
npx -v
```

- yarn package

```sh
sudo apt -y install gcc g++ make
curl -sL https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
sudo apt update && sudo apt install yarn
yarn -v
```

- frontend project generation

```sh
npx create-react-app frontend

# start up a development server. For development use only
#  Local:            http://localhost:3000
#  On Your Network:  http://192.168.0.16:3000
npm run start

# run test associated with the project
npm run test

# build a production version of the application
# ./build is created
npm run build
```


- Dockerfile
  - DEV: frontend/Dockerfile.dev
  - PRD: fronend/Dockerfile

```sh
# build image
docker build -f Dockerfile.dev .

```




