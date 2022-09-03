import React, { useEffect, useState } from "react"
import './App.css';
import bar from "./assets/images/bar.jpg"
import maps from "./assets/images/maps.jpg"
import line from "./assets/images/line.png"


import { Bar } from "react-chartjs-2"
import {Chart as ChartJs} from "chart.js/auto"

function App() {

  let [timer, setTimer] = useState(0)
  let [tabs, setTabs] = useState([])
  // let [protocol, setProtocol ] = useState([])
  let [protocolData, setProtocolData] = useState(null)

  let handleFetcher = async () => {
    let response = await fetch("http://127.0.0.1:5000/")
    let data = await response.json()
    setTabs(data.data)
  }

  let handleProtocole = async () => {
    let response = await fetch("http://localhost:5000/protocol")
    let data = await response.json()
    data = data.data

    console.log("Valeur de data => ", data)

    setProtocolData({
      labels : data.map( element => element.key),
      datasets : [{
        label : "Hello World",
        data : data.map( element => element.doc_count)
      }]  
    })
    console.log("Datas Protocoles les deux => ", data, protocolData)
  }

  let handleLength = async () => {
    let response = await fetch("http://localhost:5000/length")
    let data = await response.json()
    console.log("Datas length => ", data)
  }

  let handleTable = (tabs) => {
    return (tabs.map( (capture,ind) =>  (<tr key={ind} className={capture['_source']['dst_port']}>
      <td>{ ind + 1 }</td>
      <td>{capture['_source']['localtime']}</td>
      <td>{capture['_source']['protocol']}</td>
      <td>{capture['_source']['src_port']}</td>
      <td>{capture['_source']['dst_port']}</td>
      <td>{capture['_source']['information']}</td>
    </tr>)))
  }


  let loaded = (tabs.length === 0) ? <tr><td>Chargement en cours !</td></tr> : handleTable(tabs)

  setTimeout( () => {
    setTimer(timer => timer = timer + 1)
  }, 10000)

  // let b

  // b = 


  useEffect(()=>{
    
    handleFetcher()

    handleLength()

    handleProtocole()



  }, [timer])




  return (
    <div className="divAppContainer">
      
      <div className="divTableStream cadre-table-scroll">
        <table className="table table-scroll">

          <thead>
            <tr>
              <th>Numero</th>
              <th>Date & Heure</th>
              <th>Source</th>
              <th>Destination</th>
              <th>Protocol</th>
              <th>Informations</th>
            </tr>
          </thead>

          <tbody> { loaded } </tbody>

        </table>
      </div>

      <div className="divGraphes">
        <div id="myChart">
          { 
            (protocolData != null) ? <Bar data={protocolData} /> : "Hello"
          }
        </div>
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
