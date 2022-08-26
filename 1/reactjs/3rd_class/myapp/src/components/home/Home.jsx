import './Home.css';
import { Link } from 'react-router-dom';

const Home = () => {

    let name = "Rafiq Ahmed";
    // let dept = "Dentist";
    // const link = "https://maps.google.com";

    const handleSubmit = () => {
        console.log(name);
    }

    return (
        <div className='home'>
            <h1>Home Page</h1>
            <button onClick={handleSubmit}>Click me</button>
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