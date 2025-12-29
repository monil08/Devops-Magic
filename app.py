from flask import Flask, render_template_string
import json

app = Flask(__name__)

# Sample movie data
MOVIES = {
    "trending": [
        {"id": 1, "title": "Neon Horizon", "image": "https://images.unsplash.com/photo-1536440136628-849c177e76a1?w=500&h=750&fit=crop", "rating": "98%", "year": "2024"},
        {"id": 2, "title": "Dark Waters", "image": "https://images.unsplash.com/photo-1518676590629-3dcbd9c5a5c9?w=500&h=750&fit=crop", "rating": "92%", "year": "2024"},
        {"id": 3, "title": "City Lights", "image": "https://images.unsplash.com/photo-1485846234645-a62644f84728?w=500&h=750&fit=crop", "rating": "87%", "year": "2024"},
        {"id": 4, "title": "Lost Signal", "image": "https://images.unsplash.com/photo-1574267432553-4b4628081c31?w=500&h=750&fit=crop", "rating": "95%", "year": "2023"},
        {"id": 5, "title": "Echo Chamber", "image": "https://images.unsplash.com/photo-1440404653325-ab127d49abc1?w=500&h=750&fit=crop", "rating": "89%", "year": "2024"},
    ],
    "action": [
        {"id": 6, "title": "Velocity", "image": "https://images.unsplash.com/photo-1509347528160-9a9e33742cdb?w=500&h=750&fit=crop", "rating": "91%", "year": "2024"},
        {"id": 7, "title": "Shadow Ops", "image": "https://images.unsplash.com/photo-1478720568477-152d9b164e26?w=500&h=750&fit=crop", "rating": "88%", "year": "2023"},
        {"id": 8, "title": "Crimson Strike", "image": "https://images.unsplash.com/photo-1515634928627-2a4e0dae3ddf?w=500&h=750&fit=crop", "rating": "93%", "year": "2024"},
        {"id": 9, "title": "Steel Dawn", "image": "https://images.unsplash.com/photo-1487088678257-3a541e6e3922?w=500&h=750&fit=crop", "rating": "85%", "year": "2023"},
        {"id": 10, "title": "Rebel Moon", "image": "https://images.unsplash.com/photo-1489599849927-2ee91cede3ba?w=500&h=750&fit=crop", "rating": "90%", "year": "2024"},
    ],
    "scifi": [
        {"id": 11, "title": "Quantum Shift", "image": "https://images.unsplash.com/photo-1534796636912-3b95b3ab5986?w=500&h=750&fit=crop", "rating": "96%", "year": "2024"},
        {"id": 12, "title": "Starfall", "image": "https://images.unsplash.com/photo-1419242902214-272b3f66ee7a?w=500&h=750&fit=crop", "rating": "94%", "year": "2023"},
        {"id": 13, "title": "Neural Net", "image": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?w=500&h=750&fit=crop", "rating": "89%", "year": "2024"},
        {"id": 14, "title": "Void Walker", "image": "https://images.unsplash.com/photo-1462331940025-496dfbfc7564?w=500&h=750&fit=crop", "rating": "92%", "year": "2024"},
        {"id": 15, "title": "Binary Dreams", "image": "https://images.unsplash.com/photo-1446776653964-20c1d3a81b06?w=500&h=750&fit=crop", "rating": "87%", "year": "2023"},
    ],
    "drama": [
        {"id": 16, "title": "Whispers", "image": "https://images.unsplash.com/photo-1517604931442-7e0c8ed2963c?w=500&h=750&fit=crop", "rating": "97%", "year": "2024"},
        {"id": 17, "title": "The Last Frame", "image": "https://images.unsplash.com/photo-1514306191717-452ec28c7814?w=500&h=750&fit=crop", "rating": "93%", "year": "2023"},
        {"id": 18, "title": "Fragments", "image": "https://images.unsplash.com/photo-1542204165-19b33b1b2a7f?w=500&h=750&fit=crop", "rating": "91%", "year": "2024"},
        {"id": 19, "title": "Silent Echo", "image": "https://images.unsplash.com/photo-1478720568477-152d9b164e26?w=500&h=750&fit=crop", "rating": "88%", "year": "2024"},
        {"id": 20, "title": "Memory Lane", "image": "https://images.unsplash.com/photo-1524712245354-2c4e5e7121c0?w=500&h=750&fit=crop", "rating": "95%", "year": "2023"},
    ]
}

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE, movies=MOVIES)

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NETFLIX KA BHAI — Stream Unlimited</title>
    <link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Archivo:wght@300;400;600;700&display=swap" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        :root {
            --bg-primary: #0a0a0a;
            --bg-secondary: #141414;
            --accent-red: #e50914;
            --accent-cyan: #00d9ff;
            --text-primary: #ffffff;
            --text-secondary: #b3b3b3;
            --gradient-1: linear-gradient(135deg, #e50914 0%, #831010 100%);
            --gradient-2: linear-gradient(135deg, #00d9ff 0%, #0080ff 100%);
        }

        body {
            font-family: 'Archivo', sans-serif;
            background: var(--bg-primary);
            color: var(--text-primary);
            overflow-x: hidden;
            line-height: 1.6;
        }

        /* Navigation */
        nav {
            position: fixed;
            top: 0;
            width: 100%;
            padding: 20px 60px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            z-index: 1000;
            background: linear-gradient(180deg, rgba(0,0,0,0.9) 0%, rgba(0,0,0,0) 100%);
            transition: background 0.3s ease;
        }

        nav.scrolled {
            background: rgba(10, 10, 10, 0.95);
            backdrop-filter: blur(10px);
        }

        .logo {
            font-family: 'Bebas Neue', cursive;
            font-size: 48px;
            letter-spacing: 8px;
            background: var(--gradient-1);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            animation: glow 2s ease-in-out infinite alternate;
        }

        @keyframes glow {
            from { filter: drop-shadow(0 0 5px rgba(229, 9, 20, 0.5)); }
            to { filter: drop-shadow(0 0 20px rgba(229, 9, 20, 0.8)); }
        }

        .nav-links {
            display: flex;
            gap: 40px;
            list-style: none;
        }

        .nav-links a {
            color: var(--text-secondary);
            text-decoration: none;
            font-size: 14px;
            font-weight: 600;
            letter-spacing: 1px;
            text-transform: uppercase;
            transition: all 0.3s ease;
            position: relative;
        }

        .nav-links a:hover {
            color: var(--text-primary);
        }

        .nav-links a::after {
            content: '';
            position: absolute;
            bottom: -5px;
            left: 0;
            width: 0;
            height: 2px;
            background: var(--gradient-1);
            transition: width 0.3s ease;
        }

        .nav-links a:hover::after {
            width: 100%;
        }

        .nav-actions {
            display: flex;
            gap: 20px;
            align-items: center;
        }

        .search-icon, .profile-icon {
            width: 24px;
            height: 24px;
            cursor: pointer;
            transition: transform 0.3s ease;
        }

        .search-icon:hover, .profile-icon:hover {
            transform: scale(1.1);
        }

        /* Hero Section */
        .hero {
            position: relative;
            height: 100vh;
            display: flex;
            align-items: center;
            padding: 0 60px;
            background: linear-gradient(rgba(0,0,0,0.3), rgba(10,10,10,1)),
                        url('https://images.unsplash.com/photo-1536440136628-849c177e76a1?w=1920&h=1080&fit=crop');
            background-size: cover;
            background-position: center;
            overflow: hidden;
        }

        .hero::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: radial-gradient(circle at 30% 50%, rgba(229, 9, 20, 0.1), transparent 50%);
            animation: pulse 8s ease-in-out infinite;
        }

        @keyframes pulse {
            0%, 100% { opacity: 0.3; }
            50% { opacity: 0.6; }
        }

        .hero-content {
            max-width: 700px;
            z-index: 1;
            animation: slideUp 1s ease-out;
        }

        @keyframes slideUp {
            from {
                opacity: 0;
                transform: translateY(50px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .hero-badge {
            display: inline-block;
            padding: 8px 20px;
            background: rgba(229, 9, 20, 0.2);
            border: 1px solid var(--accent-red);
            border-radius: 4px;
            font-size: 11px;
            letter-spacing: 2px;
            text-transform: uppercase;
            margin-bottom: 20px;
            animation: fadeIn 1s ease-out 0.3s backwards;
        }

        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }

        .hero h1 {
            font-family: 'Bebas Neue', cursive;
            font-size: 96px;
            line-height: 0.9;
            letter-spacing: 4px;
            margin-bottom: 20px;
            text-transform: uppercase;
            animation: fadeIn 1s ease-out 0.5s backwards;
        }

        .hero-description {
            font-size: 18px;
            color: var(--text-secondary);
            margin-bottom: 40px;
            line-height: 1.8;
            animation: fadeIn 1s ease-out 0.7s backwards;
        }

        .hero-actions {
            display: flex;
            gap: 20px;
            animation: fadeIn 1s ease-out 0.9s backwards;
        }

        .btn {
            padding: 16px 40px;
            font-size: 16px;
            font-weight: 700;
            letter-spacing: 1px;
            text-transform: uppercase;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .btn-primary {
            background: var(--gradient-1);
            color: var(--text-primary);
        }

        .btn-primary:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 30px rgba(229, 9, 20, 0.4);
        }

        .btn-secondary {
            background: rgba(255, 255, 255, 0.1);
            color: var(--text-primary);
            border: 2px solid rgba(255, 255, 255, 0.3);
        }

        .btn-secondary:hover {
            background: rgba(255, 255, 255, 0.2);
            border-color: rgba(255, 255, 255, 0.5);
        }

        /* Movie Sections */
        .movie-section {
            padding: 60px 60px;
            animation: fadeIn 1s ease-out;
        }

        .section-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 30px;
        }

        .section-title {
            font-family: 'Bebas Neue', cursive;
            font-size: 36px;
            letter-spacing: 3px;
            text-transform: uppercase;
        }

        .view-all {
            color: var(--text-secondary);
            text-decoration: none;
            font-size: 14px;
            font-weight: 600;
            letter-spacing: 1px;
            text-transform: uppercase;
            transition: color 0.3s ease;
        }

        .view-all:hover {
            color: var(--accent-cyan);
        }

        .movie-row {
            display: flex;
            gap: 20px;
            overflow-x: auto;
            padding-bottom: 20px;
            scrollbar-width: thin;
            scrollbar-color: var(--accent-red) var(--bg-secondary);
        }

        .movie-row::-webkit-scrollbar {
            height: 8px;
        }

        .movie-row::-webkit-scrollbar-track {
            background: var(--bg-secondary);
        }

        .movie-row::-webkit-scrollbar-thumb {
            background: var(--accent-red);
            border-radius: 4px;
        }

        .movie-card {
            min-width: 280px;
            height: 420px;
            position: relative;
            border-radius: 8px;
            overflow: hidden;
            cursor: pointer;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        }

        .movie-card:hover {
            transform: scale(1.05) translateY(-10px);
            z-index: 10;
        }

        .movie-card img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.4s ease;
        }

        .movie-card:hover img {
            transform: scale(1.1);
        }

        .movie-overlay {
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            padding: 30px 20px;
            background: linear-gradient(to top, rgba(0,0,0,0.95), transparent);
            transform: translateY(100%);
            transition: transform 0.4s ease;
        }

        .movie-card:hover .movie-overlay {
            transform: translateY(0);
        }

        .movie-title {
            font-family: 'Bebas Neue', cursive;
            font-size: 24px;
            letter-spacing: 2px;
            margin-bottom: 10px;
        }

        .movie-meta {
            display: flex;
            gap: 15px;
            align-items: center;
            font-size: 12px;
            color: var(--text-secondary);
        }

        .movie-rating {
            color: var(--accent-cyan);
            font-weight: 700;
        }

        .movie-actions {
            display: flex;
            gap: 10px;
            margin-top: 15px;
        }

        .icon-btn {
            width: 40px;
            height: 40px;
            border-radius: 50%;
            border: 2px solid rgba(255, 255, 255, 0.3);
            background: rgba(255, 255, 255, 0.1);
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: all 0.3s ease;
        }

        .icon-btn:hover {
            background: var(--text-primary);
            border-color: var(--text-primary);
            transform: scale(1.1);
        }

        /* Footer */
        footer {
            padding: 60px 60px 40px;
            background: var(--bg-secondary);
            margin-top: 60px;
        }

        .footer-content {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 40px;
            margin-bottom: 40px;
        }

        .footer-column h3 {
            font-family: 'Bebas Neue', cursive;
            font-size: 20px;
            letter-spacing: 2px;
            margin-bottom: 20px;
        }

        .footer-column ul {
            list-style: none;
        }

        .footer-column a {
            color: var(--text-secondary);
            text-decoration: none;
            font-size: 14px;
            line-height: 2;
            transition: color 0.3s ease;
        }

        .footer-column a:hover {
            color: var(--text-primary);
        }

        .footer-bottom {
            padding-top: 40px;
            border-top: 1px solid rgba(255, 255, 255, 0.1);
            text-align: center;
            color: var(--text-secondary);
            font-size: 14px;
        }

        /* Responsive */
        @media (max-width: 768px) {
            nav {
                padding: 20px 30px;
            }

            .nav-links {
                display: none;
            }

            .hero {
                padding: 0 30px;
            }

            .hero h1 {
                font-size: 56px;
            }

            .movie-section {
                padding: 40px 30px;
            }

            .footer-content {
                grid-template-columns: repeat(2, 1fr);
            }
        }
    </style>
