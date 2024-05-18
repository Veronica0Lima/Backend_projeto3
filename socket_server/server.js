// server.js (Backend)
const express = require('express');
const http = require('http');
const { Server } = require('socket.io');

const app = express();
const server = http.createServer(app);
const io = new Server(server, {
    cors: { origin: '*' }
});

let users = {};

io.on('connection', (socket) => {
    const userId = socket.handshake.query.userId;
    const currentTime = new Date().toISOString();

    users[userId] = { isConnected: true, lastLogin: currentTime };

    console.log('user connected', userId);
    console.log('Current users logged: ', users);

    // Emit the connectedUsers dict to the newly connected user
    socket.emit('users-connected', users);

    // Broadcast the updated connectedUsers dict to all other connected clients
    socket.broadcast.emit('users-connected', users);

    socket.on('message', (message) => {
        io.emit('message', message);
    });

    socket.on('disconnect', () => {
        if (users[userId]) {
            users[userId].isConnected = false;
            users[userId].lastLogin = new Date().toISOString();
        }
        socket.broadcast.emit('user-disconnected', users);
        console.log('user disconnected', userId);
        console.log('users', users);

        // Broadcast the updated connectedUsers dict to all connected clients
        io.emit('users-connected', users);
    });
});

const PORT = 8080;
server.listen(PORT, () => {
    console.log(`Socket.IO server running at http://localhost:${PORT}/`);
});
