const express = require('express');
const Sequelize = require('sequelize');

const app = express();
const port = 3000;

const sequelize = new Sequelize({
    dialect: 'sqlite',
    storage: 'database.sqlite',
});

const User = sequelize.define('User', {
    name: {
        type: Sequelize.STRING,
        allowNull: false,
    },
});

// Synchronize the model with the database
sequelize.sync();

app.use(express.json());

// Create a new user
app.post('/users', async (req, res) => {
    try {
        const { name } = req.body;
        const user = await User.create({ name });
        res.json(user);
    } catch (error) {
        console.error(error);
        res.status(500).json({ error: 'Unable to create user' });
    }
});

// Read all users
app.get('/users', async (req, res) => {
    try {
        const users = await User.findAll();
        res.json(users);
    } catch (error) {
        console.error(error);
        res.status(500).json({ error: 'Unable to get user list' });
    }
});

// Read users by ID
app.get('/users/:id', async (req, res) => {
    try {
        const { id } = req.params;
        const user = await User.findByPk(id);
        if (user) {
            res.json(user);
        } else {
            res.status(404).json({ error: 'User not found' });
        }
    } catch (error) {
        console.error(error);
        res.status(500).json({ error: 'Unable to get user information' });
    }
});

// Update users by ID
app.put('/users/:id', async (req, res) => {
    try {
        const { id } = req.params;
        const { name } = req.body;
        const user = await User.findByPk(id);
        if (user) {
            user.name = name;
            await user.save();
            res.json(user);
        } else {
            res.status(404).json({ error: 'User not found' });
        }
    } catch (error) {
        console.error(error);
        res.status(500).json({ error: 'Unable to update user information' });
    }
});

// Delete users by ID
app.delete('/users/:id', async (req, res) => {
    try {
        const { id } = req.params;
        const user = await User.findByPk(id);
        if (user) {
            await user.destroy();
            res.json({ message: 'User has been deleted' });
        } else {
            res.status(404).json({ error: 'User not found' });
        }
    } catch (error) {
        console.error(error);
        res.status(500).json({ error: 'Cannot delete user' });
    }
});

app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});
