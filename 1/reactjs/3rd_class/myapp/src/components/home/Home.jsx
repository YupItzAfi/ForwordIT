import { useState } from 'react';
import './Home.css';
// import { Link } from 'react-router-dom';
const Home = () => {

    const [blog, setBlog] = useState([
        {
            title: "Title 1",
            description: "Lorem ipsum dolor sit, amet consectetur adipisicing elit.Odio eaque voluptates architecto, laboriosam iste ratione accusamus similique deserunt ut voluptatem! Repellat recusandae inventore sint voluptas facilis rem mollitia quas maiores.",
            body: "Lorem ipsum dolor sit ...",
            author: "subin",
            id: 1
        },
        {
            title: "Title 2",
            description: "Lorem ipsum dolor sit, amet consectetur adipisicing elit.Odio eaque voluptates architecto, laboriosam iste ratione accusamus similique deserunt ut voluptatem! Repellat recusandae inventore sint voluptas facilis rem mollitia quas maiores.",
            body: "Lorem ipsum dolor sit ...",
            author: "Tamim",
            id: 2
        },
        {
            title: "Title 3",
            description: "Lorem ipsum dolor sit, amet consectetur adipisicing elit.Odio eaque voluptates architecto, laboriosam iste ratione accusamus similique deserunt ut voluptatem! Repellat recusandae inventore sint voluptas facilis rem mollitia quas maiores.",
            body: "Lorem ipsum dolor sit ...",
            author: "Karim",
            id: 3
        },
    ]);
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

    return (
        <div className='home'>
            <h1>Blogs</h1>
            <div>{blog.map((b) => (
                <div className='blog-preview' key={b.id}>
                    <h2>{b.title}</h2>
                    <p><small>{b.author}</small></p>
                    <p>{b.body}</p>
                </div>
            ))}</div>
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