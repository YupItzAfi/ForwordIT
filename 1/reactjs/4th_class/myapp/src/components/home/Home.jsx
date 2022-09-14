import { useState, useEffect } from 'react';
import './Home.css';
import '../BlogList'
import BlogList from '../BlogList';
// import { Link } from 'react-router-dom';
const Home = () => {

    const [blogs, setBlog] = useState(null);
    // let name = "Rafiq Ahmed";
    // let dept = "Dentist";
    // const link = "https://maps.google.com";

    // const [name, setName] = useState('Rafiq Ahmed')
    // const [age, setAge] = useState(34)

    // const handleSubmit = () => {
    //     console.log(name);
    //     setName("Tamim Subin");
    //     setAge(32);
    // }

    // const showName = (name, e) => {
    //     console.log('Welcome ' + name, e.target)
    // }


    const handleClick = (id) => {
        const newblog = blogs.filter(blogs => blogs.id !== id);
        setBlog(newblog);
    }

    // const [name, setName] = useState('Tarek');

    useEffect(() => {
        fetch("http://localhost:4000/blogs")
            .then((res) => {
                return res.json();
            })
            .then((data) => {
                console.log(data);
                setBlog(data);
            })
        // console.log("use effect run!");
        // console.log(blogs);
    }, []);

    return (
        <div className='home'>
            {blogs && <BlogList blogs={blogs} title={'Home Blogs'} handleClick={handleClick} />}
            {/* <button onClick={() => setName("Aziz")}>Change Name</button> */}
            {/* <p>{name}</p> */}
            {/* <h1>Home Page</h1>
            <button onClick={handleSubmit}>Click me</button>
            <button onClick={(e) => {
                showName('hasan', e)
            }}>Show Name</button>

            <p>{name}</p>
            <p>{age}</p> */}
            {/* <h3>Home Page</h3>
            <p>{name}</p>
            <p>{dept}</p>
            <p>{"Dhaka"}</p>
            <p>{[1, 2, 3, 4, 5]}</p>
            <p>{Math.random() * 100}</p>
            <a href={link}>Google</a> */}
        </div>
    )
}

export default Home;