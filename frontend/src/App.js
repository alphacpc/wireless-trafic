import React, { useEffect, useState } from "react"
import './App.css';

import {Chart as ChartJs} from "chart.js/auto"
import LineChart from "./components/LineChart";
import BarChart from "./components/BarChart";
import LineChartMulti from "./components/LineChartMulti";




function App() {

  let [timer, setTimer] = useState(0)
  let [tabs, setTabs] = useState([])
  let [protocolData, setProtocolData] = useState(null)
  let [lengthData, setLengthData] = useState(null)

  let handleFetcher = async () => {
    let response = await fetch("http://127.0.0.1:5000/")
    let data = await response.json()
    setTabs(data.data)
  }

  let handleProtocole = async () => {
    let response = await fetch("http://localhost:5000/protocol")
    let data = await response.json()
    data = data.data

    setProtocolData({
      labels : data.map( element => element.key),
      datasets : [{
        label : "Lorem ipsum",
        data : data.map( element => element.doc_count),
        backgroundColor : ["#EAE3D2", "#FFC23C"],
        borderColor : "black",
        borderWidth : 2,

      }]  
    })
  }

  let handleLength = async () => {
    let response = await fetch("http://localhost:5000/length")
    let data = await response.json()
    data = data.data

    setLengthData({
      labels : data.map( element => element.key),
      datasets : [{
        label : "Lorem ipsum",
        data : data.map( element => element.doc_count),
        backgroundColor : ["#FFC23C", "#D4F6CC"],
        borderColor : "#FFC23C",
        borderWidth : 1
      }]  
    })
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
  }, 5000)


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

        <div className="divGraphItem lineChart">
          <LineChartMulti/>
        </div>

        <div className="divGraphItem barChart">
          <BarChart protocol={protocolData}/>
        </div>

      </div>

    </div>
  );
}

export default App;
