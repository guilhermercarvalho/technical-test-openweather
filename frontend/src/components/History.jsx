import { React, useState, useEffect } from "react";
import { DataGrid } from "@material-ui/data-grid";

function History(props) {
  const [queryHistory, setQueryHistory] = useState([]);

  useEffect(() => {
    async function fetchData() {
      let res = await window.fetch("/history");
      res = await res.json();
      setQueryHistory(res);
    }
    fetchData();
  }, [props.currentWeather]);

  const defineColumns = () => {
    return [
      { field: "city", headerName: "Cidade" },
      { field: "cloudiness", headerName: "Nebulosidade" },
      { field: "country", headerName: "País" },
      { field: "dt", headerName: "DateTime" },
      { field: "feels_like", headerName: "Sensação Térmica" },
      { field: "humidity", headerName: "Humidade" },
      { field: "id", headerName: "ID" },
      { field: "pressure", headerName: "Pressão" },
      { field: "temp", headerName: "Temperatura" },
      { field: "temp_max", headerName: "Temperatura MAX" },
      { field: "temp_min", headerName: "Temperatura MIN" },
      { field: "visibility", headerName: "Visibilidade" },
      { field: "weather_description", headerName: "Tempo" },
      { field: "weather_icon", headerName: "Ícone" },
      { field: "weather_main", headerName: "Tempo Resumo" },
      { field: "wind_speed", headerName: "Velocidade do Vento" },
    ];
  };

  return (
    <div className="container">
      <div className="align-items-end">
        <div className="col col-auto">
          <h1>Histórico</h1>
          <div style={{ height: 400, width: "100%" }}>
            <DataGrid
              rows={queryHistory}
              columns={defineColumns()}
              pageSize={5}
            />
          </div>
        </div>
      </div>
    </div>
  );
}

export default History;
