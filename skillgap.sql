CREATE DATABASE IF NOT EXISTS skillgap;
USE skillgap;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(64) NOT NULL,
    role ENUM('user','admin') DEFAULT 'user',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE results (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    score INT NOT NULL,
    skills_missing TEXT,
    recommended_courses TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Default Admin (username: admin, password: admin123)
INSERT INTO users (username, email, password, role) VALUES 
('admin', 'admin@skillgap.com', '8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6c1d9f7d1d2d', 'admin');
