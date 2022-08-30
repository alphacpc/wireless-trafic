import './App.css';
import bar from "./assets/images/bar.jpg"
import maps from "./assets/images/maps.jpg"
import line from "./assets/images/line.png"

function App() {

  var liste = [1,2,3,4,5,6,7,8,1,2,2,2,2]

  //https://datasciencesphere.com/project/track-location-ip-address-python-geocoder/


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
              <th>Informations</th>
            </tr>
          </thead>

          <tbody>
           {liste.map( (el,ind) =>  (<tr key={ind} >
              <td>444</td>
              <td>Mardi 30 Aout, 16:44:23</td>
              <td>192.X.X.X</td>
              <td>192.X.X.X</td>
              <td>DNS</td>
              <td>www.google.com</td>
            </tr>))}
          </tbody>

        </table>
      </div>

      <div className="divGraphes">
        
        <div className="divGraphItem lineChart">
          <img src={line} alt="line" />
        </div>

        <div className="divGraphItem barChart">
          <img src={bar} alt="line" />
        </div>

      </div>

      <div className="divGeos">

        <div className="divGeoItem divInf">
          <h2>Hello world !!!</h2>
        </div>

        <div className="divGeoItem divMaps">
          <img src={maps} alt="Geo" />
        </div>
      </div>

    </div>
  );
}

export default App;
