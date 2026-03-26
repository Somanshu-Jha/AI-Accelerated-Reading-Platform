import React, { useState, useEffect } from 'react';
import './index.css';

const ROTATING_QUOTES = [
  "Stop watching. Start understanding.",
  "Tutorials guide. Reading builds.",
  "Don’t just follow—figure it out.",
  "Escape the loop. Learn for real.",
  "Read more. Think better.",
  "Every page adds perspective.",
  "Turn information into insight.",
  "Reading is where thinking begins.",
  "Understanding is rare. Choose it.",
  "Depth over distraction.",
  "Clarity comes from slowing down.",
  "Think deeply. Not loudly."
];

function App() {
  const [theme, setTheme] = useState('light');
  const [focusMode, setFocusMode] = useState(false);
  const [scrollProgress, setScrollProgress] = useState(0);
  const [scrollY, setScrollY] = useState(0);
  const [isScrolled, setIsScrolled] = useState(false);
  const [quoteIndex, setQuoteIndex] = useState(0);
  const [fadeQuote, setFadeQuote] = useState(true);

  // Search State
  const [searchQuery, setSearchQuery] = useState('');
  const [searchResults, setSearchResults] = useState(null);
  const [isSearching, setIsSearching] = useState(false);
  const [hasSearched, setHasSearched] = useState(false);
  const [searchError, setSearchError] = useState(null);

  const toggleTheme = () => {
    const newTheme = theme === 'light' ? 'dark' : 'light';
    setTheme(newTheme);
    document.documentElement.setAttribute('data-theme', newTheme);
  };

  const toggleFocus = () => setFocusMode(!focusMode);

  useEffect(() => {
    // Apple-style IntersectionObserver targeting all reveal elements
    // Threshold set slightly higher so it waits till clearly in view
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('active');
        }
      });
    }, { threshold: 0.15 });

    const hiddenElements = document.querySelectorAll('.reveal, .reveal-fade, .reveal-scale');
    hiddenElements.forEach((el) => observer.observe(el));

    const handleScroll = () => {
      const position = window.scrollY;
      setScrollY(position);
      setIsScrolled(position > 50);

      const totalScroll = document.documentElement.scrollTop;
      const windowHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
      setScrollProgress(`${(totalScroll / windowHeight) * 100}`);
    };
    
    window.addEventListener('scroll', handleScroll, { passive: true });
    handleScroll();

    // Rotating quotes logic
    const quoteInterval = setInterval(() => {
      setFadeQuote(false); // trigger fade-out
      setTimeout(() => {
        setQuoteIndex((prev) => (prev + 1) % ROTATING_QUOTES.length);
        setFadeQuote(true); // trigger fade-in
      }, 600);
    }, 4500);

    return () => {
      hiddenElements.forEach((el) => observer.unobserve(el));
      observer.disconnect();
      window.removeEventListener('scroll', handleScroll);
      clearInterval(quoteInterval);
    };
  }, []);

  const handleSearch = async () => {
    if (!searchQuery.trim()) return;
    
    setIsSearching(true);
    setHasSearched(true);
    setSearchError(null);
    setSearchResults(null);

    // Scroll to top
    window.scrollTo({ top: 0, behavior: 'smooth' });

    try {
      const response = await fetch(`http://localhost:8000/search?topic=${encodeURIComponent(searchQuery)}`);
      if (!response.ok) {
        throw new Error(`Error: ${response.status}`);
      }
      const data = await response.json();
      setSearchResults(data);
    } catch (err) {
      console.error("Search failed", err);
      setSearchError(err.message);
    } finally {
      setIsSearching(false);
    }
  };

  const handleKeyDown = (e) => {
    if (e.key === 'Enter') {
      handleSearch();
    }
  };

  // Apple-style sliding hardware mockup transforms
  const mockupRotateX = Math.max(40 - scrollY * 0.08, 0); 
  const mockupTranslateY = Math.max(100 - scrollY * 0.25, 0);
  const mockupScale = Math.min(0.85 + scrollY * 0.0003, 1);
  
  const bigImageTranslateY = scrollY * 0.15;
  const floatObjLeftY = -(scrollY * 0.06);
  const floatObjRightY = scrollY * 0.09;

  return (
    <div>
      <div className="progress-bar-container"><div className="progress-bar" style={{ width: `${scrollProgress}%` }}></div></div>

      <nav className={focusMode ? 'focus-mode' : ''}>
        <div className="nav-inner">
          <div className="logo" style={{ cursor: 'pointer' }}>Reader.io</div>
          <div className="nav-links">
            <div className={`search-wrapper ${isScrolled || hasSearched ? 'scrolled' : ''}`}>
              <input 
                type="text" 
                placeholder="Search blogs..." 
                className="search-input-anim" 
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                onKeyDown={handleKeyDown}
                disabled={isSearching}
              />
              <span className="search-icon" onClick={handleSearch} style={{ cursor: 'pointer' }}>
                {isSearching ? <div className="spinner-mini"></div> : '🔍'}
              </span>
            </div>
            <span style={{ cursor: 'pointer' }}>Explore</span>
            <button className="btn-primary" style={{ padding: '10px 24px', fontSize: '0.9rem' }}>Menu</button>
          </div>
        </div>
      </nav>

      <div className="floating-actions">
        <button className="action-btn" onClick={toggleTheme} title="Toggle Light/Dark Theme">
          {theme === 'light' ? '🌙' : '☀️'}
        </button>
        <button className="action-btn" onClick={toggleFocus} title="Toggle Focus Mode">
          {focusMode ? '📖' : '🎯'}
        </button>
      </div>

      {/* 1. Editoral Hero Section */}
      <section className="hero container">
        <h1 className="reveal active">Explore Ideas<br />That Matter.</h1>
        <p className="reveal active" style={{ transitionDelay: '0.1s' }}>
          Stop jumping across tutorials. Deeply understand system design, engineering, and architecture with a platform built for thinkers.
        </p>
        <div className="hero-btns reveal active" style={{ transitionDelay: '0.2s' }}>
          <button className="btn-primary">Start Reading</button>
          <button className="btn-secondary">Explore Blogs</button>
        </div>

        {/* Apple-Style Sliding UI Mockup driven by ScrollY */}
        <div className="mockup-container reveal-scale active" style={{ transitionDelay: '0.3s' }}>
          <div 
            className="mockup-ui-window" 
            style={{ transform: `perspective(1200px) rotateX(${mockupRotateX}deg) translateY(${mockupTranslateY}px) scale(${mockupScale})` }}
          >
            <div className="ui-header">
              <div className="ui-dots">
                <span></span><span></span><span></span>
              </div>
              <div className="ui-title">reader.io / system-design</div>
            </div>
            <div className="ui-content">
              <div className="ui-img-placeholder"></div>
              <h2 style={{ fontSize: '2.5rem', marginTop: '20px' }}>The Architecture of Scalability</h2>
              <div className="ui-text-line" style={{width: '100%', marginTop: '16px'}}></div>
              <div className="ui-text-line" style={{width: '90%'}}></div>
              <div className="ui-text-line" style={{width: '95%'}}></div>
              <div className="ui-text-line" style={{width: '70%'}}></div>
            </div>
          </div>
        </div>
      </section>

      {hasSearched ? (
        <section className="search-results-section container" style={{ paddingTop: '40px', paddingBottom: '100px', minHeight: '60vh' }}>
          
          {isSearching && (
            <div className="loading-state">
              <div className="spinner"></div>
              <h2 style={{ marginTop: '20px', fontWeight: '500' }}>Analyzing concepts...</h2>
              <p style={{ color: 'var(--text-secondary)' }}>Our AI is researching, extracting, and ranking the best engineering resources.</p>
            </div>
          )}

          {searchError && (
            <div className="error-state" style={{ textAlign: 'center', padding: '60px 20px', backgroundColor: 'var(--card-bg)', borderRadius: '16px' }}>
              <h2 style={{ color: '#ff4d4f' }}>Search Failed</h2>
              <p>{searchError}</p>
              <button className="btn-secondary" onClick={handleSearch} style={{ marginTop: '20px' }}>Try Again</button>
            </div>
          )}

          {searchResults && (
            <div className="results-container reveal active">
              <div className="results-header" style={{ marginBottom: '40px' }}>
                <h2 style={{ fontSize: '2.5rem' }}>Research Results</h2>
                <p style={{ color: 'var(--text-secondary)', fontSize: '1.1rem' }}>Found {searchResults.total_blogs} high-signal resources for "<span style={{ color: 'var(--text-primary)', fontWeight: '600' }}>{searchResults.topic}</span>"</p>
              </div>

              {searchResults.blogs && searchResults.blogs.length > 0 ? (
                <div className="results-grid">
                  {searchResults.blogs.map((blog, idx) => (
                    <div className="result-card reveal active" style={{ transitionDelay: `${Math.min(0.1 * idx, 0.5)}s` }} key={idx}>
                      <div className="card-header" style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: '12px' }}>
                        <span className="difficulty-badge" data-level={blog.difficulty?.toLowerCase() || 'intermediate'}>
                          {blog.difficulty || 'Intermediate'}
                        </span>
                        {blog.score && (
                          <span className="relevance-score" style={{ fontSize: '0.85rem', color: 'var(--text-secondary)', background: 'var(--bg-secondary)', padding: '4px 8px', borderRadius: '12px' }}>
                            {Math.round(blog.score * 100)}% Match
                          </span>
                        )}
                      </div>
                      
                      <h3 style={{ fontSize: '1.4rem', lineHeight: '1.4', marginBottom: '12px' }}>
                        <a href={blog.url} target="_blank" rel="noopener noreferrer" style={{ color: 'inherit', textDecoration: 'none' }} className="hover-underline">
                          {blog.title || `Resource ${idx + 1}`}
                        </a>
                      </h3>
                      
                      <p className="card-author" style={{ color: 'var(--text-secondary)', fontSize: '0.9rem', marginBottom: '16px', display: 'flex', alignItems: 'center', gap: '8px' }}>
                        <span style={{ width: '20px', height: '20px', background: 'var(--text-primary)', borderRadius: '50%', display: 'inline-block', opacity: 0.1 }}></span>
                        {blog.author || 'Unknown Author'}
                      </p>

                      <p className="card-summary" style={{ color: 'var(--text-secondary)', lineHeight: '1.6', fontSize: '0.95rem', marginBottom: '24px', flexGrow: 1 }}>
                        {(blog.summary && blog.summary.length > 200) ? blog.summary.substring(0, 200) + '...' : (blog.summary || '')}
                      </p>

                      <div className="card-footer" style={{ marginTop: 'auto', borderTop: '1px solid var(--border-color)', paddingTop: '16px' }}>
                        <a href={blog.url} target="_blank" rel="noopener noreferrer" className="read-more-link" style={{ display: 'inline-flex', alignItems: 'center', gap: '8px', color: 'var(--text-primary)', textDecoration: 'none', fontWeight: '500', fontSize: '0.95rem' }}>
                          Read full article 
                          <span style={{ fontSize: '1.2rem', transition: 'transform 0.2s' }}>→</span>
                        </a>
                      </div>
                    </div>
                  ))}
                </div>
              ) : (
                <div style={{ textAlign: 'center', padding: '60px', backgroundColor: 'var(--card-bg)', borderRadius: '12px' }}>
                  <p style={{ fontSize: '1.2rem', color: 'var(--text-secondary)' }}>No blogs found for this topic.</p>
                </div>
              )}
            </div>
          )}
        </section>
      ) : (
        <>
          {/* 2. Trusted / Social Proof */}
          <section className="trusted">
        <p className="reveal">Trusted by curious minds at</p>
        <div className="trusted-icons reveal" style={{ transitionDelay: '0.1s' }}>
          <div className="trusted-icon" style={{ borderRadius: '8px' }}></div>
          <div className="trusted-icon" style={{ borderRadius: '50%' }}></div>
          <div className="trusted-icon" style={{ clipPath: 'polygon(50% 0%, 0% 100%, 100% 100%)', background: 'transparent', borderBottom: '40px solid var(--text-primary)' }}></div>
          <div className="trusted-icon" style={{ borderRadius: '16px' }}></div>
          <div className="trusted-icon" style={{ borderRadius: '50% 50% 0 0' }}></div>
        </div>
      </section>

      {/* 3. Features Dashboard */}
      <section className="container" style={{ padding: '120px 40px' }}>
        <h2 className="reveal" style={{ fontSize: '3.5rem', textAlign: 'center', marginBottom: '60px' }}>We’ve simplified learning.</h2>
        <div className="features-grid">
          <div className="f-card reveal" style={{ transitionDelay: '0s' }}>
            <h3>Read Deeply</h3>
            <p>Understand concepts holistically, not just step-by-step. Real reading builds intuitive mental models.</p>
          </div>
          <div className="f-card reveal" style={{ transitionDelay: '0.15s' }}>
            <h3>Think Clearly</h3>
            <p>Develop independent engineering thought. Break free from the constraints of passive video observation.</p>
          </div>
          <div className="f-card reveal" style={{ transitionDelay: '0.3s' }}>
            <h3>Learn Faster</h3>
            <p>No fluff, no filler. Only the highest-signal content retrieved instantly by our semantic search engine.</p>
          </div>
          <div className="f-card reveal" style={{ transitionDelay: '0.45s' }}>
            <h3>Stay Consistent</h3>
            <p>Small daily reads lead to massive compounding growth. Level up your technical prowess steadily.</p>
          </div>
        </div>
      </section>

      {/* 4. Full Width 3D Parallax visual */}
      <section className="parallax-section reveal-scale">
        <div 
          className="parallax-bg"
          style={{ transform: `translateY(${bigImageTranslateY}px)` }}
        ></div>
      </section>

      {/* 5. Split Section Layout with 3D elements */}
      <section className="container split-section">
        <div className="split-left">
          <h2 className="reveal">See the bigger picture</h2>
          <div className="split-list">
            <div className="split-list-item reveal" style={{ transitionDelay: '0.1s' }}>
              <div className="split-num">1</div>
              <span>Connect complex ideas seamlessly across multiple blogs</span>
            </div>
            <div className="split-list-item reveal" style={{ transitionDelay: '0.2s' }}>
              <div className="split-num">2</div>
              <span>Learn exponentially faster with ultra-focused reading</span>
            </div>
            <div className="split-list-item reveal" style={{ transitionDelay: '0.3s' }}>
              <div className="split-num">3</div>
              <span>Build real understanding of software architecture</span>
            </div>
            <div className="split-list-item reveal" style={{ transitionDelay: '0.4s' }}>
              <div className="split-num">4</div>
              <span>Escape crippling tutorial dependency forever</span>
            </div>
          </div>
        </div>
        
        <div className="split-right reveal-fade" style={{ transitionDelay: '0.4s' }}>
          <div 
             className="floating-obj-1" 
             style={{ transform: `translateY(${floatObjLeftY}px) scale(1.05)` }}
          ></div>
          <div 
             className="floating-obj-2"
             style={{ transform: `translateY(${floatObjRightY}px) scale(0.95)` }}
          ></div>
        </div>
      </section>

      {/* 6. Why Section */}
      <section className="container" style={{ textAlign: 'center', padding: '140px 0' }}>
        <h2 className="reveal" style={{ fontSize: '3.5rem', marginBottom: '24px' }}>Why choose this platform?</h2>
        <p className="reveal" style={{ transitionDelay: '0.1s', fontSize: '1.3rem', color: 'var(--text-secondary)', maxWidth: '750px', margin: '0 auto', lineHeight: '1.8' }}>
          Social media timelines and algorithm-driven video feeds are weaponized to steal your attention. 
          We built the exact opposite. A distraction-free sanctuary crafted strictly for reading, deep thinking, and compounding growth.
        </p>
      </section>

      {/* 7. Testimonial Section */}
      <section className="container reveal-scale">
        <div className="testimonial-section">
          <img 
             src="https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?auto=format&fit=crop&w=800&q=80" 
             alt="Close up of a classic book showing reading text lines" 
             className="testi-img" 
          />
          <div className="testi-content">
            <p className="testi-quote reveal" style={{ transitionDelay: '0.2s', minHeight: '180px', display: 'flex', alignItems: 'center' }}>
              <span 
                style={{ 
                  display: 'inline-block', 
                  opacity: fadeQuote ? 1 : 0, 
                  transform: fadeQuote ? 'translateY(0)' : 'translateY(15px)',
                  transition: 'opacity 0.6s ease, transform 0.6s cubic-bezier(0.16, 1, 0.3, 1)' 
                }}
              >
                “{ROTATING_QUOTES[quoteIndex]}”
              </span>
            </p>
          </div>
        </div>
      </section>

      {/* 8. Final Call to Action */}
      <section className="hero container" style={{ paddingBottom: '200px', paddingTop: '100px' }}>
        <h2 className="reveal">Start reading. Start thinking.</h2>
        <p className="reveal" style={{ transitionDelay: '0.1s', margin: '20px auto 40px auto', maxWidth: '500px' }}>
          The world's best engineers read vastly more than they write. Join the top 1%.
        </p>
        <button className="btn-primary reveal" style={{ transitionDelay: '0.2s', padding: '18px 48px', fontSize: '1.1rem' }}>
          Explore Blogs
        </button>
      </section>
      </>
      )}

    </div>
  );
}

export default App;
