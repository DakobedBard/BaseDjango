import React, { Component } from 'react';
import logo from '../img/logo.svg';
import '../css/App.css';

import _ from "lodash";
import ListItem from './ListItem.jsx';
//class App extends Component {
//  render() {
//    return (
//      <div className="App">
//        <header className="App-header">
//          <img src={logo} className="App-logo" alt="logo" />
//          <h1 className="App-title">Welcome to React</h1>
//        </header>
//        <p className="App-intro">
//          To get started, edit <code>src/components/App.js</code> and save to reload.
//        </p>
//      </div>
//    );
//  }
//}

class DocumentList extends Component {
  constructor(props) {
    super(props);

    this.state = {
      chores: [
        {
          id: 1,
          name: "Take out trash",
          description: "Trash removal from both bins",
          completed: true
        },
        {
          id: 2,
          name: "Do the Dishes",
          description: "Wash and dry the dishes",
          completed: false
        },
        {
          id: 3,
          name: "Walk the Dog",
          description: "Take dog around the block 2 times",
          completed: true
        }
      ]
    };
  }

  handleOnClick = id => {
    const chores = _.cloneDeep(this.state.chores);

    for (let chore of chores) {
      if (chore.id === id) {
        chore.completed = !chore.completed;
        break;
      }
    }

    this.setState({ chores });
  };

  render() {
    const { chores } = this.state;
    return (
      <div className="App">
        <h1>Chores</h1>
        <ul>
          {chores.map(chore => (
            <ListItem
              key={chore.id}
              id={chore.id}
              name={chore.name}
              completed={chore.completed}
              description={chore.description}
              handleOnClick={this.handleOnClick}
            />
          ))}
        </ul>
      </div>
    );
  }
}

//export default App;
export default DocumentList;

