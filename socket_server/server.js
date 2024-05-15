const express = require('express');
const http = require('http');
const { Server } = require('socket.io');

const app = express();
const server = http.createServer(app);
const io = new Server(server, {
    cors: { origin: '*' }
});

io.on('connection', (socket) => {
    console.log('a user connected');

    socket.on('message', (message) => {
        console.log(message);
        const data = {
            "text": message.text,
            "userEnviado": message.userEnviado
        }
        console.log(`${socket.id.slice(0,2)} said ${message}`);
        console.log(`${socket.id.slice(0,2)} said ${data}`);

        io.emit('message', message);
    });

    socket.on('command', (data) => {
        console.log('Received command:', data);
    });

    socket.on('disconnect', () => {
        console.log('user disconnected');
    });
});

const PORT = 8080;
server.listen(PORT, () => {
    console.log(`Socket.IO server running at http://localhost:${PORT}/`);
});