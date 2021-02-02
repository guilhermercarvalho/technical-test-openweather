import React, { useState } from "react";

function Form({ doSearch }) {
  const [city, setCity] = useState("");

  function handleSubmit(e) {
    e.preventDefault();
    doSearch(city);
  }

  return (
    <div className="container">
      <div className="align-items-center">
        <div className="col col-auto">
          <form onSubmit={handleSubmit}>
            <div className="input-group mb-3">
              <input
                name="city"
                className="form-control"
                placeholder="Selecione uma cidade"
                type="text"
                value={city}
                required
                onChange={(e) => setCity(e.target.value)}
              ></input>
              <button className="btn btn-primary" type="submity">
                Pesquisar
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
}

export default Form;
