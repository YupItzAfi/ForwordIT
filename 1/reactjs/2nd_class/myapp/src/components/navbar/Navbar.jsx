import './Navbar.css';

const Navbar = () => {
    return (
        <nav className="navbar">
            <h1>My Blog</h1>
            <div className="links">
                <a href="/">Home</a>
                <a href="/about">About</a>
                <a href="/blogs">Blogs</a>
            </div>
        </nav>
    )
}

export default Navbar;