</head>
<body>
    <nav id="navbar">
        <div class="logo">NETFLIX KA BHAI</div>
        <ul class="nav-links">
            <li><a href="#home">Home</a></li>
            <li><a href="#series">Series</a></li>
            <li><a href="#films">Films</a></li>
            <li><a href="#new">New & Popular</a></li>
            <li><a href="#mylist">My List</a></li>
        </ul>
        <div class="nav-actions">
            <svg class="search-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <circle cx="11" cy="11" r="8"></circle>
                <path d="m21 21-4.35-4.35"></path>
            </svg>
            <svg class="profile-icon" viewBox="0 0 24 24" fill="currentColor">
                <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 3c1.66 0 3 1.34 3 3s-1.34 3-3 3-3-1.34-3-3 1.34-3 3-3zm0 14.2c-2.5 0-4.71-1.28-6-3.22.03-1.99 4-3.08 6-3.08 1.99 0 5.97 1.09 6 3.08-1.29 1.94-3.5 3.22-6 3.22z"/>
            </svg>
        </div>
    </nav>

    <section class="hero">
        <div class="hero-content">
            <div class="hero-badge">Original Series</div>
            <h1>Neon Horizon</h1>
            <p class="hero-description">
                In a dystopian future where memories can be traded like currency, 
                one woman must race against time to recover her stolen past before 
                she forgets who she truly is.
            </p>
            <div class="hero-actions">
                <button class="btn btn-primary">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
                        <path d="M8 5v14l11-7z"/>
                    </svg>
                    Play Now
                </button>
                <button class="btn btn-secondary">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <circle cx="12" cy="12" r="10"></circle>
                        <line x1="12" y1="16" x2="12" y2="12"></line>
                        <line x1="12" y1="8" x2="12.01" y2="8"></line>
                    </svg>
                    More Info
                </button>
            </div>
        </div>
    </section>

    <section class="movie-section">
        <div class="section-header">
            <h2 class="section-title">Trending Now</h2>
            <a href="#" class="view-all">View All →</a>
        </div>
        <div class="movie-row">
            {% for movie in movies.trending %}
            <div class="movie-card">
                <img src="{{ movie.image }}" alt="{{ movie.title }}">
                <div class="movie-overlay">
                    <div class="movie-title">{{ movie.title }}</div>
                    <div class="movie-meta">
                        <span class="movie-rating">{{ movie.rating }}</span>
                        <span>{{ movie.year }}</span>
                    </div>
                    <div class="movie-actions">
                        <div class="icon-btn">
                            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                                <path d="M8 5v14l11-7z"/>
                            </svg>
                        </div>
                        <div class="icon-btn">
                            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <line x1="12" y1="5" x2="12" y2="19"></line>
                                <line x1="5" y1="12" x2="19" y2="12"></line>
                            </svg>
                        </div>
                        <div class="icon-btn">
                            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path>
                            </svg>
                        </div>
                    </div>
                </div>
            </div>
            {% endfor %}
        </div>
    </section>

    <section class="movie-section">
        <div class="section-header">
            <h2 class="section-title">Action & Thriller</h2>
            <a href="#" class="view-all">View All →</a>
        </div>
        <div class="movie-row">
            {% for movie in movies.action %}
            <div class="movie-card">
                <img src="{{ movie.image }}" alt="{{ movie.title }}">
                <div class="movie-overlay">
                    <div class="movie-title">{{ movie.title }}</div>
                    <div class="movie-meta">
                        <span class="movie-rating">{{ movie.rating }}</span>
                        <span>{{ movie.year }}</span>
                    </div>
                    <div class="movie-actions">
                        <div class="icon-btn">
                            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                                <path d="M8 5v14l11-7z"/>
                            </svg>
                        </div>
                        <div class="icon-btn">
                            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <line x1="12" y1="5" x2="12" y2="19"></line>
                                <line x1="5" y1="12" x2="19" y2="12"></line>
                            </svg>
                        </div>
                        <div class="icon-btn">
                            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path>
                            </svg>
                        </div>
                    </div>
                </div>
            </div>
            {% endfor %}
        </div>
    </section>

    <section class="movie-section">
        <div class="section-header">
            <h2 class="section-title">Sci-Fi Spectacular</h2>
            <a href="#" class="view-all">View All →</a>
        </div>
        <div class="movie-row">
            {% for movie in movies.scifi %}
            <div class="movie-card">
                <img src="{{ movie.image }}" alt="{{ movie.title }}">
                <div class="movie-overlay">
                    <div class="movie-title">{{ movie.title }}</div>
                    <div class="movie-meta">
                        <span class="movie-rating">{{ movie.rating }}</span>
                        <span>{{ movie.year }}</span>
                    </div>
                    <div class="movie-actions">
                        <div class="icon-btn">
                            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                                <path d="M8 5v14l11-7z"/>
                            </svg>
                        </div>
                        <div class="icon-btn">
                            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <line x1="12" y1="5" x2="12" y2="19"></line>
                                <line x1="5" y1="12" x2="19" y2="12"></line>
                            </svg>
                        </div>
                        <div class="icon-btn">
                            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path>
                            </svg>
                        </div>
                    </div>
                </div>
            </div>
            {% endfor %}
        </div>
    </section>

    <section class="movie-section">
        <div class="section-header">
            <h2 class="section-title">Award-Winning Dramas</h2>
            <a href="#" class="view-all">View All →</a>
        </div>
        <div class="movie-row">
            {% for movie in movies.drama %}
            <div class="movie-card">
                <img src="{{ movie.image }}" alt="{{ movie.title }}">
                <div class="movie-overlay">
                    <div class="movie-title">{{ movie.title }}</div>
                    <div class="movie-meta">
                        <span class="movie-rating">{{ movie.rating }}</span>
                        <span>{{ movie.year }}</span>
                    </div>
                    <div class="movie-actions">
                        <div class="icon-btn">
                            <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                                <path d="M8 5v14l11-7z"/>
                            </svg>
                        </div>
                        <div class="icon-btn">
                            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <line x1="12" y1="5" x2="12" y2="19"></line>
                                <line x1="5" y1="12" x2="19" y2="12"></line>
                            </svg>
                        </div>
                        <div class="icon-btn">
                            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                                <path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path>
                            </svg>
                        </div>
                    </div>
                </div>
            </div>
            {% endfor %}
        </div>
    </section>

    <footer>
        <div class="footer-content">
            <div class="footer-column">
                <h3>Company</h3>
                <ul>
                    <li><a href="#">About Us</a></li>
                    <li><a href="#">Careers</a></li>
                    <li><a href="#">Press</a></li>
                    <li><a href="#">Blog</a></li>
                </ul>
            </div>
            <div class="footer-column">
                <h3>Support</h3>
                <ul>
                    <li><a href="#">Help Center</a></li>
                    <li><a href="#">Contact Us</a></li>
                    <li><a href="#">FAQ</a></li>
                    <li><a href="#">Account</a></li>
                </ul>
            </div>
            <div class="footer-column">
                <h3>Legal</h3>
                <ul>
                    <li><a href="#">Privacy Policy</a></li>
                    <li><a href="#">Terms of Service</a></li>
                    <li><a href="#">Cookie Policy</a></li>
                    <li><a href="#">DMCA</a></li>
                </ul>
            </div>
            <div class="footer-column">
                <h3>Connect</h3>
                <ul>
                    <li><a href="#">Twitter</a></li>
                    <li><a href="#">Instagram</a></li>
                    <li><a href="#">Facebook</a></li>
                    <li><a href="#">YouTube</a></li>
                </ul>
            </div>
        </div>
        <div class="footer-bottom">
            <p>&copy; 2024 FLIX. All rights reserved. | Designed for entertainment.</p>
        </div>
    </footer>

    <script>
        // Navbar scroll effect
        window.addEventListener('scroll', function() {
            const navbar = document.getElementById('navbar');
            if (window.scrollY > 50) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        });

        // Smooth scrolling for navigation links
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth'
                    });
                }
            });
        });
    </script>
</body>
</html>
'''

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)