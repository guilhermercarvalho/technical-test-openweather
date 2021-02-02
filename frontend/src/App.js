import { React, useEffect, useState } from "react";
import Form from "./components/Form";
import Weather from "./components/Weather";
import History from "./components/History";

function App(props) {
  const [currentWeather, setCurrentWeather] = useState(undefined);

  const doSearch = async (city) => {
    let result = await window.fetch("/add", {
      method: "post",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ city }),
    });
    
    let res = await result.json();

    setCurrentWeather(res);
  };


  return (
    <div className="container wrapper">
      <header className="title mb-5">
        <h1>Previsão do Tempo</h1>
      </header>

      <article className="mb-5">
        <h2>O que é este projeto</h2>
        <p>
          Sistema de consulta meteorológica que utiliza a API{" "}
          <a href="https://openweathermap.org/">OpenWeatherMap</a>.
        </p>
      </article>

      <Form doSearch={doSearch} />

      { currentWeather ? <Weather currentWeather={currentWeather} /> : <></>}
      <br></br>
      <History />
    </div>
  );
}

export default App;
