

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

```sh
docker-compose up -d

# docker build & run
docker-compose --build
```
