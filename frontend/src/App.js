import logo from './logo.svg';
import './App.css';
import { Button, Form, Card } from 'react-bootstrap';
import React from 'react';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      query: '',
      links: [],
    };
  }

  handleChange = (event) => {
    this.setState({[event.target.name]: event.target.value});
  }

  handleSubmit = (event) => {
    var that = this;
    fetch(`http://localhost:5000/search?query=${this.state.query}`, {
        method: 'GET',
        // We convert the React state to JSON and send it as the POST body
        // body: JSON.stringify(this.state)
      }).then(function(response) {
        response.json().then(json => that.setState({links: json}))
      });

    event.preventDefault();
}


  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <p>
            <code>FAANGMULA</code> Job Search Engine
          </p>
        </header>
        <div className="App-body">
          <Form onSubmit={this.handleSubmit} className="App-form">
            <Form.Group controlId="query" className="App-text-input">
              <Form.Control type="text" value={this.state.value} name="query" onChange={this.handleChange} />
            </Form.Group>
            <Button variant="success" type="submit" className="App-button">
              Search
            </Button>
          </Form>
          <div className="App-result">
            {
              this.state.links.map((link, index) =>
              <Card key={index}>
                <Card.Body><a href={link}>{link}</a></Card.Body>
              </Card>
              )
            }
          </div>
        </div>

      </div>
    );
  }
}

export default App;
