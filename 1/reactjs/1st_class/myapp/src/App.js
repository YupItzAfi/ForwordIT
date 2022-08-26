import logo from './logo.svg';
import './App.css';

function App() {

  let name = "Yeasin";
  let name2 = "mamun";

  const address = "Dhaka";

  return (
    <div className="App">
      <header className="App-header">
        <div className='name'>
          {name}
          {name2}
          {address}
        </div>
      </header>
    </div>
  );
}

export default App;
