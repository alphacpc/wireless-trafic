import './App.css';

function App() {

  var liste = [1,2,3,4,5,6,7,8,1,2,2,2,2]


  return (
    <div className="divAppContainer">
      <div className="divTableStream">
        <table className="table">

          <thead>
            <tr>
              <th>Numero</th>
              <th>Temps</th>
              <th>Source</th>
              <th>Destination</th>
              <th>Protocol</th>
              <th>Information</th>
            </tr>
          </thead>

          <tbody>
           {liste.map(el =>  <tr key={el}>
              <td>444</td>
              <td>Mardi 30 Aout, 16:44:23</td>
              <td>192.X.X.X</td>
              <td>192.X.X.X</td>
              <td>DNS</td>
              <td>www.google.com</td>
            </tr>)}
          </tbody>

        </table>
      </div>
    </div>
  );
}

export default App;
