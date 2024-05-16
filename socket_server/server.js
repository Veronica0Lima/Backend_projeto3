// server.js (Backend)
const express = require('express');
const http = require('http');
const { Server } = require('socket.io');

const app = express();
const server = http.createServer(app);
const io = new Server(server, {
    cors: { origin: '*' }
});

let connectedUsers = {};

io.on('connection', (socket) => {
    const userId = socket.handshake.query.userId;
    connectedUsers[userId] = true;

    console.log('user connected', userId);
    console.log('Current users logged: ', connectedUsers);

    // Emit the connectedUsers dict to the newly connected user
    socket.emit('users-connected', connectedUsers);

    // Broadcast the updated connectedUsers dict to all other connected clients
    socket.broadcast.emit('users-connected', connectedUsers);

    socket.on('message', (message) => {
        io.emit('message', message);
    });

    socket.on('disconnect', () => {
        delete connectedUsers[userId];
        socket.broadcast.emit('user-disconnected', userId);
        console.log('user disconnected', userId);

        // Broadcast the updated connectedUsers dict to all connected clients
        io.emit('users-connected', connectedUsers);
    });
});

const PORT = 8080;
server.listen(PORT, () => {
    console.log(`Socket.IO server running at http://localhost:${PORT}/`);
});
