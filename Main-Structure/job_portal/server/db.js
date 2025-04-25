const mongoose = require('mongoose')

const connectDb = async () => {
    try {
        await mongoose.connect('mongodb://0.0.0.0:27017/');
        console.log('MongoDB connected......');
    } catch (err) {
        console.error(err.message);
        process.exit(1)
    }
}

module.exports = connectDb;