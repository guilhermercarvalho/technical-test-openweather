import React from "react";

function Weather(props) {
  return (
    <div class="container">
      <div className="align-items-end">
        <div className="col col-auto">
          <h1>{props.currentWeather.city}</h1>
          <div className="table-responsive text-nowrap">
            <table className="table table-striped">
              <thead>
                <tr>
                  <th scope="col">Cidade</th>
                  <th scope="col">Nebulosidade (%)</th>
                  <th scope="col">País</th>
                  <th scope="col">DateTime</th>
                  <th scope="col">Sensação Térmica (°C)</th>
                  <th scope="col">Humidade (%)</th>
                  <th scope="col">ID</th>
                  <th scope="col">Pressão (hPa)</th>
                  <th scope="col">Temperatura (°C)</th>
                  <th scope="col">Temperatura MAX (°C)</th>
                  <th scope="col">Temperatura MIN (°C)</th>
                  <th scope="col">Visibilidade (KM)</th>
                  <th scope="col">Tempo</th>
                  <th scope="col">Ícone</th>
                  <th scope="col">Tempo Resumo</th>
                  <th scope="col">Velocidade do Vento (%m/s)</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  {Object.keys(props.currentWeather).map((k) => {
                    return (
                      <>
                        <td>{props.currentWeather[k]}</td>
                      </>
                    );
                  })}
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Weather;
