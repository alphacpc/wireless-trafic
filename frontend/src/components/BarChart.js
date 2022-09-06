import React, {useEffect, useState} from 'react';
import { Bar } from "react-chartjs-2";

const BarChart = ({data}) => {

  const [dnsData, setDnsData] = useState([])

  const dataDomaine = {
    labels : dnsData.map( element => element.key),
    datasets : [{
      label : "Top 10 des noms de domaines",
      data : dnsData.map( element => element.doc_count),
      backgroundColor : ["#FFC23C", "#EAE3D2"],
      borderColor : "black",
      borderWidth : 2,
    }]  
  }

  useEffect(()=>{
    data && setDnsData(data)
  }, [data])

  return (
    (data != null) ? <Bar data={ dataDomaine } /> : <p className='p-loader'>Chargement en cours !</p>
  )
}

export default BarChart;